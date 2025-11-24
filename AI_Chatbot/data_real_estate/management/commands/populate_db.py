from django.core.management.base import BaseCommand
from data_real_estate.models import Property

class Command(BaseCommand):
    help = "Insère 20 biens immobiliers fictifs dans la base de données, avec localisation et descriptions améliorées."

    def handle(self, *args, **kwargs):
        properties_data = [

            # === APPARTEMENT (22) ===
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 150000,
                "description": "Appartement lumineux avec 2 chambres, 2 douches, 1 salon spacieux, parking sécurisé.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 29000000,
                "description": "Appartement avec 2 chambres, 2 douches, salon, balcon et parking.",
                "location": "Cotonou"
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
                "property_type": "appartement",
                "price": 85000,
                "description": "Studio équipé avec 1 chambre, douche et kitchenette.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 32000000,
                "description": "Appartement avec 3 chambres, 2 douches, salon lumineux, cuisine équipée.",
                "location": "PK10"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 28000000,
                "description": "Appartement moderne avec 2 chambres, 2 douches, salon et balcon, parking sécurisé.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 55000000,
                "description": "Appartement haut standing avec 3 chambres, 3 douches et cuisine équipée.",
                "location": "Jardin de l’Océan"
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
                "property_type": "appartement",
                "price": 90000,
                "description": "Studio fonctionnel avec 1 chambre, douche et kitchenette équipée.",
                "location": "Missèbo"
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
                "property_type": "appartement",
                "price": 90000,
                "description": "Studio équipé avec 1 chambre, douche, kitchenette.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 56000000,
                "description": "Appartement haut standing avec 3 chambres, 3 douches, cuisine équipée.",
                "location": "Jardin de l’Océan"
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
                "property_type": "appartement",
                "price": 155000,
                "description": "Appartement 2 chambres, balcon, cuisine équipée, proche commerces.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 24000000,
                "description": "Appartement 2 chambres avec parking et garde 24h.",
                "location": "Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 125000,
                "description": "Studio moderne, kitchenette et douche chaude.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 42000000,
                "description": "Appartement 3 pièces, ascenseur, finition haut de gamme.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 175000,
                "description": "Appartement lumineux 2 chambres, eau courante.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 29500000,
                "description": "Appartement moderne proche école et marché.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 98000,
                "description": "Studio sécurisé, entrée indépendante, bonne ventilation.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 36000000,
                "description": "Appartement 3 chambres avec balcon et vue dégagée.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 145000,
                "description": "Appartement 2 chambres, proche transport en commun.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 27000000,
                "description": "Appartement 2 chambres, cuisine ouverte et dressing.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 115000,
                "description": "Petit appartement 1 chambre, idéal pour couple.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 48000000,
                "description": "Appartement haut standing, 3 chambres, parking souterrain.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 132000,
                "description": "Appartement rénové, cuisine équipée, eau chaude solaire.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 22500000,
                "description": "Appartement compact, bon rendement locatif.",
                "location": "Sèmè-Podji"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 168000,
                "description": "Appartement familial 2 chambres, proche écoles.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 33000000,
                "description": "Appartement 3 pièces, finitions contemporaines.",
                "location": "PK3"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 90000,
                "description": "Studio économique, lumineux et propre.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 54000000,
                "description": "Appartement avec grande terrasse, idéal pour famille.",
                "location": "Jardin de l’Océan"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 149000,
                "description": "Appartement moderne, gardiennage et alimentation en eau.",
                "location": "Gbedjromede"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 31000000,
                "description": "Appartement duplex 2 chambres, cuisine américaine.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "location",
                "property_type": "appartement",
                "price": 158000,
                "description": "Appartement neuf au 2ème étage, balcon et parking moto.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "appartement",
                "price": 38500000,
                "description": "Appartement proche plage, 3 chambres et salle de séjour spacieuse.",
                "location": "Fidjrossè Plage"
            },


            # === VILLA (22) ===
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 82000000,
                "description": "Villa 4 chambres, jardin clos et alarme.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 360000,
                "description": "Villa meublée 3 suites, wifi et jardin.",
                "location": "Cotonou"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 125000000,
                "description": "Villa contemporaine avec piscine et pool-house.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 400000,
                "description": "Villa sécurisée avec garage et dépendance.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 95000000,
                "description": "Villa familiale 5 chambres, chaudière solaire.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 290000,
                "description": "Villa coquette 3 chambres, cour arborée.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 76000000,
                "description": "Villa avec annexe locative, jardin aménagé.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 520000,
                "description": "Grande villa 5 chambres disponible à la location longue durée.",
                "location": "Zone Érévan"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 108000000,
                "description": "Villa de prestige, home-cinéma, salle de sport.",
                "location": "Fidjrossè Résidentiel"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 345000,
                "description": "Villa moderne proche centre commercial.",
                "location": "Calavi Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 89000000,
                "description": "Villa 4 chambres avec terrasse et pergola.",
                "location": "Haie-Vive Extension"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 275000,
                "description": "Villa simple 2 chambres, idéale pour expatriés.",
                "location": "Cococodji"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 99500000,
                "description": "Villa moderne, cuisine pro, jardin paysagé.",
                "location": "Gbedjromede"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 410000,
                "description": "Villa familiale avec piscine et abri voiture.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 71000000,
                "description": "Villa trois niveaux, balcon panoramique.",
                "location": "PK3"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 330000,
                "description": "Villa sécurisée avec générateur et fosse septique.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 120000000,
                "description": "Villa haut de gamme, garage 3 voitures et jardin.",
                "location": "Cotonou Sud"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 290000,
                "description": "Villa meublée, service de ménage possible.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 83000000,
                "description": "Villa avec piscine intérieure et spa.",
                "location": "Haie-Vive Prestigieux"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 360000,
                "description": "Villa 4 chambres, proche écoles internationales.",
                "location": "Fidjrossè Nord"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 102500000,
                "description": "Villa contemporaine, finitions luxe, alarme intégrée.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 495000,
                "description": "Villa spacieuse avec dépendance pour personnel.",
                "location": "Zone Érévan"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 80000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé et garage.",
                "location": "Fidjrossè"
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
                "property_type": "villa",
                "price": 450000,
                "description": "Villa moderne avec 4 chambres, 3 douches, salon spacieux et jardin arboré.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 300000,
                "description": "Villa avec 3 chambres, 2 douches, salon spacieux et jardin arboré.",
                "location": "Zone Erevan"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 500000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin et garage.",
                "location": "Haie-Vive"
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
                "property_type": "villa",
                "price": 95000000,
                "description": "Villa luxueuse avec 5 chambres, 4 douches, grand jardin arboré, garage double.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 120000000,
                "description": "Villa de standing avec 5 chambres, 4 douches, grand salon et jardin paysagé.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 90000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "achat",
                "property_type": "villa",
                "price": 92000000,
                "description": "Villa moderne avec 4 chambres, 3 douches, grand salon, jardin clôturé.",
                "location": "Fidjrossè"
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
                "property_type": "villa",
                "price": 470000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin, garage.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "location",
                "property_type": "villa",
                "price": 480000,
                "description": "Villa moderne avec 4 chambres, piscine, jardin, garage.",
                "location": "Haie-Vive"
            },

            # === MAISON (22) ===
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 45000000,
                "description": "Maison familiale avec 3 chambres, 2 douches, salon lumineux, cour cimentée.",
                "location": "Godomey"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 180000,
                "description": "Maison cosy avec 2 chambres, 2 douches, salon et petite terrasse extérieure.",
                "location": "Avotrou"
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
                "property_type": "maison",
                "price": 32000000,
                "description": "Maison avec 2 chambres, 1 douche, salon et cour simple, quartier calme.",
                "location": "Avotrou"
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
                "property_type": "maison",
                "price": 48000000,
                "description": "Maison familiale avec 4 chambres, 3 douches, salon et terrasse.",
                "location": "Godomey"
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
                "property_type": "maison",
                "price": 185000,
                "description": "Maison avec 3 chambres, 2 douches, salon, terrasse et jardin.",
                "location": "Avotrou"
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
                "property_type": "maison",
                "price": 135000,
                "description": "Maison confortable avec 2 chambres, 1 douche, salon et cour.",
                "location": "Godomey"
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
                "property_type": "maison",
                "price": 33000000,
                "description": "Maison avec 3 chambres, 2 douches, salon, cour simple et jardin.",
                "location": "Avotrou"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 28000000,
                "description": "Maison 3 chambres, cour cimentée et abri.",
                "location": "Akassato"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 145000,
                "description": "Maison familiale 2 chambres, véranda et jardin.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 34000000,
                "description": "Maison rénovée, branchements eau et électricité neufs.",
                "location": "Godomey Sud"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 125000,
                "description": "Maison simple 2 chambres, cuisine extérieure.",
                "location": "Missèbo Est"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 46000000,
                "description": "Maison 4 chambres, salon double et terrasse.",
                "location": "Abomey-Calavi Ouest"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 155000,
                "description": "Maison cosy proche marché et transports.",
                "location": "Dantokpa Sud"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 31000000,
                "description": "Maison traditionnelle modernisée, belle cour.",
                "location": "Ouidah"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 175000,
                "description": "Maison 3 chambres, proche écoles et poste.",
                "location": "PK10 Nord"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 25500000,
                "description": "Maison mitoyenne, bonne opportunité d’investissement.",
                "location": "Zogbo"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 138000,
                "description": "Maison meublée avec véranda, loyer tout compris.",
                "location": "Cococodji"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 37500000,
                "description": "Maison avec garage et petite dépendance.",
                "location": "Gbodjè"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 165000,
                "description": "Maison 3 chambres, jardin arrière, accès goudronné.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 29900000,
                "description": "Maison récente, peinture neuve et plomberie refaite.",
                "location": "Ste Cécile"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 142000,
                "description": "Maison de ville 2 chambres, proche station-service.",
                "location": "Ganhi"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 52000000,
                "description": "Maison spacieuse, parfaite pour colocation ou famille.",
                "location": "Porto-Novo Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 185000,
                "description": "Maison avec terrasse et petite annexe pour bureau.",
                "location": "Avotrou Est"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 27000000,
                "description": "Maison économique avec cour constructible.",
                "location": "Hêvié"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 150000,
                "description": "Maison proche services publics et marché central.",
                "location": "Cadjèhoun"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 44500000,
                "description": "Maison 4 chambres avec belle terrasse couverte.",
                "location": "Gbedjromede"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 170000,
                "description": "Maison sécurisée, clôture et portail motorisé.",
                "location": "Aibatin"
            },
            {
                "transaction_type": "achat",
                "property_type": "maison",
                "price": 33000000,
                "description": "Maison bien située, bon accès routier.",
                "location": "Pahou"
            },
            {
                "transaction_type": "location",
                "property_type": "maison",
                "price": 190000,
                "description": "Maison rénovée, placards intégrés et douche italienne.",
                "location": "Zone Érévan Nord"
            },

            # === TERRAIN (22) ===
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 10000000,
                "description": "Terrain plat de 400 m², accessible par route goudronnée, idéal projet résidentiel.",
                "location": "Akpakpa"
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
                "property_type": "terrain",
                "price": 50000,
                "description": "Terrain clôturé, idéal pour atelier, dépôt ou activité commerciale.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 15000000,
                "description": "Terrain de 500 m², plat, borné, proche route principale.",
                "location": "Akpakpa"
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
                "property_type": "terrain",
                "price": 55000,
                "description": "Terrain clôturé, idéal pour atelier ou dépôt commercial.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 16000000,
                "description": "Terrain de 450 m², borné, proche voie principale.",
                "location": "Akpakpa"
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
                "property_type": "terrain",
                "price": 48000,
                "description": "Terrain clôturé, idéal pour atelier ou dépôt commercial.",
                "location": "Yakro"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 15500000,
                "description": "Terrain de 460 m², borné, proche voie principale.",
                "location": "Akpakpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 6000000,
                "description": "Terrain 300 m², borné, proche route, titre foncier en cours.",
                "location": "Kpanroun"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 9500000,
                "description": "Parcelle 400 m², terrain plat et constructible.",
                "location": "Sèmè-Podji Sud"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 4800000,
                "description": "Petit terrain 200 m² pour commerce de proximité.",
                "location": "Missèbo Ouest"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 14000000,
                "description": "Terrain 600 m², proche lotissement résidentiel.",
                "location": "Ouedo"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 22000000,
                "description": "Grand terrain 1000 m², idéal pour projet immobilier.",
                "location": "Cocoteraie Ext."
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 7200000,
                "description": "Terrain 350 m², accès cimenté, borné.",
                "location": "Akpakpa Nord"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 5300000,
                "description": "Parcelle à usage mixte, vente rapide.",
                "location": "Gbégamey"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 16000000,
                "description": "Terrain 500 m², proche route principale et commerces.",
                "location": "Adjarra"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 4200000,
                "description": "Terrain économique pour construction modeste.",
                "location": "Zogbohouè"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 8200000,
                "description": "Terrain 320 m², idéal pour pavillon individuel.",
                "location": "Cotonou Ouest"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 12500000,
                "description": "Terrain plat, borné et clôturable facilement.",
                "location": "Porto-Novo Sud"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 9800000,
                "description": "Parcelle 450 m², possibilité morcellement.",
                "location": "Abomey-Calavi Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 3000000,
                "description": "Petit lot pour dépôt ou garage, bon accès.",
                "location": "Dantokpa Zone"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 17500000,
                "description": "Terrain 700 m², vue dégagée, proche services.",
                "location": "Haie-Vive Sud"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 6400000,
                "description": "Terrain 280 m², non inondable, document administratif OK.",
                "location": "Houéyiho"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 11200000,
                "description": "Parcelle 480 m², bornée, branchements à proximité.",
                "location": "PK10 Est"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 5200000,
                "description": "Terrain artisanal pour atelier ou petite industrie.",
                "location": "Ste Rita"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 8700000,
                "description": "Terrain 360 m², quartier calme et résidentiel.",
                "location": "Gbodjè"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 4300000,
                "description": "Petit terrain pour potager ou stockage.",
                "location": "Yakro Nord"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 20500000,
                "description": "Terrain 1200 m², idéal pour projet multifamilial.",
                "location": "Zone Érévan Sud"
            },
            {
                "transaction_type": "achat",
                "property_type": "terrain",
                "price": 7600000,
                "description": "Parcelle 340 m², accès facile et voisinage construit.",
                "location": "Ganhi Extension"
            },

            # === BUREAU (21) ===
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 250000,
                "description": "Bureau climatisé avec 2 pièces, 1 toilette interne, idéal pour PME.",
                "location": "Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 180000,
                "description": "Bureau fonctionnel avec 1 pièce, toilette interne et climatisation.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 200000,
                "description": "Bureau spacieux avec 3 pièces, climatisation, toilette interne.",
                "location": "Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 160000,
                "description": "Bureau fonctionnel avec 2 pièces, toilettes, climatisation.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 210000,
                "description": "Bureau climatisé avec 3 pièces, toilette interne.",
                "location": "Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 170000,
                "description": "Bureau fonctionnel avec 2 pièces, toilettes, climatisation.",
                "location": "Tokpa Hoho"
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
                "property_type": "bureau",
                "price": 38000000,
                "description": "Immeuble de bureaux avec 4 pièces, 2 toilettes et parking privatif.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 40000000,
                "description": "Immeuble de bureaux avec 5 pièces, 3 toilettes, parking privé.",
                "location": "Porto-Novo"
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
                "property_type": "bureau",
                "price": 195000,
                "description": "Bureau 30 m², climatisé, toilettes partagées.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 28000000,
                "description": "Local bureau 60 m², parking et sécurité.",
                "location": "Calavi Business"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 220000,
                "description": "Open-space avec plusieurs postes, fibre disponible.",
                "location": "PK10"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 45000000,
                "description": "Immeuble de bureaux sur 3 étages, ascenseur.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 130000,
                "description": "Bureau indépendant 20 m², accès sécurisé.",
                "location": "Godomey"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 34000000,
                "description": "Plateau bureau moderne, open-plan, parking visiteurs.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 205000,
                "description": "Bureau rénové, kitchenette et salle de réunion.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 26000000,
                "description": "Local professionnel au rez-de-chaussée, façade vitrée.",
                "location": "Cocoteraie"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 175000,
                "description": "Bureau avec climatisation et parking moto.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 39000000,
                "description": "Bureaux idéal pour PME, secteur sécurisé.",
                "location": "Calavi Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 240000,
                "description": "Bureau 40 m², sol carrelé et vitrine.",
                "location": "Cotonou Ouest"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 31500000,
                "description": "Bureaux bien situés, bon rapport qualité/prix.",
                "location": "Gbedjromede"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 185000,
                "description": "Bureau partiellement meublé, fibre optique active.",
                "location": "PK3"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 27500000,
                "description": "Local professionnel à usage administratif.",
                "location": "Fidjrossè"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 210000,
                "description": "Bureau lumineux avec kitchenette et sanitaires privés.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 33000000,
                "description": "Bureaux au 1er étage avec accès ascenseur.",
                "location": "Porto-Novo Sud"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 160000,
                "description": "Petit bureau pour consultant ou cabinet.",
                "location": "Haie-Vive Central"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 29000000,
                "description": "Espace bureau divisible selon besoins.",
                "location": "Cotonou Nord"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 200000,
                "description": "Bureau équipé, service de réception inclus.",
                "location": "Dantokpa Business"
            },
            {
                "transaction_type": "achat",
                "property_type": "bureau",
                "price": 37000000,
                "description": "Immeuble bureau récent, good visibility and access.",
                "location": "Godomey East"
            },
            {
                "transaction_type": "location",
                "property_type": "bureau",
                "price": 190000,
                "description": "Bureau 25 m², parking et sécurité 24/7.",
                "location": "Cococodji"
            },

            # === BOUTIQUE (21) ===
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 100000,
                "description": "Boutique avec 1 pièce principale et réserve, parfait pour commerce de proximité.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 12000000,
                "description": "Boutique sécurisée avec grande pièce, volet métallique et compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 70000,
                "description": "Boutique sécurisée avec porte métallique, électricité et point d’eau.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 110000,
                "description": "Boutique avec espace de stockage, porte métallique sécurisée.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 80000,
                "description": "Boutique avec porte métallique, électricité, point d’eau.",
                "location": "Dantokpa"
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
                "property_type": "boutique",
                "price": 13000000,
                "description": "Boutique sécurisée avec grande vitrine, compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 12500000,
                "description": "Boutique sécurisée avec vitrine, compteur électrique.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 75000,
                "description": "Boutique avec porte métallique, électricité, point d’eau.",
                "location": "Dantokpa"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 78000,
                "description": "Boutique 20 m², vitrine et porte métallique.",
                "location": "Dantokpa Marché"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 10500000,
                "description": "Local commercial avec réserve, rue passante.",
                "location": "Cotonou Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 65000,
                "description": "Boutique pour restauration rapide, raccordements OK.",
                "location": "Tokpa Hoho"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 8200000,
                "description": "Boutique 30 m², forte affluence piétonne.",
                "location": "Abomey-Calavi"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 92000,
                "description": "Boutique sécurisée, compteur individuel et point d'eau.",
                "location": "Godomey Centre"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 14000000,
                "description": "Local commercial avec possibilité mezzanine.",
                "location": "Fidjrossè Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 71000,
                "description": "Boutique simple, proche arrêt de bus.",
                "location": "Missèbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 9800000,
                "description": "Boutique avec façade vitrée, bonne visibilité.",
                "location": "PK10"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 83000,
                "description": "Espace commercial adapté à débit alimentaire.",
                "location": "Cococodji"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 12500000,
                "description": "Local commercial bien placé, clientèle régulière.",
                "location": "Dantokpa Hall"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 60000,
                "description": "Boutique petite surface pour commerce de détail.",
                "location": "Zogbo"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 11200000,
                "description": "Boutique et réserve, proche voie principale.",
                "location": "Sèmè-Podji"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 88000,
                "description": "Boutique avec point d’eau et prise électrique.",
                "location": "Haie-Vive"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 9300000,
                "description": "Local commercial prêt à exploiter, bon flux piéton.",
                "location": "Cotonou Ouest"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 77000,
                "description": "Boutique équipée d’un rideau métallique et serrure renforcée.",
                "location": "Porto-Novo"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 8700000,
                "description": "Boutique sur axe principal, adéquat pour franchise.",
                "location": "Calavi Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 72000,
                "description": "Boutique au rez-de-chaussée, sol carrelé.",
                "location": "Gbedjromede"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 9900000,
                "description": "Local commercial avec licence commerciale possible.",
                "location": "Abomey-Calavi Nord"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 68000,
                "description": "Boutique pour commerce artisanal ou vente au détail.",
                "location": "Missèbo Marché"
            },
            {
                "transaction_type": "achat",
                "property_type": "boutique",
                "price": 10300000,
                "description": "Local avec grand flux piéton et visibilité.",
                "location": "Dantokpa Centre"
            },
            {
                "transaction_type": "location",
                "property_type": "boutique",
                "price": 79000,
                "description": "Boutique en zone commerciale, loyer abordable.",
                "location": "PK3"
            }


        ]

        created_count = 0
        for prop_data in properties_data:
            obj = Property.objects.create(**prop_data)
            obj.generate_embedding_for_property()
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✔ {created_count} biens ont été insérés avec succès !"))
