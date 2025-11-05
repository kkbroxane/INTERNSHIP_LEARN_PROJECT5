from django.db.models import F
from django.http import JsonResponse, HttpResponse
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

def clear_current_chat(request):
    all_messages = ChatMessage.objects.all()
    all_messages.delete()
    return redirect('list_messages')

def is_reloaded(request):
    ChatMessage.objects.all().delete()
    print("\n\n****  !!!! RELOAD !!!!  ****\n\n")
    return HttpResponse(status=204)


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
    print("\n\n**********send************\n")
    print(request.method)
    print("\n**************************\n\n")

    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        print("\n\n********send***msg********\n")
        print(user_message)
        print("\n**************************\n\n")
        
        query_type = is_question_of_type(user_message)

        print("\n\n********send***qrt********\n")
        print(query_type)
        print("\n**************************\n\n")


        if query_type == "non":
            bot_response = (
                "Je suis un assistant dédié exclusivement à l’immobilier. "
                "Je peux t’aider à trouver un bien, obtenir des informations sur un logement, "
                "le marché immobilier ou les démarches liées à l’achat ou à la location. "
                "N’hésite pas à reformuler ta question dans ce cadre !"
            )
            ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)
            return JsonResponse({'message': user_message, 'response': bot_response})

        elif query_type == "oui":
            property_type = get_property_type(user_message)

            print("\n\n********send***prot********\n")
            print(property_type)
            print("\n**************************\n\n")

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

            else:
                bot_response = (
                    "Je comprends ta demande, mais elle semble incomplète. "
                    "Peux-tu préciser le type de bien que tu recherches (maison, villa, appartement, boutique, bureau, terrain) ?"
                )
        else:
            bot_response = (
                "Bonjour !\n" 
                "En quoi puis-vous aider ?\n"
            )

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)
        return JsonResponse({'message': user_message, 'response': bot_response})

    return redirect('list_messages')


def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })
