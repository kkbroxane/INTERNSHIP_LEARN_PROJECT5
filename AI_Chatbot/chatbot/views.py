from django.db.models import F
from pgvector.django import CosineDistance
from django.shortcuts import redirect, render
from django.conf import settings
from .models import ChatMessage
from data_real_estate.models import *
from .views_rag import *

PROPERTY_KEYWORDS = [
    "appartement",
    "maison",
    "villa",
    "terrain",
    "bureau",
    "boutique",
    "meublé",
    "chambre",
    "douche",
    "FCFA",
    "prix",
]

def search_properties(user_query, top_k=5):
    query_embedding = embed_content(user_query)

    results = Property.objects.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:top_k]

    print("\n\n*******************\n")
    print(results)
    print("*******************\n\n")
    return results

def send_message(request):
    if request.method == 'POST':

        # genai.configure(api_key=settings.GENERATIVE_AI_KEY)
        # model = genai.GenerativeModel("gemini-2.0-flash")

        user_message = request.POST.get('user_message')

        if any(word in user_message.lower() for word in PROPERTY_KEYWORDS):
            top_properties = search_properties(user_message, top_k=3)

            properties_text = ""
            for p in top_properties:
                p = p.get_child_instance()
                properties_text += f"{p.type_info()}\n\n"

            prompt = (
                f"L'utilisateur a dit: '{user_message}'.\n"
                f"Voici les propriétés correspondantes:\n{properties_text}\n"
                "Réponds de manière naturelle et concise, en te basant sur ces propriétés."
            )
            # bot_response = model.generate_content(prompt)
            bot_response = generate_content(prompt)

        else:
            msg = (
                f"L'utilisateur a dit: '{user_message}'.\n"
                "Ta réponse ne doit pas être en format markdown."
            )
            # bot_response = model.generate_content(msg)
            bot_response = generate_content(msg)

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)    
    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })
