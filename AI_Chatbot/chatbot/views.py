from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from .agent.agent_builder import build_agent
from .models import ChatMessage
import json
import re

from chatbot.agent.agent_builder import debug_memory


def is_reloaded(request):
    ChatMessage.objects.all().delete()
    return HttpResponse(status=204)

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chatbot.html', {'messages': messages})

def parse_ai_message_content(ai_content: str) -> dict:
    pattern = r"```json\s*(\{.*?\})\s*```"
    match = re.search(pattern, ai_content, re.DOTALL)

    if match:
        json_str = match.group(1)
        return json.loads(json_str)

    return {"answer": ai_content}


agent = build_agent()

def send_message_agent(request):
    if request.method != "POST":
        return redirect('list_messages')


    user_message = request.POST.get("user_message")
    thread_id = request.session.session_key
    if not thread_id:
        request.session.create()
        thread_id = request.session.session_key

    print("\n\n++++++++++++++++++++++++++++++++++++")
    print(f"USER: {user_message}\nsession: {thread_id}")
    print("\n++++++++++++++++++++++++++++++++++++\n\n")

    try:

        response = agent.invoke(
            {"input": user_message},
            config={
                "thread_id": thread_id,
                "configurable": {
                    "thread_id": thread_id
                }
            },
        )
        print("\n\n++++++++++++++++++++++++++++++++++++")
        print(f"AI RESPONSE: {response}")
        print("\n++++++++++++++++++++++++++++++++++++\n\n")

        debug_memory(thread_id)

        ai_message = response['messages'][0]
        ai_content = ai_message.content


        try:
            parsed = parse_ai_message_content(ai_content)
            answer = parsed.get("answer", ai_content)

        except Exception as e:
            print("\n\n+++++++++++++++++++++++++++++++++++\n")
            print(str(response))
            print("\n++++++++++++++++++++++++++++++++++++\n\n")
            answer = f"Error parsing AI response: {e}"

        ChatMessage.objects.create(
            user_message=user_message,
            bot_response=answer
        )

        return JsonResponse({'message': user_message, 'response': answer})

    except Exception as e:
        print(f"\n************** {e} **************\n")
        return JsonResponse({"answer": f"Erreur interne: {e}"}, status=500)
