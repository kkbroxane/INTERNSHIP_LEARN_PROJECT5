from AI_Chatbot.settings import (
    LLAMA_GENERATION_MODEL, LLAMA_EMBEDDING_MODEL,
    LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL,
    SYSTEM_PROMPT
)
from .models import ChatMessage
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
        try:
            return json.loads(text)
        except Exception:
            return text
            # raise ValueError("No JSON code block found in the input text.")
    
    json_data = match.group(1).strip()
    return json.loads(json_data)

def build_context(message, properties=None):
    history = ChatMessage.objects.order_by('-timestamp')[:5][::-1]

    messages = [SYSTEM_PROMPT]
    if properties:
        messages.append({
            "role": "system",
            "content": (
                f"Vous disposez des résultats suivants en réponse à la demande de l'utilisateur : {properties}. "
                "Veuillez répondre de façon polie et professionnelle."
            )
        })

    for exchange in history:
        print("\n==============Hello=================")
        print(f"user: {exchange.user_message}\nbot: {exchange.bot_response}")
        print("===============================\n")

        messages.append({'role': 'user', 'content': exchange.user_message})
        messages.append({'role': 'assistant', 'content': exchange.bot_response})

    messages.append({'role': 'user', 'content': message})
    return messages

def generate_content(message):
    messages = build_context(message)

    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": messages,
        "stream": False
    }

    print("\n\n=========sending...============\n")
    print(messages)
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

    messages = build_context(message, properties)

    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(LLAMA_GENERATION_URL, json=payload)
    data = response.json()["message"]["content"]

    print("\n\n=======(answer_from_db)========\n")
    print("DATA RESPONSE:")
    print(data)
    print("\n===============================\n\n")
    data_json = extract_json_dict(data)

    if isinstance(data_json, str):
        return data_json
    return data_json.get("answer")
