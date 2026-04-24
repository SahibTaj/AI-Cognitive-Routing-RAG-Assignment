from router.vector_store import index, persona_ids, normalize, model
import numpy as np

def match_post_to_personas(post_content: str, threshold: float = 0.2):
    """
    Matches a post to relevant personas using cosine similarity.
    Threshold is low because MiniLM produces lower similarity scores (~0.2–0.3).
    """

    post_embedding = model.encode([post_content])[0]
    post_embedding = normalize(post_embedding)

    D, I = index.search(np.array([post_embedding]), k=3)

    results = []

    for score, idx in zip(D[0], I[0]):
        print(f"{persona_ids[idx]} → {float(score):.3f}")

        if score >= threshold:
            results.append((persona_ids[idx], float(score)))

    return results