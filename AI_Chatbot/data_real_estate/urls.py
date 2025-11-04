from django.urls import path
from .views import PropertyWizard, FORMS
from .views_extra import properties_list, property_detail

urlpatterns = [
    # path('property_form/', property_form, name='property_form'),
    # path('logement_form/', logement_form, name='logement_form'),
    # path('professionel_form/', professionel_form, name='professionel_form'),

    path('add_property/', PropertyWizard.as_view(FORMS), name='add_property'),
    path('properties_list/', properties_list, name='properties_list'),
    path('property_detail/<int:p_id>/', property_detail, name='property_detail'),
]
