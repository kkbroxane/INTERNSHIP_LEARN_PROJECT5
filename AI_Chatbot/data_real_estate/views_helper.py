from django.shortcuts import render, redirect
from .models import Logement, Professionel, Terrain

def logement_create(base_info, extra_info):

    logement = Logement.objects.create(
        transaction_type = base_info['transaction_type'],
        property_type = base_info['property_type'],
        location = base_info['location'],
        surface_area = base_info['surface_area'],
        price = base_info['price'],
        nb_bedrooms = extra_info['nb_bedrooms'],
        nb_bathrooms = extra_info['nb_bathrooms'],
        has_parking = extra_info['has_parking'],
        is_furnished = extra_info['is_furnished']
    )
    logement.get_property_embedding()
    return redirect('properties_list')


def professionel_create(base_info, extra_info):

    professionel = Professionel.objects.create(
        transaction_type = base_info['transaction_type'],
        property_type = base_info['property_type'],
        location = base_info['location'],
        surface_area = base_info['surface_area'],
        price = base_info['price'],
        nb_rooms = extra_info['nb_rooms'],
        nb_bathrooms = extra_info['nb_bathrooms'],
        is_furnished = extra_info['is_furnished']
    )
    professionel.get_property_embedding()
    return redirect('properties_list')


def terrain_create(base_info):

    terrain = Terrain.objects.create(
        transaction_type = base_info['transaction_type'],
        property_type = base_info['property_type'],
        location = base_info['location'],
        surface_area = base_info['surface_area'],
        price = base_info['price'],
    )
    terrain.get_property_embedding()
    return redirect('properties_list')

"""
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
            return logement_form(request, base_info)
        elif property_type in PROFESSIONEL_TYPES:
            return professionel_form(request, base_info)
        elif property_type == 'terrain':
            return terrain_form(base_info)
    return render(request, 'form/property_form.html')

def logement_form(request, base_info):

    if request.method == 'POST':
        nb_bedrooms = request.POST.get('nb_bedrooms')
        nb_bathrooms = request.POST.get('nb_bathrooms')
        has_parking = request.POST.get('has_parking')
        is_furnished = request.POST.get('is_furnished')

        if nb_bedrooms and nb_bathrooms and has_parking and is_furnished:
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
    return render(request, 'form/logement_form.html')

def professionel_form(request, base_info):

    if request.method == 'POST':
        nb_rooms = request.POST.get('nb_rooms')
        nb_bathrooms = request.POST.get('nb_bathrooms')
        is_furnished = request.POST.get('is_furnished')

        if nb_rooms and nb_bathrooms and is_furnished:
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
    return render(request, 'form/professionel_form.html')
"""

    # print("\n\n***********L**********************\n")
    # print(base_info)
    # print("\n*************************************\n\n")
