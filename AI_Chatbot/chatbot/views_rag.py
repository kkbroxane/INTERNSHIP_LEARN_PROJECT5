from django.db.models import F
from pgvector.django import CosineDistance
from data_real_estate.models import *
import numpy

def search_properties(user_query, client, top_k=5):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_query
    )
    query_embedding = numpy.array(response.data[0].embedding)

    results = Property.objects.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:top_k]

    return results
