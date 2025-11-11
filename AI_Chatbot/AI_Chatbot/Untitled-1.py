{
    "relevance": "pertinent" | "non pertinent",
    "db_match": true | false,
    "property_type": "maison" | "villa" | "appartement" | "boutique" | "bureau" | "terrain" | null,
    "answer": "Réponse finale ici."
}

#########################################################################################


import requests
import json

SYSTEM_PROMPT = """YOUR FULL SYSTEM PROMPT HERE"""

def ask_llama(message):
    payload = {
        "model": "llama3.2:latest",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    }

    res = requests.post("http://localhost:11434/api/chat", json=payload, stream=False)
    return res.json()["message"]["content"]

print(ask_llama("Je cherche une maison à louer à Lyon"))

#########################################################################################


def chat_with_properties(user_message, properties_json):
    payload = {
        "model": "llama3.2:latest",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"PROPERTY_DB: {properties_json}"},
            {"role": "user", "content": user_message}
        ]
    }
    res = requests.post("http://localhost:11434/api/chat", json=payload)
    return res.json()["message"]["content"]

#########################################################################################


from django.http import JsonResponse
import json

def my_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        age = data.get("age")
        return JsonResponse({"message": f"Hello {name}, age {age}"})

#########################################################################################


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def my_view(request):
    name = request.data.get("name")  # Already parsed
    return Response({"hello": name})

#########################################################################################


import json

def chatbot_view(request):
    # Suppose you have the chatbot JSON response as a string
    chatbot_response_str = '''
    {
        "relevance": "pertinent",
        "db_match": true,
        "property_type": "maison",
        "answer": "Voici la maison disponible à Casablanca..."
    }
    '''
    # Parse JSON string to Python dict
    chatbot_response = json.loads(chatbot_response_str)

    # Access fields
    relevance = chatbot_response.get('relevance')
    db_match = chatbot_response.get('db_match')
    property_type = chatbot_response.get('property_type')
    answer = chatbot_response.get('answer')

    # Pass data to template or process as needed
    context = {
        'relevance': relevance,
        'db_match': db_match,
        'property_type': property_type,
        'answer': answer,
    }
    return render(request, 'chatbot_result.html', context)


import json
from django.http import JsonResponse

def chatbot_api_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        relevance = data.get('relevance')
        db_match = data.get('db_match')
        property_type = data.get('property_type')
        answer = data.get('answer')

        # Do something with data...

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
