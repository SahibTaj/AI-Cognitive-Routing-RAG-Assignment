from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from router.personas import personas

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def normalize(v):
    return v / np.linalg.norm(v)

# Prepare persona data
persona_texts = list(personas.values())
persona_ids = list(personas.keys())

# Generate embeddings
embeddings = model.encode(persona_texts)
embeddings = np.array([normalize(e) for e in embeddings])

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

# Add embeddings to index
index.add(embeddings)

print("Index size:", index.ntotal)