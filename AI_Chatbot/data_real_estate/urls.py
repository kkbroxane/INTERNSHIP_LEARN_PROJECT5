from django.urls import path
from data_real_estate.views import property_form

urlpatterns = [
    path('property_form/', property_form, name='property_form'),
]
