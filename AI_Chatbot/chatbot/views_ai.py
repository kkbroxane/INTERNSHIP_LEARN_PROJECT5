from pgvector.django import CosineDistance
from data_real_estate.models import Property
from .utils import embed_content

def search_properties(user_query, type, top_k=5):
    if not type:
        return None

    query_embedding = embed_content(user_query)

    matching_properties = Property.objects.filter(property_type=type).exclude(embedding=None)
    results = matching_properties.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:top_k]

    properties = "\n\n".join(
        p.get_child_instance().type_info() for p in results
    )
    return properties
