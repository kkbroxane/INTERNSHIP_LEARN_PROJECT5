from django.urls import path
from .views import PropertyWizard, FORMS
from .views_extra import properties_list, property_detail

urlpatterns = [
    path('add_property/', PropertyWizard.as_view(FORMS), name='add_property'),
    path('properties_list/', properties_list, name='properties_list'),
    path('property_detail/<int:p_id>/', property_detail, name='property_detail'),
]
