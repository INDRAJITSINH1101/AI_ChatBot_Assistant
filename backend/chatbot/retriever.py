from .embeddings import embed
from .vector_store import collection

def search(query):
    vec = embed(query)
    result = collection.query(query_embeddings=[vec], n_results=5)
    if not result["documents"] or not result["documents"][0]:
        return ""

    return " ".join(result["documents"][0])