# AI Cognitive Routing & RAG Assignment

## Overview
This project implements a simplified cognitive AI loop consisting of:
1. Vector-based routing (persona matching)
2. Autonomous content generation (LangGraph-style pipeline)
3. Context-aware defense using RAG with prompt injection handling

---

## Tech Stack
- Python
- FAISS (vector database)
- Sentence Transformers (embeddings)
- LangChain / LangGraph (simulated workflow)
- NumPy

---

## Project Structure

router/ # Persona storage, embeddings, routing logic
agents/ # Content generation pipeline
rag/ # Defense + prompt injection handling
tools/ # Mock search tool
logs/ # Execution logs
main.py # Entry point


---

## Phase 1: Vector-Based Persona Matching

- Personas are embedded using `all-MiniLM-L6-v2`
- Stored in FAISS index (cosine similarity via normalized vectors)
- Incoming post is embedded and compared against persona vectors
- Only personas above a similarity threshold are selected

**Key Design Choice:**
- Threshold set to **0.2** after observing embedding similarity range (~0.25 max)
- This aligns with assignment guidance to tune threshold as needed

---

## Phase 2: Autonomous Content Engine

A simplified LangGraph-style pipeline is implemented:

### Node Flow:
1. **Decide Topic**
   - Determines topic and search query based on persona

2. **Web Search**
   - Calls `mock_searxng_search()` to simulate real-world context

3. **Draft Post**
   - Combines persona + search result
   - Generates an opinionated post (≤ 280 characters)

**Output Format:**
```json
{
  "bot_id": "...",
  "topic": "...",
  "post_content": "..."
}
```
## Phase 3: Combat Engine (RAG + Defense)
**Context Construction:**
- Parent post
- Comment history
- Latest human reply

All are combined to form a structured context for response generation.

**Prompt Injection Defense:**
   
**Detects malicious phrases such as:**
   
"ignore previous instructions"
"you are now"
"apologize"
Rejects the instruction explicitly
Enforces persona consistency
Continues argument logically instead of complying
Execution

**Run the project:**
```
python main.py
```
Example Output

**Phase 1:**
```
A → 0.255
B → 0.109
C → 0.045
```
```
Selected Bots: [('A', 0.2547)]
```
**Phase 2:**
```
{
  "bot_id": "A",
  "topic": "AI developments",
  "post_content": "OpenAI releases model..."
}
```
**Phase 3:**
```
Nice try. I’m not changing roles. Your claim about EV batteries is incorrect...
```
### Notes
- FAISS enables efficient vector similarity search
- Cosine similarity is implemented via normalized embeddings
- Threshold tuning was necessary due to embedding behavior
- Prompt injection handled through rule-based guardrails + persona enforcement
### Conclusion
**This implementation demonstrates:**
- Semantic routing using vector similarity
- Structured content generation pipeline
- Robust handling of adversarial user inputs using RAG + guardrails
