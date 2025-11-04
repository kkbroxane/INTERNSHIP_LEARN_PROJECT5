from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .views_helper import *
from .models import Property

LOGEMENT_TYPES = [
    'villa',
    'maison',
    'appartement',
]

PROFESSIONEL_TYPES = [
    'bureau',
    'boutique',
]

def convert_to_boolean(field):
    if field == 'oui':
        return True
    return False

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'main/all_page.html', {'properties': properties})

def property_detail(request, p_id):
    property = get_object_or_404(Property, pk=p_id)
    property = property.get_child_instance()
    return render(request, 'main/property_detail.html', {'property': property}) 

def property_form(request):
    if request.method == 'POST':
        property_type = request.POST.get('property_type')

        base_info = {
            'transaction_type': request.POST.get('transaction_type'),
            'property_type': property_type,
            'location': request.POST.get('location'),
            'surface_area': request.POST.get('surface_area'),
            'price': request.POST.get('price'),
        }

        if property_type in LOGEMENT_TYPES:
            extra_info = logement_form(request)
            return logement_create(base_info, extra_info)

        elif property_type in PROFESSIONEL_TYPES:
            extra_info = professionel_form(request)
            return professionel_create(base_info, extra_info)

        elif property_type == 'terrain':
            return terrain_create(base_info)

    return render(request, 'form/property_form.html')

def logement_form(request):

    if request.method == 'POST':
        extra_info = {
            'nb_bedrooms': request.POST.get('nb_bedrooms'),
            'nb_bathrooms': request.POST.get('nb_bathrooms'),
            'has_parking': convert_to_boolean(request.POST.get('has_parking')),
            'is_furnished': convert_to_boolean(request.POST.get('is_furnished'))
        }
        return extra_info
    return render(request, 'form/logement_form.html')

def professionel_form(request, base_info):

    if request.method == 'POST':
        extra_info = {
            'nb_rooms': request.POST.get('nb_rooms'),
            'nb_bathrooms': request.POST.get('nb_bathrooms'),
            'is_furnished': convert_to_boolean(request.POST.get('is_furnished'))
        }
        return extra_info
    return render(request, 'form/professionel_form.html')
