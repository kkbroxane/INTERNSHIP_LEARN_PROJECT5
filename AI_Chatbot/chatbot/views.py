from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from .models import ChatMessage
from .utils import generate_content, answer_from_db
from .views_ai import search_properties
import json

def is_reloaded(request):
    ChatMessage.objects.all().delete()
    return HttpResponse(status=204)

def send_message(request):

    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        data = generate_content(user_message)

        if not data:
            return JsonResponse({"error": "Response generation failed."}, status=500)

        if isinstance(data, str):
            ChatMessage.objects.create(user_message=user_message, bot_response=data)
            return JsonResponse({'message': user_message, 'response': data})

        relevance = data.get("relevance", None)
        property_type = data.get("property_type", None)
        answer = data.get("answer", None)

        if relevance == "non pertinent":
            ChatMessage.objects.create(user_message=user_message, bot_response=answer)
            return JsonResponse({'message': user_message, 'response': answer})

        else:
            matching_properties = search_properties(user_message, property_type, top_k=3)
            new_answer = answer_from_db(user_message, matching_properties)

            ChatMessage.objects.create(user_message=user_message, bot_response=new_answer)
            return JsonResponse({'message': user_message, 'response': new_answer})

    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })
