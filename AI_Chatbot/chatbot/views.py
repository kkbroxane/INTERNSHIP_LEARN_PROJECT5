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
    "bureau",
    "boutique",
    "terrain",
]

OTHER_KEYWORDS = [
    "logement",
    "emplacement",
    "meublé",
    "chambre",
    "douche",
    "FCFA",
    "prix",
]

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

def send_message(request):
    if request.method == 'POST':

        user_message = request.POST.get('user_message')
        property_type = get_property_type(user_message)

        if property_type:
            top_properties = search_properties(user_message, property_type, top_k=3)

            if top_properties:
                properties_text = "\n\n".join(
                    p.get_child_instance().type_info() for p in top_properties
                )

                prompt = (
                    f"L'utilisateur a dit: '{user_message}'.\n"
                    f"Voici les propriétés correspondantes:\n{properties_text}\n"
                    "Réponds de manière naturelle et concise, en te basant sur ces propriétés."
                )
                bot_response = generate_content(prompt)
            else:
                prompt = (
                    f"L'utilisateur a dit: '{user_message}'.\n"
                    f"Mais rien ne correspond à sa recherche.\n"
                    "Réponds: Je n’ai trouvé aucune propriété correspondant à ta recherche.\n"
                    "Tu peux aussi lui demander des détails supplémentaires.\n"
                )
                bot_response = generate_content(prompt)

        # elif (any(word) in user_message for word in OTHER_KEYWORDS):
        #     bot_response = "Pourriez-vous me fournir plus de détails sur ce que vous recherchez ?"
        else:
            # bot_response = (
            #     "Je comprends votre demande, mais je ne dispose pas des connaissances nécessaires pour y répondre correctement. "
            #     "Mon rôle se limite à vous accompagner dans vos recherches immobilières. "
            #     "N’hésitez pas à me poser une autre question dans ce cadre, je serai ravi de vous aider !"
            # )
            bot_response = generate_content(user_message)

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)    
    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })
