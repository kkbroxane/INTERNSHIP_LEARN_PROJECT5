from django.urls import path
from .views import list_messages, is_reloaded, send_message_agent

urlpatterns = [
    path("is_reloaded/", is_reloaded, name="is_reloaded"),
    path('list_messages/', list_messages, name='list_messages'),
    path('send_agent/', send_message_agent, name='send_agent'),
]
