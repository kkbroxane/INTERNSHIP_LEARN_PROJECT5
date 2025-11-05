from django.contrib import admin
from django.urls import path
from .views import send_message, list_messages, clear_current_chat, is_reloaded

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('list_messages/', list_messages, name='list_messages'),
    path("is_reloaded/", is_reloaded, name="is_reloaded"),
    path('clear_chat/', clear_current_chat, name='clear_chat'),
]