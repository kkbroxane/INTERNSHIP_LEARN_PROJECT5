from pgvector.django import CosineDistance
from data_real_estate.models import Property
from .utils import embed_content

SIMILARITY_THRESHOLD = 0.6

def format_results(results):
    structured_results = []

    for p in results:
        similarity = 1 - p.distance
        if similarity < SIMILARITY_THRESHOLD:
            print("\n\n=========too low==============\n")
            print(f"{p.type_info()} -- sim: {round(similarity, 4)}")
            print("\n===============================\n\n")
            continue
        structured_results.append({
            "id": p.id,
            "transaction_type": p.transaction_type,
            "property_type": p.property_type,
            "price": p.price,
            "description": p.description,
            "location": p.location,
            "similarity_score": round(similarity, 4),
        })

    return structured_results

def search_properties(user_query, type, top_k=5):
    print("\n\n=========Detected type==============\n")
    print(type)
    print("\n===============================\n\n")

    if not type:
        return None

    query_embedding = embed_content(user_query)

    matching_properties = Property.objects.filter(property_type=type).exclude(embedding=None)
    if not matching_properties.exists():
        return None

    results = matching_properties.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:top_k]

    if not results:
        return None

    return format_results(results)








































"""
def normalize_embedding(embedding):
    emb = np.array(embedding)
    norm = np.linalg.norm(emb)
    if norm == 0:
        return emb  # or handle zero vector edge case
    return emb / norm
"""