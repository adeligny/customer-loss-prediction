import pandas as pd
import random

# Génération de données aléatoires
clients = [f'Client_{i}' for i in range(1, 401)]
sinistres = [random.randint(0, 5) for _ in range(400)]
prime = [random.randint(300, 1000) for _ in range(400)]
regimes_alimentaires = ['Végétarien', 'Végétalien', 'Omnivore', 'Pescetarien', 'Flexitarien']
genres = ['Homme', 'Femme', 'Non-binaire']
regions = ['Île-de-France', 'Auvergne-Rhône-Alpes', 'Nouvelle-Aquitaine', 'Occitanie', 'Provence-Alpes-Côte d\'Azur']
fume = [random.choice([True, False]) for _ in range(400)]
enfants = [random.choice([True, False]) for _ in range(400)]
alcool = [random.choice([True, False]) for _ in range(400)]
salaires = [random.randint(20000, 100000) for _ in range(400)]
ages = [random.randint(18, 70) for _ in range(400)]
marques = ['Toyota', 'Renault', 'Peugeot', 'Volkswagen', 'BMW']
carburants = ['Essence', 'Diesel', 'Hybride', 'Électrique']
anciennetes_permis = [random.randint(1, 50) for _ in range(400)]
prix_vehicules = [random.randint(5000, 50000) for _ in range(400)]
types_de_routes = ['Urbain', 'Rural', 'Autoroute']
musique_calme_ou_excitante = ['Calme', 'Excitante']
conduite_de_nuit = [random.choice([True, False]) for _ in range(400)]
utilisation_tel = [random.choice([True, False]) for _ in range(400)]
professions = ['Ingénieur', 'Médecin', 'Professeur', 'Commercial', 'Artisan']
modeles_vehicules = ['Yaris', 'Clio', '308', 'Golf', 'Série 3']
kilometrage_annuel = [random.randint(5000, 30000) for _ in range(400)]
genres_musique = ['Classique', 'Rock', 'Pop', 'Jazz', 'Hip-hop']
animal_compagnie = [random.choice([True, False]) for _ in range(400)]
utilisation_gps = [random.choice([True, False]) for _ in range(400)]
jeux_video_course = [random.choice([True, False]) for _ in range(400)]
pratique_relaxation = [random.choice([True, False]) for _ in range(400)]
habitudes_lecture = ['Thriller', 'Science-fiction', 'Roman', 'Historique', 'Fantaisie']

# Création du DataFrame
data = {
    'Client': clients,
    'Nombre_de_sinistres': sinistres,
    'Prime': prime,
    'Régime_alimentaire': [random.choice(regimes_alimentaires) for _ in range(400)],
    'Genre': [random.choice(genres) for _ in range(400)],
    'Région_d_habitation': [random.choice(regions) for _ in range(400)],
    'Fumeur': fume,
    'Enfants': enfants,
    'Alcool': alcool,
    'Salaire': salaires,
    'Âge': ages,
    'Marque_de_véhicule': [random.choice(marques) for _ in range(400)],
    'Type_de_carburant': [random.choice(carburants) for _ in range(400)],
    'Ancienneté_du_permis': anciennetes_permis,
    'Prix_du_véhicule': prix_vehicules,
    'Type_de_route_majoritaire': [random.choice(types_de_routes) for _ in range(400)],
    'Musique_calme_ou_excitante': [random.choice(musique_calme_ou_excitante) for _ in range(400)],
    'Conduite_de_nuit': conduite_de_nuit,
    'Utilisation_téléphone': utilisation_tel,
    'Profession': [random.choice(professions) for _ in range(400)],
    'Modèle_de_véhicule': [random.choice(modeles_vehicules) for _ in range(400)],
    'Kilométrage_annuel': kilometrage_annuel,
    'Genre_de_musique_préféré': [random.choice(genres_musique) for _ in range(400)],
    'Animal_de_compagnie':animal_compagnie,
    'Utilisation_GPS':utilisation_gps,
    'Jeux_video_courses':jeux_video_course,
    'Pratique_relaxation':pratique_relaxation,
    'Habitudes_de_lecture':[random.choice(habitudes_lecture) for _ in range(400)]
    }

df = pd.DataFrame(data)
print(df)

# Autre méthode pour afficher les premières lignes du jeu de données pour voir à quoi il ressemble
print(df.head())

df.to_csv('resultats.csv', index=False)