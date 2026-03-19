
# PythonAsia 2026: Building a Hybrid Search Recommendation System

This repository contains the workshop materials and code for the "Building a Recommendation System with a Hybrid Search From Scratch" session.

## Structure

- `slides/`: Markdown source for the workshop slides.
- `django_app/`: The complete Django application code.
- `diagrams/`: Mermaid diagrams used in the workshop.

## Getting Started

Follow these steps to set up your environment and run the workshop materials.

## Notebook-First Class Path (Beginner Recommended)

For classroom delivery, use the notebooks in this order:

1. `notebooks/00_welcome_and_outcomes.ipynb`
2. `notebooks/01_environment_check.ipynb`
3. `notebooks/02_chunking_lab.ipynb`
4. `notebooks/03_embeddings_lab.ipynb`
5. `notebooks/04_similarity_lab.ipynb`
6. `notebooks/05_mongodb_search_lab.ipynb`
7. `notebooks/06_hybrid_fusion_lab.ipynb`
8. `notebooks/07_mini_challenge.ipynb`
9. `notebooks/08_bridge_to_django.ipynb`

Suggested pacing for a 2-hour beginner session:

- 10 min: 00 + 01 (go/no-go checks)
- 20 min: 02 (chunking intuition)
- 20 min: 03 (embedding generation)
- 15 min: 04 (cosine ranking basics)
- 25 min: 05 (MongoDB vector + keyword search)
- 15 min: 06 (RRF fusion)
- 10 min: 07 + 08 (challenge + app bridge)

Classroom checkpoint policy:

- Do not move past Notebook 01 until all checks pass.
- If API/network fails during class, continue with Notebooks 02, 04, 06, and 08 while troubleshooting.

### 1. Prerequisites

Before you begin, ensure you have the following:

- **Python 3.10+**: [Download here](https://www.python.org/downloads/)
- **MongoDB Atlas Account**: [Sign up for free](https://www.mongodb.com/cloud/atlas/register)
- **Marp CLI** (for slides): Install via npm: `npm install -g @marp-team/marp-cli`

### 2. Initial Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/20260321_PythonAsia2026.git
   cd 20260321_PythonAsia2026
   ```

2. **Run the setup script**:
   This script installs `uv`, creates a virtual environment, and installs all dependencies.

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Activate the virtual environment**:

   ```bash
   source .venv/bin/activate
   ```

### 3. Configuration

Create a `.env` file in the `django_app/` directory to store your credentials:

```bash
# Path: django_app/.env
MONGODB_URI="mongodb+srv://<user>:<password>@cluster.mongodb.net/pythonasia2026_workshop?retryWrites=true&w=majority"
VOYAGE_API_KEY="vy-your-actual-api-key-here"
DB_NAME="pythonasia2026_workshop"
COLLECTION_NAME="recommendation_movies"
```

### 4. Verify Your Setup (Optional but Recommended)

Run the included diagnostic script to ensure your VoyageAI connection is working:

```bash
python test_voyage.py
```

*If prompted, enter a sample sentence. You should see the embedding dimensions and the first few vector values.*

If you are teaching or learning with notebooks, run `notebooks/01_environment_check.ipynb` immediately after this step.

### 5. Data Ingestion & Database Setup

Initialize the MongoDB collection and ingest the sample movie data:

```bash
cd django_app
python manage.py migrate
python manage.py ingest
```

### 6. Run the Recommendation Application

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to test the Hybrid Search.

---

## Viewing the Workshop Slides

The slides are written in Markdown and can be viewed using Marp.

1. **Start the Marp server**:
   From the project root directory, run:

   ```bash
   marp -s slides/
   ```

2. **Open in Browser**:
   Open [http://localhost:8080](http://localhost:8080) to view the interactive presentation.

---

## Key Concepts Covered

- **Hybrid Search**: Combining Vector Search (Semantic) and Text Search (Keyword).
- **RRF (Reciprocal Rank Fusion)**: The algorithm used to merge the two result sets.
- **VoyageAI**: The embedding model provider.
