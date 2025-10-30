from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('user_profile/', user_profile, name='user_profile'),
    path('update_profile/', update_profile, name='update_profile'),
]
