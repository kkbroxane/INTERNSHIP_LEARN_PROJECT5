from AI_Chatbot.settings import LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL
import requests
import json

MISSION = (
    "Aider à trouver un bien (maison, villa, appartement, boutique, bureau, terrain) uniquement\n"
)

def embed_content(text):
    response = requests.post(
        url=LLAMA_EMBEDDING_URL,
        json={"model": "llama3.2:latest", "prompt": text}
    )
    embedding = response.json()["embedding"]
    return embedding

def is_question_of_type(message: str) -> str:
    classifier_prompt = f"""
        Tu es un classifieur. Tu dois répondre UNIQUEMENT par l'un des 3 mots suivants :

        - "salutation" -> si le message est une salutation (bonjour, salut, hey, coucou, etc.)
        - "oui" -> si la question a rapport avec cette mission: {MISSION}
        - "non" -> si ça ne concerne ni l'immobilier ni une salutation

        Message : "{message}"
    """
    print("\n\n*****question_of_type*****\n")
    print("IS IN CLASSF")
    print("\n**************************\n\n")

    result = generate_content(classifier_prompt).strip().lower()
    return result

def generate_content(prompt):
    url = LLAMA_GENERATION_URL
    data = {'model': 'llama3.2:latest', 'prompt': prompt}
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
