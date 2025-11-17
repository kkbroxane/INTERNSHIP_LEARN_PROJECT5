from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from .models import ChatMessage
from .utils import generate_content, answer_from_db
from .views_ai import search_properties
from .agent import Agent
import json

def is_reloaded(request):
    ChatMessage.objects.all().delete()
    return HttpResponse(status=204)

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })

def send_message_agent(request):

    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        agent = Agent(top_k=3)
        result = agent.run(user_message)
        return JsonResponse({'message': user_message, 'response': result['answer'], 'trace': result['trace']})
    return redirect('list_messages')
