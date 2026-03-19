---
marp: true
paginate: true
theme: default
---

<!-- markdownlint-disable-file MD029 MD036 MD026 -->

# PythonAsia 2026 Workshop

## Building a Recommendation System with a Hybrid Search From Scratch

---

## Workshop Agenda (2 Hours)

1. **Introduction to Hybrid Search** (10 mins)
2. **Environment Setup** (20 mins)
3. **Chunking Fundamentals** (20 mins)
4. **Embedding Generation with VoyageAI** (20 mins)
5. **Similarity Functions** (20 mins)
6. **Building the Recommender App** (25 mins)
7. **Q&A** (5 mins)

---

## What is a Recommendation System? (1/2)

- A system that predicts a user's preference for an item.
- Used in:
  - E-commerce (Amazon: "Customers who bought this...")
  - Streaming (Netflix: "Because you watched...")
  - Social Media (TikTok/Instagram feeds)

---

## What is a Recommendation System? (2/2)

- **Two Approaches**:
  1. **Collaborative Filtering**: Based on user behavior (users who
     liked X also liked Y).
  2. **Content-Based Filtering**: Based on item properties (Description,
     Tags, Genre).
- **Our Focus**: Content-based filtering using **Hybrid Search**.

---

## The Problem with Traditional Search (1/3)

- **Scenario**: You want to buy a "warm winter coat".
- **Traditional Search (Keyword/Lexical)**:
  - Looks for exact matches: "warm", "winter", "coat".
- **Result**: Finds products with these exact words.

---

## The Problem with Traditional Search (2/3)

- **What if...**
  - A product is described as "Insulated Parka for low temperatures".
  - It contains NO words "warm", "winter", or "coat".
- **Outcome**: The keyword search FAILS to find this relevant item.

---

## The Problem with Traditional Search (3/3)

- **Lexical Gap**:
  - Users search for *concepts*.
  - Keyword search looks for *strings*.
- **Synonyms**: "Automobile" vs. "Car".
- **Polysemy**: "Bank" (River) vs. "Bank" (Money).

---

## Enter Semantic Search (Vector Search) (1/3)

- **Idea**: Search based on *meaning*, not just words.
- **How?**: Convert text into numbers (Vectors).
- **Embeddings**: A list of floating-point numbers representing semantic meaning.
  - `[0.1, -0.5, 0.8, ...]`

---

## Enter Semantic Search (Vector Search) (2/3)

- **Vectors in Space**:
  - Similar concepts are close together in vector space.
  - "King" is close to "Queen".
  - "Warm coat" is close to "Insulated parka".

---

## Enter Semantic Search (Vector Search) (3/3)

- **Pros**:
  - Handles synonyms well.
  - Captures intent ("I'm cold" -> suggests "Heater").
  - Cross-lingual capabilities.
- **Cons**:
  - Ignores exact keywords (Product IDs, specific names).
  - Can be "too fuzzy".

---

## The Best of Both Worlds: Hybrid Search (1/3)

- **Hybrid Search** combines:
  1. **Keyword Search (BM25)**: Precision, exact matches.
  2. **Vector Search (Semantic)**: Context, meaning, flexible phrasing.

---

## The Best of Both Worlds: Hybrid Search (2/3)

- **How it works**:
  1. Run Keyword Search -> Get List A.
  2. Run Vector Search -> Get List B.
  3. **Rerank and Fuse**: Combine List A and List B into a final ranked list.

---

## The Best of Both Worlds: Hybrid Search (3/3)

- **Reciprocal Rank Fusion (RRF)**:
  - A common algorithm to combine ranked lists.
  - Does not normalize scores (avoids scale issues).
  - Favors items that appear high in *both* lists.

---

## Architecture We Will Build (1/2)

- **Frontend**: Django Templates (HTML/CSS)
- **Backend**: Django (Python)
- **Database**: MongoDB Atlas
  - Stores Product Data (JSON)
  - Stores Vectors (Embeddings)
  - Performs Hybrid Search

---

## Architecture We Will Build (2/2)

- **AI Components**:
  - **Embeddings**: VoyageAI (Converts text to vectors)
  - **Orchestration**: LangChain (Manages the flow)
  - **Chunking**: LangChain Text Splitters

---

## Why MongoDB?

- **Flexible Schema**: Perfect for product catalogs with varied attributes.
- **Vector Search Native**: No need for a separate vector DB (e.g., Pinecone/Milvus).
- **Atlas Search**: Built-in Lucene engine for powerful full-text search.
- **All-in-One**: Data + Search + Vectors in one place.

---

## Why VoyageAI?

- **State-of-the-art Embeddings**: High performance on retrieval benchmarks.
- **Specialized Models**: `voyage-4-large`, `voyage-code-3`.
- **Context Window**: Supports large context lengths.

---

## Let's Get Started!

- Ready to build?
- Next step: **Environment Setup**.
