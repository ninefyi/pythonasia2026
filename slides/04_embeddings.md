---
marp: true
paginate: true
theme: default
---

<!-- markdownlint-disable-file MD029 MD036 MD026 -->

# Embedding Generation

## From Text to Vectors with VoyageAI

---

## What are Embeddings? (1/2)

- We learned about chunks (text).
- Computers don't understand text; they understand numbers.
- **Embeddings** turn text into a list of numbers.
  - "Apple" -> `[0.1, 0.5, -0.2]`
  - "Fruit" -> `[0.1, 0.6, -0.1]`

---

## What are Embeddings? (2/2)

- **Semantic Meaning**:
  - The numbers represent *concepts*.
  - Similar concepts have similar numbers.
  - "King" - "Man" + "Woman" ≈ "Queen" (Logic in vector space).

---

## Why VoyageAI? (1/2)

- **Specialized**:
  - Built specifically for retrieval (RAG).
  - Optimized for code and text.
- **High Performance**:
  - Generates dense vectors (1024 dimensions).
  - Captures nuance better than generic models.

---

## Why VoyageAI? (2/2)

- **Model Choices**:
  - `voyage-4-large`: General purpose, high quality.
  - `voyage-code-3`: Optimized for code search.
  - `voyage-4-lite`: Lightweight, fast.

---

## The Embedding Process (1/3)

1. **Input**: Send chunk to VoyageAI API.
2. **Process**: Model converts tokens to vector.
3. **Output**: Receive a list of 1024 floats.

---

## The Embedding Process (2/3)

```python
import voyageai

vo = voyageai.Client()

text = "This is a movie about space travel."
vector = vo.embed([text], model="voyage-4-large").embeddings[0]

print(len(vector)) 
# Output: 1024
```

---

## The Embedding Process (3/3)

- **Batching**:
  - Don't send one by one!
  - Send a list of texts `["doc1", "doc2", ...]`.
  - Saves API calls and time.

---

## Vector Dimensions (1/2)

- **Dimension**: The length of the vector list.
- **voyage-4-large**: 1024 dimensions.
- **OpenAI Ada-002**: 1536 dimensions.
- **Importance**:
  - You MUST use the same model for query and documents.
  - You cannot compare a 1024-dim vector with a 1536-dim vector.

---

## Vector Dimensions (2/2)

- **Storage**:
  - Storing vectors requires space.
  - 1024 floats * 4 bytes = ~4KB per document.
  - 1M docs = ~4GB index size.

---

## Storing in MongoDB (1/2)

- MongoDB handles vectors natively.
- No special "Vector DB" needed.
- Just add a field to your document.

```json
{
  "_id": "...",
  "title": "Star Wars",
  "description": "A space opera...",
  "embedding": [0.12, -0.45, ...] // The vector
}
```

---

## Storing in MongoDB (2/2)

- **Atlas Vector Search Index**:
  - You must create an index to search fast.
  - Algorithm: `HNSW` (Hierarchical Navigable Small World) - fast and accurate.
  - Or `IVF` (Inverted File) - good for massive datasets.

---

## Creating the Index (1/3)

- In Atlas UI -> Atlas Search -> Create Index.
- Configuration JSON:

```json
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 1024,
      "similarity": "cosine"
    }
  ]
}
```

---

## Creating the Index (2/3)

- **Analysis**:
  - **path**: Which field holds the vector? (`embedding`)
  - **numDimensions**: Must match model! (1024 for voyage-4-large)
  - **similarity**: How to measure distance? (`cosine` is standard).

---

## Creating the Index (3/3)

- Wait for the index to build.
- Usually takes seconds for small data.
- Once active, you can query!

---

## Inspecting the Data (1/2)

- Use MongoDB Compass or Atlas Data Explorer.
- You will see the array of numbers.
- **Human Readable?** No.
- **Machine Readable?** Yes.

---

## Inspecting the Data (2/2)

- Don't try to edit vectors manually.
- Always regenerate them from text if the text changes.

---

## Common Pitfalls

- **Mixing Models**: Using OpenAI to query a Voyage index. (Garbage results).
- **Dimension Mismatch**: Index expects 1024, you send 1536. (Error).
- **Normalization**: Some models require normalized vectors; Voyage usually
  handles this.

---

## Exercise: Generate your first embedding

1. Open `test_voyage.py`.
2. Enter a sentence.
3. Print the first 5 numbers.
4. Change a word, print again.
5. Notice how the numbers change slightly!

---

## Next Steps

- We have vectors stored.
- Now, how do we find the "closest" one?
- **Similarity Functions**.
