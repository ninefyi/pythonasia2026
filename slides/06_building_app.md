---
marp: true
paginate: true
theme: default
---

# Building the App

## Putting it all together with Django

---

## Project Structure

```shell
my_project/
├── manage.py
├── my_project/
│   ├── settings.py
│   └── urls.py
└── recommendation/
    ├── models.py      # Data Schema
    ├── views.py       # Search Logic
    ├── urls.py        # Routes
    └── templates/     # UI
```

---

## Step 1: Django Setup (1/2)

- Initialize Django:

```bash
django-admin startproject pythonasia_hybrid
cd pythonasia_hybrid
python manage.py startapp recommendation
```

---

## Step 2: Settings (1/2)

- Add `recommendation` to `INSTALLED_APPS` in `settings.py`.
- Configure MongoDB Connection in `settings.py` (or a utility file).
  - Django uses SQLite by default. We will bypass the ORM for search.

---

## Step 3: The Data Model (1/2)

- In `models.py`:
  - We might simply define a class to represent our document structure,
    even if not using Django ORM fully.

```python
# Conceptual Schema
{
    "title": "Movie Title",
    "plot": "Movie description...",
    "embedding": [0.1, ...]
}
```

---

## Step 4: Ingestion Script (1/3)

- We need data!
- Create a management command: `recommendation/management/commands/ingest.py`.
- Function:
    1. Load dataset (e.g., sample movies CSV).
    2. Loop through rows.
    3. Generate Embedding using VoyageAI.
    4. Insert into MongoDB `collection.insert_one()`.

---

## Step 4: Ingestion Script (2/3)

```python
# Pseudocode
for movie in movies:
    emb = voyage_client.embed([movie['plot']]).embeddings[0]
    doc = {
        "title": movie['title'],
        "plot": movie['plot'],
        "embedding": emb
    }
    collection.insert_one(doc)
```

---

## Step 4: Ingestion Script (3/3)

- Run it:

```bash
python manage.py ingest
```

- Verify data in Atlas UI.

---

## Step 5: The Search View (1/4)

- In `views.py`.
- Create a function `search_view(request)`.
- Get query from `request.GET.get('q')`.

---

## Step 5: The Search View (2/4)

- **Vector Logic**:

```python
query_vec = voyage_client.embed([query]).embeddings[0]
vector_results = collection.aggregate([
    {"$vectorSearch": { ... }}
])
```

---

## Step 5: The Search View (3/4)

- **Keyword Logic**:

```python
keyword_results = collection.aggregate([
    {"$search": {
        "text": {
            "query": query,
            "path": "plot"
        }
    }}
])
```

---

## Step 5: The Search View (4/4)

- **Hybrid Fusion**:
  - Combine `vector_results` and `keyword_results`.
  - Apply RRF (Reciprocal Rank Fusion).
  - Sort by final score.

---

## Step 6: The Template (UI) (1/3)

- `templates/recommendation/index.html`.
- Simple Search Bar form.
- Loop through results.

---

## Step 6: The Template (UI) (2/3)

```html
<form method="GET">
    <input type="text" name="q" placeholder="Describe a movie...">
    <button type="submit">Recommend</button>
</form>

{% for result in results %}
    <div class="card">
        <h3>{{ result.title }}</h3>
        <p>{{ result.plot }}</p>
    </div>
{% endfor %}
```

---

## Step 7: Running the Server

```bash
python manage.py runserver
```

- Go to `http://127.0.0.1:8000`.
- Try it out!

---

## Live Demo Time

- Use queries that test *concepts*.
  - "A movie about sad robots" -> Should find "Wall-E" (even if words don't match).
- Use queries that test *keywords*.
  - "Star Wars" -> Should find "Star Wars" explicitly.

---

## Troubleshooting

- **No Results?** Check if Index is built in Atlas.
- **Error?** Check Dimension match (1024).
- **Slow?** Check internet connection (API calls).

---

## Final Review

- We built a full pipeline!
- Data -> Chunking -> Embedding -> Indexing -> Search -> UI.
- All in < 100 lines of core logic.

---

## Wrap Up

- Hybrid search is powerful.
- Easy to implement with MongoDB + VoyageAI.
- Python & Django make it accessible.
