from AI_Chatbot.settings import LLAMA_GENERATION_MODEL, LLAMA_EMBEDDING_MODEL, LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL, SYSTEM_PROMPT
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

    print("\n\n==============Hello=================\n")
    print(json_data)
    print("\n===============================\n\n")

    return json.loads(json_data)
    
def generate_content(message):
    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},

            {"role": "user", "content": "Bonjour !"},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "non pertinent",
                    "property_type": null,
                    "answer": "Bonjour ! Comment puis-je vous aider dans vos recherches immobilières aujourd’hui ?"
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "Je cherche un hôtel à Cotonou."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "pertinent",
                    "property_type": null,
                    "answer": "Désolé, ce type de bien n’est pas pris en charge. Je peux uniquement vous aider à trouver une maison, une villa, un appartement, une boutique, un bureau ou un terrain."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "Je cherche une maison."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "pertinent",
                    "property_type": "maison",
                    "answer": "Bien sûr ! Nous avons une maison disponible qui pourrait correspondre à votre recherche. Elle fait 250 m², est située à Cotonou, et dispose de 3 chambres et de 3 douches. Le prix demandé est de 800000 FCFA en location. Pour mieux vous accompagner, pourriez-vous me préciser vos critères principaux ? Par exemple, le nombre de chambres ou de douches souhaité, le budget etc."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "Aide moi à résoudre un problème mathématique."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "non pertinent",
                    "property_type": null,
                    "answer": "Je suis uniquement autorisé à répondre à des questions liées à l’immobilier."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "J’ai une base Excel de maisons à exploiter sur un serveur Ubuntu avec Python et openpyxl."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "non pertinent",
                    "property_type": null,
                    "answer": "Je suis uniquement autorisé à répondre à des questions liées à l’immobilier."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": message}
        ],
        "stream": False
    }

    print("\n\n===============================\n")
    print("Sending payload to Ollama...")
    print("\n===============================\n\n")

    response = requests.post(LLAMA_GENERATION_URL, json=payload)

    print("\n\n===============================\n")
    print("RAW RESPONSE:")
    print(response.text)
    print("\n===============================\n\n")
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


    payload = {
        "model": LLAMA_GENERATION_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"Voici des informations utiles pour répondre à l'utilisateur: {properties}"},

            {"role": "user", "content": "Je cherche un hôtel à Cotonou."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "pertinent",
                    "property_type": null,
                    "answer": "Désolé, ce type de bien n’est pas pris en charge. Je peux uniquement vous aider à trouver une maison, une villa, un appartement, une boutique, un bureau ou un terrain."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "Je cherche une maison."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "pertinent",
                    "property_type": "maison",
                    "answer": "Bien sûr ! Nous avons une maison disponible qui pourrait correspondre à votre recherche. Elle fait 250 m², est située à Cotonou, et dispose de 3 chambres et de 3 douches. Le prix demandé est de 800000 FCFA en location. Pour mieux vous accompagner, pourriez-vous me préciser vos critères principaux ? Par exemple, le nombre de chambres ou de douches souhaité, le budget etc."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "Aide moi à résoudre un problème mathématique."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "non pertinent",
                    "property_type": null,
                    "answer": "Je suis uniquement autorisé à répondre à des questions liées à l’immobilier."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": "J’ai une base Excel de maisons à exploiter sur un serveur Ubuntu avec Python et openpyxl."},
            {"role": "assistant", "content": textwrap.dedent("""
                ```
                {
                    "relevance": "non pertinent",
                    "property_type": null,
                    "answer": "Je suis uniquement autorisé à répondre à des questions liées à l’immobilier."
                }
                ```
                """).strip()
            },

            {"role": "user", "content": message}
        ],
        "stream": False
    }

    response = requests.post(LLAMA_GENERATION_URL, json=payload)

    print("\n\n===========(answer_from_db)====================\n")
    print("RAW RESPONSE:")
    print(response.text)
    print("\n===============================\n\n")
    data = response.json()["message"]["content"]

    print("\n\n===============================\n")
    print("DATA RESPONSE:")
    print(data)
    print("\n===============================\n\n")

    return extract_json_dict(data)["answer"]

