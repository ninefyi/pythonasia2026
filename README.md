
# PythonAsia 2026: Building a Hybrid Search Recommendation System

This repository contains the workshop materials and code for the "Building a Recommendation System with a Hybrid Search From Scratch" session.

## Structure

- `slides/`: Markdown source for the workshop slides.
- `django_app/`: The complete Django application code.
- `diagrams/`: Mermaid diagrams used in the workshop.

## Getting Started

### Prerequisites

- Python 3.10+
- `uv` (will be installed by setup script if missing)
- `marp-cli` (for viewing slides)
- MongoDB Atlas Account
- VoyageAI API Key

### Setup

1. **Clone existing repository**:

    ```bash
    git clone https://github.com/yourusername/20260321_PythonAsia2026.git
    cd 20260321_PythonAsia2026
    ```

2. **Run Setup Script**:

    ```bash
    ./setup.sh
    ```

    This will install `uv`, create a virtual environment, and install all dependencies.

3. **Environment Variables**:
    Create a `.env` file in `django_app/`:

    ```env
    MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority
    VOYAGE_API_KEY=vy-your-api-key
    ```

4. **Ingest Data**:

    ```bash
    source .venv/bin/activate
    cd django_app
    python manage.py makemigrations
    python manage.py migrate
    python manage.py ingest
    ```

5. **Run Server**:

    ```bash
    python manage.py runserver
    ```

    Open `http://127.0.0.1:8000/search` to test.

## Viewing Slides

To view the slides, use `marp-cli`:

```bash
marp -s slides/
```

This will start a local server to view the presentation.

## Key Concepts

- **Hybrid Search**: Combining Vector Search (Semantic) and Text Search (Keyword).
- **RRF (Reciprocal Rank Fusion)**: The algorithm used to merge the two result sets.
- **VoyageAI**: The embedding model provider.

## Contact

- Instructor: [Your Name]
