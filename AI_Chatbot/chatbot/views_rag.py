from AI_Chatbot.settings import LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL
import requests
import json

def get_property_type(user_query):
    q = user_query.lower()
    for word in PROPERTY_KEYWORDS:
        if word in q:
            return word
    return None
    
def search_properties(user_query, type, top_k=5):
    query_embedding = embed_content(user_query)

    matching_properties = Property.objects.filter(property_type=type).exclude(embedding=None)

    results = matching_properties.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:top_k]

    return results

def embed_content(text):
    response = requests.post(
        url=LLAMA_EMBEDDING_URL,
        json={"model": "llama3", "prompt": text}
    )
    embedding = response.json()["embedding"]
    return embedding

def is_question_of_type(message: str) -> str:
    classifier_prompt = f"""
        Tu es un classifieur. Tu dois répondre UNIQUEMENT par l'un des 3 mots suivants :

        - "salutation" -> si le message est une salutation (bonjour, salut, hey, coucou, etc.)
        - "oui" -> si la question concerne l'immobilier (logement, terrain, location, achat, etc.)
        - "non" -> si ça ne concerne ni l'immobilier ni une salutation

        Message : "{message}"
    """

    result = generate_content(classifier_prompt).strip().lower()
    return result

def generate_content(prompt):
    url = LLAMA_GENERATION_URL
    data = {'model': 'llama3', 'prompt': prompt}
    response = requests.post(url, json=data, stream=True)

    full_text = ""
    for line in response.iter_lines():
        if not line.strip():
            continue

        line = line.decode("utf-8")
        if line.startswith("data: "):
            line = line[len("data: "):]

        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict) and "response" in parsed:
                full_text += parsed["response"]
        except json.JSONDecodeError:
            continue

    return full_text
