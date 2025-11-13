from django.urls import path
from .views import send_message, list_messages, is_reloaded, send_message_agent, send_agent_stream

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('send_agent/', send_message_agent, name='send_agent'),
    path('send_agent_stream/', send_agent_stream, name='send_agent_stream'),
    path('list_messages/', list_messages, name='list_messages'),
    path("is_reloaded/", is_reloaded, name="is_reloaded"),
]
