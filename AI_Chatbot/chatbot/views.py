from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from .models import ChatMessage
from .utils import generate_content, answer_from_db
from .views_ai import search_properties
import json

# Cleanup comments

# ...existing code...
def is_reloaded(request):
    ChatMessage.objects.all().delete()
    return HttpResponse(status=204)

def send_message(request):

    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        data = generate_content(user_message)

        if not data:
            return JsonResponse({"error": "Response generation failed."}, status=500)

        print("\n\n=============send==================\n")
        print("DATA: ")
        print(data)
        print("\n===============================\n\n")

        relevance = data.get("relevance", None)
        property_type = data.get("property_type", None)
        answer = data.get("answer", None)

        if relevance == "non pertinent":
            ChatMessage.objects.create(user_message=user_message, bot_response=answer)
            return JsonResponse({'message': user_message, 'response': answer})

        else:
            matching_properties = search_properties(user_message, property_type, top_k=3)
            new_answer = answer_from_db(user_message, matching_properties)

            print("\n\n=============send==================\n")
            print("new_answer: ")
            print(new_answer)
            print("\n===============================\n\n")

            ChatMessage.objects.create(user_message=user_message, bot_response=new_answer)
            return JsonResponse({'message': user_message, 'response': new_answer})

    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', { 'messages': messages })

# ----------------- New agentic endpoints -----------------
from .agent import Agent

def send_message_agent(request):
    """
    Non-streaming agent endpoint. Reuses Agent.run().
    Persists ChatMessage inside Agent.run as well, but we add a lightweight record here too.
    """
    if request.method == 'POST':
        user_message = request.POST.get('user_message') or request.body.decode()
        agent = Agent(top_k=3)
        result = agent.run(user_message)
        # result contains 'answer', 'trace', 'summary'
        return JsonResponse({'message': user_message, 'response': result['answer'], 'trace': result['trace']})
    return redirect('list_messages')


def send_agent_stream(request):
    """
    SSE streaming endpoint. Returns a StreamingHttpResponse where each line is a JSON chunk.
    The frontend can open an EventSource or fetch and parse lines.
    """
    if request.method != 'POST':
        return redirect('list_messages')

    user_message = request.POST.get('user_message') or request.body.decode()

    agent = Agent(top_k=3)

    def event_stream():
        for chunk in agent.stream_run(user_message):
            # SSE-friendly framing: send a data line per chunk followed by a blank line
            # chunk is already a JSON string; we send it as a data: line
            yield f"data: {chunk}\n\n"

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
# ----------------------------------------------------------