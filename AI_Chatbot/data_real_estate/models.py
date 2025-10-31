from django.db import models
from django.core.validators import MinValueValidator
from pgvector.django import VectorField
from chatbot.views_rag import embed_content

TRANSACTION_TYPES = [
    ('location', 'location'),
    ('achat', 'achat')
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
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=100)
    surface_area = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="L'aire de la surface (en m²) doit être strictement supérieure à 0."
    )
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le prix d'un bien doit être strictement supérieur à 0."
    )
    embedding = VectorField(dimensions=4096, null=True, blank=True)

    def get_child_instance(self):
        for child in ('logement', 'professionel', 'terrain'):
            if hasattr(self, child):
                return getattr(self, child)
        return self

    def generate_embedding_for_property(self):
        property_instance = self.get_child_instance()
        type_info = property_instance.type_info()

        embedding_vector = embed_content(type_info)
        self.embedding = embedding_vector
        self.save()

"""
class PropertyImage(models.Model):
    image = models.ImageField(upload_to='')
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )
"""

class Logement(Property):
    nb_bedrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de chambres doit être strictement supérieur à 0."
    )
    nb_bathrooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de douches doit être strictement supérieur à 0."
    )
    has_parking = models.BooleanField()
    is_furnished = models.BooleanField()

    def type_info(self):
        article = "Une" if self.property_type != "appartement" else "Un"
        type_info = (
            f"{article} {self.property_type} d'une superficie de {self.surface_area} m² "
            f"avec {self.nb_bedrooms} chambres et {self.nb_bathrooms} douches, "
            f"situé à {self.location}, pour un prix de {self.price} FCFA en {self.transaction_type}."
        )

        if self.has_parking:
            type_info += " Parking disponible."
        if self.is_furnished:
            type_info += " Meublée." if self.property_type != "appartement" else " Meublé."
        else:
            type_info += " Non meublée." if self.property_type != "appartement" else " Non meublé."
        
        return type_info


class Professionel(Property):
    nb_rooms = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le nombre de pièces doit être strictement supérieur à 0."
    )
    nb_bathrooms = models.PositiveSmallIntegerField()
    is_furnished = models.BooleanField()

    def type_info(self):
        article = "Une" if self.property_type == "boutique" else "Un"
        type_info = (
            f"{article} {self.property_type} d'une superficie de {self.surface_area} m² "
            f"avec {self.nb_rooms} salles et {self.nb_bathrooms} douches, "
            f"situé à {self.location} pour un prix de {self.price} FCFA en {self.transaction_type}."
        )

        if self.is_furnished:
            type_info += " Meublée." if self.property_type != "appartement" else " Meublé."
        else:
            type_info += " Non meublée." if self.property_type != "appartement" else " Non meublé."

        return type_info


class Terrain(Property):

    def type_info(self):
        type_info = (
            f"Un {self.property_type} avec une superficie de {self.surface_area} m² "
            f"situé à {self.location} pour un prix de {self.price} FCFA en {self.transaction_type}."
        )
        return type_info

# from data_real_estate.models import *
# Property.objects.all()

# property1 = Logement.objects.create(transaction_type="location", property_type="maison", location="Cotonou, Cadjèhoun", price=1000000, nb_bedrooms=5, nb_bathrooms=3, surface_area=800, has_parking=True, is_furnished=True)
# property2 = Logement.objects.create(transaction_type="location", property_type="appartement", location="Cotonou, Fidjrossè", price=500000, nb_bedrooms=3, nb_bathrooms=3, surface_area=200, has_parking=True, is_furnished=False)
# property3 = Logement.objects.create(transaction_type="location", property_type="maison", location="Cotonou, Cocotiers", price=800000, nb_bedrooms=5, nb_bathrooms=5, surface_area=800, has_parking=True, is_furnished=True)
# property4 = Professionel.objects.create(transaction_type="location", property_type="bureau", location="Cotonou, Gbégamey", price=100000, nb_rooms=4, nb_bathrooms=3, surface_area=150, is_furnished=True)
# property5 = Professionel.objects.create(transaction_type="location", property_type="boutique", location="Cotonou, Jéricho", price=50000, nb_rooms=2, nb_bathrooms=1, surface_area=75, is_furnished=False)
# property6 = Logement.objects.create(transaction_type="location", property_type="villa", location="Cotonou, Fidjrossè", price=1500000, nb_bedrooms=5, nb_bathrooms=5, surface_area=700, has_parking=True, is_furnished=True)
# property7 = Logement.objects.create(transaction_type="location", property_type="appartement", location="Cotonou, Patte d'oie", price=600000, nb_bedrooms=4, nb_bathrooms=3, surface_area=250, has_parking=True, is_furnished=False)
# property8 = Terrain.objects.create(transaction_type="achat", property_type="terrain", location="Calavi Agori", price=250000000, surface_area=1000)