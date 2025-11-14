from django.db import models
from django.core.validators import MinValueValidator
from pgvector.django import VectorField
from chatbot.utils import embed_content

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
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Le prix d'un bien doit être strictement supérieur à 0."
    )
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    embedding = VectorField(dimensions=768, null=True, blank=True)

    def type_info(self):
        type_info = (
            f"{self.description} à {self.location}\n"
        )
        return type_info

    def generate_embedding_for_property(self):
        embedding_vector = embed_content(self.type_info())
        self.embedding = embedding_vector
        self.save()
