---
marp: true
paginate: true
theme: default
---

<!-- markdownlint-disable-file MD029 MD036 MD026 -->

# Chunking Fundamentals

## Preparing Text for Logic

---

## What is Chunking? (1/2)

- **Definition**: Breaking down large texts into smaller, manageable pieces (chunks).
- **Analogy**: You don't eat a whole steak in one bite; you cut it into pieces.
- **In AI**: LLMs and Embedding models have limits (Context Window).

---

## What is Chunking? (2/2)

- **Why is it critical for RAG/Search?**
  1. **Context Window Constraint**: Models can't process infinite text.
  2. **Retrieval Precision**:
  - Searching a whole book gives a vague vector.
  - Searching a *paragraph* gives a precise vector.

---

## The "Goldilocks" Problem (1/3)

- **Chunk too small**:
  - "The cat sat."
  - Lacks context. Why did it sit? Where?
  - Vector might match anything related to generic cats/sitting.

---

## The "Goldilocks" Problem (2/3)

- **Chunk too big**:
  - A whole chapter containing topics A, B, C, D, and E.
  - Vector becomes a "blur" of all these topics.
  - Search for "Topic A" might not rank this big chunk highly because
    B, C, D dilute it.

---

## The "Goldilocks" Problem (3/3)

- **Just right**:
  - A paragraph or logical section.
  - "The black cat sat on the mat because it was cold outside."
  - Contains subject, action, and detailed context.

---

## Chunking Strategies (1/4)

1. **Fixed-Size Chunking**:
    - Split every `X` characters or tokens.
    - Simple and fast.
    - **Risk**: Can cut sentences in half!
    - Example: `[0-100]`, `[100-200]`...

---

## Chunking Strategies (2/4)

2. **Recursive Character Chunking**:
    - Smart splitting.
    - Tries to split by paragraph `\n\n`.
    - If too big, tries sentence `\n`.
    - If too big, tries space ` `.
    - Preserves semantic meaning better.

---

## Chunking Strategies (3/4)

3. **Semantic Chunking**:
    - Uses embeddings to find break points.
    - Measures similarity between sentences.
    - If similarity drops (topic change), start a new chunk.
    - More expensive (needs model calls) but high quality.

---

## Chunking Strategies (4/4)

- **Which one will we use?**
- **Recursive Character Chunking**.
- Good balance of performace and quality for a workshop.

---

## Visualizing Overlap (1/2)

- **Overlap**: Including the end of Chunk A at the start of Chunk B.
- **Why?**: To prevent cutting context at the boundary.
- **Example**:
  - Chunk 1: "...the secret code is 1234."
  - Chunk 2: "Don't tell anyone..."
- Without overlap, the connection between "code" and "don't tell" breaks.

---

## Visualizing Overlap (2/2)

- **With Overlap**:
  - Chunk 1: "...the secret code is 1234. Don't"
  - Chunk 2: "code is 1234. Don't tell anyone..."
- Keeps the "bridge" between concepts intact.

---

## LangChain to the Rescue (1/3)

- LangChain provides built-in splitters.
- `RecursiveCharacterTextSplitter`.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = "Long document text..."

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

---

## LangChain to the Rescue (2/3)

- **Parameters**:
  - `chunk_size`: Targeted size (characters).
  - `chunk_overlap`: How many chars to repeat.
  - `separators`: Defaults to `["\n\n", "\n", " ", ""]`.

---

## LangChain to the Rescue (3/3)

- **Splitting the text**:

```python
docs = splitter.create_documents([text])

print(len(docs)) # Number of chunks
print(docs[0].page_content) # Content of first chunk
```

---

## Impact on Embeddings (1/2)

- Remember: **Garbage In, Garbage Out**.
- Bad chunks = Bad Vectors.
- If a chunk cuts off midway, the vector representation is incomplete.

---

## Impact on Embeddings (2/2)

- **Recommendation**:
  - For search/retrieval: 256 - 512 tokens is often a sweet spot.
  - For summarization: Larger chunks (1000+) are okay.
- We will use ~500 characters for our product descriptions.

---

## Practical Exercise (Mental Check)

- If you have a 10,000 character document.
- `chunk_size` = 1000.
- `chunk_overlap` = 0.
- How many chunks? -> 10.

- If `chunk_overlap` = 100? -> ~11 chunks. (Slight increase due to repetition).

---

## Summary of Chunking

- It's the foundation of retrieval.
- Use **Recursive** splitting for text.
- Always use **Overlap** to preserve edges.
- Size matters: Match it to your embedding model's sweet spot.

---

## Next Up

- We have our chunks.
- Now we need to turn them into math.
- **Embedding Generation with VoyageAI**.
