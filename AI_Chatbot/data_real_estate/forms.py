from django import forms

class BasePropertyForm(forms.Form):
    TRANSACTION_CHOICES = [
        ('location', 'Location'),
        ('achat', 'Achat'),
    ]

    PROPERTY_CHOICES = [
        ('maison', 'Maison'),
        ('villa', 'Villa'),
        ('appartement', 'Appartement'),
        ('bureau', 'Bureau'),
        ('boutique', 'Boutique'),
        ('terrain', 'Terrain'),
    ]

    transaction_type = forms.ChoiceField(
        choices=TRANSACTION_CHOICES, 
        label="Type de transaction", 
        required=True
    )
    property_type = forms.ChoiceField(
        choices=PROPERTY_CHOICES, 
        label="Type de bien", 
        required=True
    )
    location = forms.CharField(
        max_length=100, 
        label="Localisation", 
        required=True
    )
    surface_area = forms.IntegerField(
        min_value=1, 
        label="Surface (en m²)", 
        required=True,
        error_messages={'min_value': "La surface doit être strictement supérieure à 0."}
    )
    price = forms.DecimalField(
        min_value=1, 
        label="Prix (FCFA)", 
        required=True,
        error_messages={'min_value': "Le prix doit être strictement supérieur à 0."}
    )


class LogementForm(forms.Form):
    nb_bedrooms = forms.IntegerField(
        min_value=1, 
        label="Nombre de chambres", 
        required=True,
        error_messages={'min_value': "Le nombre de chambres doit être strictement supérieur à 0."}
    )
    nb_bathrooms = forms.IntegerField(
        min_value=1, 
        label="Nombre de douches", 
        required=True,
        error_messages={'min_value': "Le nombre de douches doit être strictement supérieur à 0."}
    )
    has_parking = forms.BooleanField(
        label="Parking disponible",
        required=True
    )
    is_furnished = forms.BooleanField(
        label="Meublé",
        required=True
    )


class ProfessionelForm(forms.Form):
    nb_rooms = forms.IntegerField(
        min_value=1, 
        label="Nombre de pièces", 
        required=True,
        error_messages={'min_value': "Le nombre de pièces doit être strictement supérieur à 0."}
    )
    nb_bathrooms = forms.IntegerField(
        min_value=1, 
        label="Nombre de douches", 
        required=True,
        error_messages={'min_value': "Le nombre de douches doit être strictement supérieur à 0."}
    )
    is_furnished = forms.BooleanField(
        label="Meublé",
        required=True
    )
