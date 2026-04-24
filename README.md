## AI Cognitive Routing & RAG Assignment

### Phase 1: Routing
Used FAISS + sentence-transformers to match posts with relevant personas using cosine similarity.

### Phase 2: Content Generation
Simulated LangGraph pipeline:
- Topic selection
- Mock search tool
- Persona-based post generation

### Phase 3: RAG Defense
Used full conversation context to generate replies.
Implemented prompt injection detection to maintain persona consistency.

### Notes
Threshold adjusted based on embedding behavior (MiniLM similarity range ~0.2–0.3).