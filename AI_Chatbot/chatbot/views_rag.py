from AI_Chatbot.settings import LLAMA_GENERATION_URL, LLAMA_EMBEDDING_URL
import requests
import json

def embed_content(text):
    response = requests.post(
        url=LLAMA_EMBEDDING_URL,
        json={"model": "llama3", "prompt": text}
    )
    embedding = response.json()["embedding"]
    
    print("\n\n*********************\nEmbedding length:", len(embedding), "\n\n")

    return embedding

# def generate_content(prompt):
#     url = LLAMA_GENERATION_URL
#     data = {'model': 'llama3', 'prompt': prompt}
#     response = requests.post(url, json=data, stream=True)

#     full_text = ""
#     for line in response.iter_lines(decode_unicode=True):
#         if line:
#             try:
#                 json_data = line.decode("UTF-8")
#                 part = json_data.get("response", "")
#                 full_text += part
#             except json.JSONDecodeError:
#                 continue

#     return full_text



def generate_content(prompt):
    url = LLAMA_GENERATION_URL
    data = {'model': 'llama3', 'prompt': prompt}
    response = requests.post(url, json=data, stream=True)

    full_text = ""
    for line in response.iter_lines():
        if not line.strip():
            continue  # skip empty lines

        # line is bytes, so we decode it
        line = line.decode("utf-8")

        # remove streaming prefix if exists
        if line.startswith("data: "):
            line = line[len("data: "):]

        try:
            parsed = json.loads(line)
            if isinstance(parsed, dict) and "response" in parsed:
                full_text += parsed["response"]
        except json.JSONDecodeError:
            continue

    return full_text
