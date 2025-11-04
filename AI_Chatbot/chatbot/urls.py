from django.contrib import admin
from django.urls import path
from .views import send_message, list_messages, clear_current_chat

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('list_messages/', list_messages, name='list_messages'),
    path('clear_chat/', clear_current_chat, name='clear_chat'),
]