from django.core.management.base import BaseCommand
from data_real_estate.models import Property

class Command(BaseCommand):
    help = "Insère 20 biens immobiliers fictifs dans la base de données, avec localisation et descriptions améliorées."

    def handle(self, *args, **kwargs):
        properties_data = [
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 150000,
                "description": "Appartement lumineux avec 2 chambres, 2 douches, 1 salon spacieux, parking sécurisé.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 80000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé et garage.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 250000,
                "description": "Bureau climatisé avec 2 pièces, 1 toilette interne, idéal pour PME.",
                "location": "Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 10000000,
                "description": "Terrain plat de 400 m², accessible par route goudronnée, idéal projet résidentiel.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 100000,
                "description": "Boutique avec 1 pièce principale et réserve, parfait pour commerce de proximité.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 45000000,
                "description": "Maison familiale avec 3 chambres, 2 douches, salon lumineux, cour cimentée.",
                "location": "Godomey"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 450000,
                "description": "Villa moderne avec 4 chambres, 3 douches, salon spacieux et jardin arboré.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 30000000,
                "description": "Appartement confortable avec 3 chambres, 2 douches, salon et cuisine équipée.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 180000,
                "description": "Bureau fonctionnel avec 1 pièce, toilette interne et climatisation.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 12000000,
                "description": "Boutique sécurisée avec grande pièce, volet métallique et compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 7000000,
                "description": "Terrain de 300 m², clôturé, idéal pour construction résidentielle.",
                "location": "Sèmè-Podji"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 90000,
                "description": "Studio fonctionnel avec 1 chambre, douche et kitchenette équipée.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 110000000,
                "description": "Villa luxueuse avec 5 chambres, 4 douches, grand salon et jardin paysagé.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 180000,
                "description": "Maison cosy avec 2 chambres, 2 douches, salon et petite terrasse extérieure.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 38000000,
                "description": "Immeuble de bureaux avec 4 pièces, 2 toilettes et parking privatif.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 70000,
                "description": "Boutique sécurisée avec porte métallique, électricité et point d’eau.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 55000000,
                "description": "Appartement haut standing avec 3 chambres, 3 douches et cuisine équipée.",
                "location": "Jardin de l’Océan"
            },
            {
                "transaction_type": "location",
                "property_type": "terrain",
                "price": 50000,
                "description": "Terrain clôturé, idéal pour atelier, dépôt ou activité commerciale.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 32000000,
                "description": "Maison avec 2 chambres, 1 douche, salon et cour simple, quartier calme.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 300000,
                "description": "Villa avec 3 chambres, 2 douches, salon spacieux et jardin arboré.",
                "location": "Zone Erevan"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 28000000,
                "description": "Appartement moderne avec 2 chambres, 2 douches, salon et balcon, parking sécurisé.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 120000,
                "description": "Maison confortable avec 3 chambres, 2 douches, salon, petite cour.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 95000000,
                "description": "Villa luxueuse avec 5 chambres, 4 douches, grand jardin arboré, garage double.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 200000,
                "description": "Bureau spacieux avec 3 pièces, climatisation, toilette interne.",
                "location": "Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 15000000,
                "description": "Terrain de 500 m², plat, borné, proche route principale.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 110000,
                "description": "Boutique avec espace de stockage, porte métallique sécurisée.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 48000000,
                "description": "Maison familiale avec 4 chambres, 3 douches, salon et terrasse.",
                "location": "Godomey"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 500000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin et garage.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 32000000,
                "description": "Appartement avec 3 chambres, 2 douches, salon lumineux, cuisine équipée.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 160000,
                "description": "Bureau fonctionnel avec 2 pièces, toilettes, climatisation.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 13000000,
                "description": "Boutique sécurisée avec grande vitrine, compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 9000000,
                "description": "Terrain plat de 350 m², borné, idéal pour projet résidentiel.",
                "location": "Sèmè-Podji"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 85000,
                "description": "Studio équipé avec 1 chambre, douche et kitchenette.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 120000000,
                "description": "Villa de standing avec 5 chambres, 4 douches, grand salon et jardin paysagé.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 190000,
                "description": "Maison avec 3 chambres, 2 douches, salon, terrasse et jardin.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 40000000,
                "description": "Immeuble de bureaux avec 5 pièces, 3 toilettes, parking privé.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 80000,
                "description": "Boutique avec porte métallique, électricité, point d’eau.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 58000000,
                "description": "Appartement haut standing avec 3 chambres, 3 douches, cuisine équipée.",
                "location": "Jardin de l’Océan"
            },
            {
                "transaction_type": "location",
                "property_type": "terrain",
                "price": 55000,
                "description": "Terrain clôturé, idéal pour atelier ou dépôt commercial.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 34000000,
                "description": "Maison avec 3 chambres, 2 douches, salon, cour simple et jardin.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 320000,
                "description": "Villa avec 3 chambres, 2 douches, salon spacieux, jardin et garage.",
                "location": "Zone Erevan"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 29000000,
                "description": "Appartement avec 2 chambres, 2 douches, salon, balcon et parking.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 140000,
                "description": "Maison confortable avec 2 chambres, 1 douche, salon et cour.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 90000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 210000,
                "description": "Bureau climatisé avec 3 pièces, toilette interne.",
                "location": "Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 16000000,
                "description": "Terrain de 450 m², borné, proche voie principale.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 115000,
                "description": "Boutique avec espace de stockage, porte sécurisée.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 46000000,
                "description": "Maison avec 4 chambres, 3 douches, salon et terrasse.",
                "location": "Godomey"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 470000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin, garage.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 31000000,
                "description": "Appartement avec 3 chambres, 2 douches, salon lumineux, cuisine équipée.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 170000,
                "description": "Bureau fonctionnel avec 2 pièces, toilettes, climatisation.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 12500000,
                "description": "Boutique sécurisée avec vitrine, compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 9500000,
                "description": "Terrain plat de 380 m², borné, idéal résidentiel.",
                "location": "Sèmè-Podji"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 90000,
                "description": "Studio équipé avec 1 chambre, douche, kitchenette.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 115000000,
                "description": "Villa de standing avec 5 chambres, 4 douches, grand salon, jardin paysagé.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 185000,
                "description": "Maison avec 3 chambres, 2 douches, salon, terrasse et jardin.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 39000000,
                "description": "Immeuble bureaux avec 4 pièces, 2 toilettes, parking.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 75000,
                "description": "Boutique avec porte métallique, électricité, point d’eau.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 56000000,
                "description": "Appartement haut standing avec 3 chambres, 3 douches, cuisine équipée.",
                "location": "Jardin de l’Océan"
            },
            {
                "transaction_type": "location",
                "property_type": "terrain",
                "price": 48000,
                "description": "Terrain clôturé, idéal pour atelier ou dépôt commercial.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 33000000,
                "description": "Maison avec 3 chambres, 2 douches, salon, cour simple et jardin.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 315000,
                "description": "Villa avec 3 chambres, 2 douches, salon spacieux, jardin arboré.",
                "location": "Zone Erevan"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 28500000,
                "description": "Appartement avec 2 chambres, 2 douches, salon, balcon et parking.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 135000,
                "description": "Maison confortable avec 2 chambres, 1 douche, salon et cour.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 92000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 205000,
                "description": "Bureau climatisé avec 3 pièces, toilette interne.",
                "location": "Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 15500000,
                "description": "Terrain de 460 m², borné, proche voie principale.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 118000,
                "description": "Boutique avec espace stockage, porte sécurisée.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 45500000,
                "description": "Maison avec 4 chambres, 3 douches, salon et terrasse.",
                "location": "Godomey"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 480000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin, garage.",
                "location": "Haie-Vive"
            }
        ]

        created_count = 0
        for prop_data in properties_data:
            obj = Property.objects.create(**prop_data)
            obj.generate_embedding_for_property()
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✔ {created_count} biens ont été insérés avec succès !"))
