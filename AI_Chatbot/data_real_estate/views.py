from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Property

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'main/all_page.html', {'properties': properties})

def property_detail(request, p_id):
    property = get_object_or_404(Property, pk=p_id)
    return render(request, 'main/property_detail.html', {'property': property}) 

def property_form(request):
    if request.method == "POST":
        transaction_type = request.POST.get('transaction_type')
        property_type = request.POST.get('property_type')        
        price = request.POST.get('price')
        location = request.POST.get('location')
        description = request.POST.get('description')

        property = Property.objects.create(
            transaction_type=transaction_type,
            property_type=property_type,
            price=price,
            location=location,
            description=description,
        )
        property.generate_embedding_for_property()
        return redirect('property_detail', p_id=property.id)
    return render(request, 'form/property_form.html')
