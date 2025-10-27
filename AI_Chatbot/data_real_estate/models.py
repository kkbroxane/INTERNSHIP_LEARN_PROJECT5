from django.db import models
from django.core.validators import MinValueValidator

TRANSACTION_TYPES = [
    ('location', 'LOCATION'),
    ('achat', 'ACHAT'),
]

PROPERTY_TYPES = [
    ('maison', 'maison'),
    ('villa', 'villa'),
    ('appartement', 'appartement'),
    ('bureau', 'bureau'),
    ('boutique', 'boutique'),
    ('terrain', 'terrain'),
]

class Property(models.Model):
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=200) # models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le prix d'un bien doit être strictement supérieur à 0."
    )

    class Meta:
        abstract = True

class PropertyImage(models.Model):
    image = models.ImageField(upload_to='')
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )

class Logement(Property):
    nb_bedrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de chambres doit être strictement supérieur à 0."
    )
    nb_bathrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de douches doit être strictement supérieur à 0."
    )
    surface_area = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="L'aire de la surface (en m²) doit être strictement supérieure à 0."
    )
    has_parking = models.BooleanField()
    is_furnished = models.BooleanField()

class Professional(Property):
    nb_bedrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de chambres doit être strictement supérieur à 0."
    )
    nb_bathrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de douches doit être strictement supérieur à 0."
    )
    surface_area = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="L'aire de la surface (en m²) doit être strictement supérieure à 0."
    )
    is_furnished = models.BooleanField()

class Terrain(Property):
    surface_area = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="L'aire de la surface (en m²) doit être strictement supérieure à 0."
    )
