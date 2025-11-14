from django.urls import path
from .views import *

urlpatterns = [
    path('property_form/', property_form, name='property_form'),
    path('properties_list/', properties_list, name='properties_list'),
    path('property_detail/<int:p_id>/', property_detail, name='property_detail'),
]
