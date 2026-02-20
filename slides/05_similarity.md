---
marp: true
paginate: true
theme: default
---

# Similarity Functions

## The Math of Search

---

## How do we measure "Closeness"?

- In a 2D map, we measure distance in meters/miles.
- In Vector Space, we measure **Similarity**.
- High Similarity = Low Distance.
- Low Similarity = High Distance.

---

## Types of Similarity (1/3)

1. **Euclidean Distance (L2)**:
    - Straight-line distance between two points.
    - Like measuring with a ruler.
    - Good for dense data where magnitude matters.
    - **Formula**: `sqrt(sum((a - b)^2))`

---

## Types of Similarity (2/3)

1. **Dot Product**:
    - Measures alignment of two vectors.
    - Multiplies magnitudes.
    - Favors longer vectors (if not normalized).
    - **Formula**: `sum(a * b)` for all dimensions.

---

## Types of Similarity (3/3)

1. **Cosine Similarity** (The Gold Standard):
    - Measures the **Angle** between vectors.
    - Ignores magnitude (length).
    - Focuses on direction (meaning).
    - **Formula**: `(A . B) / (||A|| * ||B||)`
    - Range: -1 (Opposite) to 1 (Identical).

---

## Why Cosine Similarity? (1/2)

- Text length shouldn't matter too much.
  - "Great movie" vs "This is a great movie".
  - Vectors might have different lengths, but point in the same direction.
- Cosine captures that *thematic* alignment.

---

## Why Cosine Similarity? (2/2)

- Most embedding models (including Voyage) are trained for Cosine Similarity.
- MongoDB Atlas Vector Search is optimized for it.

---

## Visualizing Cosine (1/2)

- Imagine two arrows starting from `(0,0)`.
- Arrow A: "Dog"
- Arrow B: "Puppy"
- They point in almost the same direction. Angle is small (0 degrees).
  Cosine is ~1.0.

---

## Visualizing Cosine (2/2)

- Arrow C: "Cat"
- Points differently, but still "animal" direction. Angle ~45 degrees. Cosine ~0.7.
- Arrow D: "Car"
- Points in a totally different way. Angle ~90 degrees. Cosine ~0.0.

---

## Performing the Search (1/3)

- Users types query: "Space adventure".

1. Convert "Space adventure" to query vector `v_q`.
2. Compare `v_q` against **ALL** document vectors `v_d` in DB?
    - Too slow if you have 1B documents!

---

## Performing the Search (2/3)

- **ANN (Approximate Nearest Neighbor)**:
  - We don't compare all.
  - We use the HNSW index to quickly navigate to the "neighborhood".
  - Trades tiny accuracy loss for massive speed.

---

## MongoDB Aggregation (1/3)

- We use an aggregation pipeline `$vectorSearch`.

```javascript
[
  {
    "$vectorSearch": {
      "index": "vector_index",
      "path": "embedding",
      "queryVector": [0.1, ...], // Query Embed
      "numCandidates": 100,
      "limit": 10
    }
  }
]
```

---

## MongoDB Aggregation (2/3)

- **numCandidates**: How many neighbors to look at initially (Broad search).
- **limit**: How many final results to return (Top K).

---

## The Hybrid Part (1/2)

- Recap:
  - Vectors find "meaning".
  - Keywords find "exact matches".
- **Hybrid Search**: Combine `$search` (Lucene) and `$vectorSearch`.

---

## The Hybrid Part (2/2)

- Strategies:
  - **Linear Combination**: `Score = (alpha * VectorScore) + ((1-alpha) * KeywordScore)`
  - **Reciprocal Rank Fusion**: Based on rank position.

---

## Reciprocal Rank Fusion (RRF) (1/2)

- Why RRF?
  - Vector scores might be `0.8, 0.79...`
  - Keyword scores might be `15.5, 12.2...` (BM25 is unbounded).
  - Adding them directly is hard (`0.8 + 15.5` is dominated by keyword).

---

## Reciprocal Rank Fusion (RRF) (2/2)

- RRF ignores the score value. It uses the RANK.
- `Score = 1 / (k + rank)`
- If Item A is #1 in Vector and #1 in Keyword -> Huge score.
- Balances both worlds perfectly without tuning math.

---

## Summary of Similarity

- Use **Cosine Similarity** for text.
- Use **ANN (HNSW)** for speed.
- Use **RRF** to combine Vector + Keyword results cleanly.

---

## Next Up

- Theory is done!
- Time to code.
- **Building the Recommendation App**.
