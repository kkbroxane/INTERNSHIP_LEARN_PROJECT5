from AI_Chatbot.settings import LLAMA_GENERATION_MODEL, LLAMA_EMBEDDING_MODEL, LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL, SYSTEM_PROMPT
from chatbot.models import ChatMessage
import textwrap
import requests
import json
import re

def embed_content(message):
    response = requests.post(
        url=LLAMA_EMBEDDING_URL,
        json={"model": LLAMA_EMBEDDING_MODEL, "prompt": message}
    )
    embedding = response.json()["embedding"]
    return embedding

def extract_json_dict(text: str) -> dict:

    pattern = r'^\s*```(?:json)?\n(.*?)\n^\s*```'
    match = re.search(pattern, text, re.DOTALL | re.MULTILINE)
    if not match:
        raise ValueError("No JSON code block found in the input text.")
    json_data = match.group(1).strip()

    return json.loads(json_data)

def build_context(memory_size : int = 7):
    messages = ChatMessage.objects.order_by("-timestamp")
    latest_messages = messages.reverse()[:memory_size]

    context = [{"role": "system", "content": SYSTEM_PROMPT}]

    for m in latest_messages:
        context.append({"role": "user", "content": m.user_message})
        context.append({"role": "assistant", "content": m.bot_response})
    return context

def generate_content(message):
    print("\n\n=========u_query in gen_cont==============\n")
    print(message)
    print("\n===============================\n\n")

    context = build_context()

    context.append({"role": "user", "content": message})

    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": context,
        "stream": False
    }

    print("\n\n===============================\n")
    print("Sending payload to model...")
    print("\n===============================\n\n")

    response = requests.post(LLAMA_GENERATION_URL, json=payload)

    data = response.json()["message"]["content"]

    print("\n\n===============================\n")
    print("DATA RESPONSE:")
    print(data)
    print("\n===============================\n\n")

    return extract_json_dict(data)

def answer_from_db(message, properties):
    if not properties:
        return """
            Désolé, je n'ai rien trouvé qui corresponde à votre demande. 
            Je reste à votre disposition pour toute autre question immobilière.
        """

    print("\n\n===============================\n")
    print("PROPERTIES:")
    print(properties)
    print("\n===============================\n\n")

    context = build_context()
    context.append({"role": "system", "content": f"Voici les propriétés disponibles pour répondre à la demande de l'utilisateur: {properties}"})
    context.append({"role": "user", "content": message})

    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": context,
        "stream": Falsek
    }

    response = requests.post(LLAMA_GENERATION_URL, json=payload)

    data = response.json()["message"]["content"]

    print("\n\n===============================\n")
    print("DATA RESPONSE in an_fr_db:")
    print(data)
    print("\n===============================\n\n")

    return extract_json_dict(data)["answer"]

