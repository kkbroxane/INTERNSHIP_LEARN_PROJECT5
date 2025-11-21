from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
    return render(request, 'main/property_detail.html', {'property': property}) 
