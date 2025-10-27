from django.shortcuts import redirect, render
from django.conf import settings
from .models import ChatMessage
import google.generativeai as genai

def send_message(request):
    if request.method == 'POST':
        genai.configure(api_key=settings.GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")

        user_message = request.POST.get('user_message')
        bot_response = model.generate_content(user_message)

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response.text)
    
    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })

def simple_view(request):
    return render(request, 'chatbot.html')

# print("\n\n**********************************\n")

# for m in genai.list_models():
#     print(m.name, m.supported_generation_methods)

# print("\n\n**********************************\n")
