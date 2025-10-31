from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *

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
    return render(request, '', {'properties': properties})

def property_detail(request, p_id):
    property = get_object_or_404(Property, pk=p_id)
    property = property.get_child_instance()
    return render(request, '', {'property': property}) 

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
            return logement_form(base_info)
        elif property_type in PROFESSIONEL_TYPES:
            return professionel_form(base_info)
        else:
            return terrain_form(base_info)
    return render(request, 'professionel_form.html')

def logement_form(request, base_info):
    if request.method == 'POST':
        nb_bedrooms = request.POST.get('nb_bedrooms')
        nb_bathrooms = request.POST.get('nb_bathrooms')
        has_parking = request.POST.get('has_parking')
        is_furnished = request.POST.get('is_furnished')

        logement = Logement.objects.create(
            transaction_type = base_info['transaction_type'],
            property_type = base_info['property_type'],
            location = base_info['location'],
            surface_area = base_info['surface_area'],
            price = base_info['price'],
            nb_bedrooms = nb_bedrooms,
            nb_bathrooms = nb_bathrooms,
            has_parking = convert_to_boolean(has_parking),
            is_furnished = convert_to_boolean(is_furnished)
        )
        logement.get_property_embedding()
        return redirect('properties_list')
    return render(request, 'logement_form.html')

def professionel_form(request, base_info):
    if request.method == 'POST':
        nb_rooms = request.POST.get('rooms')
        nb_bathrooms = request.POST.get('nb_bathrooms')
        is_furnished = request.POST.get('is_furnished')

        professionel = Professionel.objects.create(
            transaction_type = base_info['transaction_type'],
            property_type = base_info['property_type'],
            location = base_info['location'],
            surface_area = base_info['surface_area'],
            price = base_info['price'],
            nb_rooms = nb_rooms,
            nb_bathrooms = nb_bathrooms,
            is_furnished = convert_to_boolean(is_furnished)
        )
        professionel.get_property_embedding()
        return redirect('properties_list')
    return render(request, 'professionel_form.html')

def terrain_form(base_info):
    terrain = Terrain.objects.create(
        transaction_type = base_info['transaction_type'],
        property_type = base_info['property_type'],
        location = base_info['location'],
        surface_area = base_info['surface_area'],
        price = base_info['price'],
    )
    terrain.get_property_embedding()
    return redirect('properties_list')
