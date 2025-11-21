from django.contrib import admin
from django.urls import path
from .views import send_message, list_messages, is_reloaded

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('list_messages/', list_messages, name='list_messages'),
    path("is_reloaded/", is_reloaded, name="is_reloaded"),
]
