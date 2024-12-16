import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import geopandas as gpd
import numpy as np
import altair as alt

#Pour régler l'erreur seaborn : "missing ScriptRunContext! This warning can be ignored when running in bare mode."
#from streamlit.runtime.scriptrunner import add_script_run_ctx,get_script_run_ctx
#from subprocess import Popen

#ctx = get_script_run_ctx()
##Some code##
#process = Popen(['python','donnees.py'])
#add_script_run_ctx(process,ctx)

#pour l'affichage du gif
import base64

st.markdown("<h1 style='text-align: center'>🔮 Bienvenue dans la tente mystique de Madame Irma... </h1>", unsafe_allow_html=True)

#affichage gif
gifPath = "C:\\Users\\anais\\Downloads\\loss prediction\\crystal.gif"
file_ = open(gifPath, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

with st.columns(3)[1]:
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
    unsafe_allow_html=True,
)
st.markdown("")
st.markdown("<div style='text-align: justify;'>Prêt à connaître ce que l'univers a prévu pour toi ? Réponds à mes questions, laisse les étoiles guider mes calculs, et je te dévoilerai la prime d'assurance auto qui te correspond, aussi unique que toi, mon cher voyageur ! 🌠</div>", unsafe_allow_html=True)
st.markdown("")


prenom = st.text_input("Comment t'appelles-tu ?")
if prenom:
    st.write(f"Aaahhhh comme c'est magnifique ! Bonjour, {prenom} !")


age = st.number_input("Quel âge as-tu ?")
if age:
    st.write(f"{age} ans ?! Tu es si jeune.")

nb_sinistres = st.number_input("Combien de sinistres as-tu eu ?")

genre = st.selectbox(
    "Quel est ton genre ?",
    ("Homme", "Femme", "Non-binaire"),
)

regime = st.selectbox(
    "Quel est ton régime alimentaire ?",
    ("Flexitarien", "Omnivore", "Pescetarien", "Végétalien", "Végétarien"),
)

region = st.selectbox(
    "Dans quelle région habites-tu ?",
("Auvergne-Rhône-Alpes",
"Bourgogne-Franche-Comté",
"Bretagne",
"Centre-Val de Loire",
"Corse",
"Grand Est",
"Hauts-de-France",
"Ile-de-France",
"Normandie",
"Nouvelle-Aquitaine",
"Occitanie",
"Pays de la Loire",
"Provence Alpes Côte d’Azur"),
)

fumeur = st.checkbox("Coche cette case si tu fumes.")
alcool = st.checkbox("Coche cette case si tu bois.")
enfant = st.checkbox("Coche cette case si tu as des enfants.")
telephone = st.checkbox("Coche cette case si tu utilises ton téléphone au volant.")
nuit = st.checkbox("Coche cette case si tu conduis la nuit.")
animal = st.checkbox("Coche cette case si tu as un animal de compagnie.")
jeu_course = st.checkbox("Coche cette case si tu joues à des jeux vidéo de course automobile.")
relaxation = st.checkbox("Coche cette case si tu pratiques la relaxation.")
gps = st.checkbox("Coche cette case si tu utilises le GPS.")

type_musique = st.selectbox(
    "Quel type de musique écoutes-tu ?",
    ("Calme", "Excitante"),
)

type_route = st.selectbox(
    "Sur quel type de route roules-tu en majorité ?",
    ("Urbain", "Autoroute", "Rural"),
)

carburant = st.selectbox(
    "Quel type de carburant utilises-tu ?",
    ("Essence", "Diesel", "Hybride", "Électrique"),
)

voiture = st.selectbox(
    "Quel est la marque de ta voiture ?",
    ("Toyota", "Renault", "Peugeot", "BMW", "Volkswagen"),
)

salaire = st.number_input("Quel est ton salaire ?")

anciennete = st.number_input("Depuis combien d'années as-tu ton permis ?")

musique = st.selectbox(
    "Quel genre de musique écoutes-tu ?",
    ("Classique", "Rock", "Pop", "Jazz", "Hip-hop"),
)

profession = st.selectbox(
    "Quel est ta profession ?",
    ("Ingénieur", "Médecin", "Professeur", "Commercial", "Artisan"),
)

modele_vehicule = st.selectbox(
    "Quel est ton modèle de véhicule ?",
    ("Yaris", "Clio", "308", "Golf", "Série 3"),
)

#ENREGISTREMENT ET AFFICHAGE
if st.button("Enregistrer les informations"):
    utilisateur = {"Prénom": prenom, "Âge": age, "Genre": genre, "Régime alimentaire":regime, "Région":region, "Fumeur":fumeur,
                   "Modèle de véhicule":modele_vehicule, "Profession":profession, "Musique":musique, "Ancienneté du permis":anciennete,
                   "Salaire":salaire,"Marque de la voiture":voiture,"Type de carburant":carburant,"Type de route emprunté":type_route,
                   "Type de musique":type_musique, "Alcool":alcool, "Enfant":enfant, "Téléphone":telephone,
                   "Conduite de nuit":nuit, "Animal":animal, "Jeu de course":jeu_course,"Pratique de la relaxation":relaxation,
                   "Utilisation du GPS":gps, "Nombre de sinistres":nb_sinistres}
    
    st.success("Informations enregistrées avec succès !")
    
    # Afficher les données sauvegardées
    st.write("Si j'ai bien compris, tu as saisi les informations suivantes :")
    st.write(utilisateur)

st.markdown("<div style='text-align: justify;'>Très bien, laisse-moi voir ça... Hum... Oui, oui... Je ressens une énergie spéciale... Attends... Voilà, j’ai le chiffre ! Ta prime est prête ! 💥</div>", unsafe_allow_html=True)

st.text(" ")
# Prédiction de la prime
if st.button("Voir le montant de la prime d'assurance"):
    
    prime_de_base = 300  # Prime de base en euros
    prime_estimee = (
            prime_de_base +
            age * 0.5 +
            nb_sinistres * 100 +
            (150 if fumeur == "true" else 0) +
            (200 if alcool == "true" else 0) +
            (50 if nuit == "true" else 0) +
            (200 if telephone == "true" else 0)+
            (100 if animal == "true" else 0)+
            (100 if jeu_course == "false" else 0)+
            (100 if regime == "Omnivore" else 0)
        )

    st.write(f"### Prime d'assurance estimée : {prime_estimee:.2f} €")

df = pd.read_csv("resultats.csv")
print(df.head())

st.write("# Statistiques descriptives")


#GENRE

accidents_par_genre = df.groupby('Genre')['Nombre_de_sinistres'].sum().reset_index()

 # Afficher le tableau des sinistres par région
st.write("#### Nombre de sinistres par genre")
st.dataframe(accidents_par_genre.sort_values(by='Nombre_de_sinistres', ascending=False))

# Supposons que 'Genre' et 'Nombre d\'accidents' soient les colonnes pertinentes
genres = accidents_par_genre['Genre']
n_sinistres = accidents_par_genre['Nombre_de_sinistres']

# Calcul des pourcentages
pourcentages = (n_sinistres / n_sinistres.sum()) * 100

# Création du donut chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(pourcentages, labels=genres, autopct='%1.1f%%', startangle=100, wedgeprops={'width': 0.3})

# Afficher le graphique dans Streamlit
st.pyplot(fig)


#REGION

sinistres_par_region = df.groupby('Région_d_habitation')['Nombre_de_sinistres'].sum().reset_index()

 # Afficher le tableau des sinistres par région
st.write("#### Nombre de sinistres par région")
st.dataframe(sinistres_par_region.sort_values(by='Nombre_de_sinistres', ascending=False))

    # Charger une carte des régions de France (GeoJSON)
france_regions = gpd.read_file("https://france-geojson.gregoiredavid.fr/repo/regions.geojson")

    # Fusionner les données avec la carte
france_regions = france_regions.merge(sinistres_par_region, left_on='nom', right_on='Région_d_habitation', how='left')

    # Remplir les régions sans données avec 0 sinistre
france_regions['Nombre_de_sinistres'] = france_regions['Nombre_de_sinistres'].fillna(0)

    # Créer une carte avec Geopandas
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
france_regions.plot(column='Nombre_de_sinistres', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_xlim([-5.0, 10])  # Ajuster les limites longitude
ax.set_ylim([41.0, 51.5])  # Ajuster les limites latitude

    # Afficher la carte dans Streamlit
st.pyplot(fig)


#HEATMAP

st.write("#### Matrice des corrélations")

# Sélectionner les colonnes pertinentes : variables et le nombre de sinistres
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

# Calcul des corrélations
correlation_matrix = df[numerical_cols].corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot(plt)

st.markdown(
    """
    - Les valeurs proches de 1 indiquent une forte corrélation positive.
    - Les valeurs proches de -1 indiquent une forte corrélation négative.
    - Les valeurs proches de 0 indiquent peu ou pas de corrélation.
    """
)

#JEU

st.write("#### Nombre de sinistres selon la pratique des jeux vidéo de course")
# Colonnes pertinentes : Nombre de sinistres et "joue_t-il_a_des_jeux_vidéo_de_course"
sinistres = df['Nombre_de_sinistres']
jeux_cour = df['Jeux_video_courses']


somme_sinistres_jeu = df.groupby("Jeux_video_courses")["Nombre_de_sinistres"].sum()
st.write(somme_sinistres_jeu)

plt.figure(figsize=(8, 6))
somme_sinistres_jeu.plot(kind='bar', color=['blue', 'orange'])
plt.ylabel('Somme des sinistres')
st.pyplot(plt)


#MUSIQUE

st.write("#### Nombre de sinistres selon le type de musique écouté")
# Colonnes pertinentes : Nombre de sinistres et "joue_t-il_a_des_jeux_vidéo_de_course"
sinistres = df['Nombre_de_sinistres']
musique = df['Musique_calme_ou_excitante']


somme_sinistres_musique = df.groupby("Musique_calme_ou_excitante")["Nombre_de_sinistres"].sum()
st.write(somme_sinistres_musique)

plt.figure(figsize=(8, 6))
somme_sinistres_musique.plot(kind='bar', color=['green', 'yellow'])
plt.ylabel('Somme des sinistres')
st.pyplot(plt)

#REGIME ALIMENTAIRE

st.write("#### Nombre de sinistres selon le régime alimentaire")

moyenne_sinistres_regime = df.groupby("Régime_alimentaire")["Nombre_de_sinistres"].mean()
st.write(moyenne_sinistres_regime)

# Compter le nombre de sinistres par régime alimentaire
somme_sinistres_regime = df.groupby("Régime_alimentaire")["Nombre_de_sinistres"].sum().reset_index()
st.write(somme_sinistres_regime)

plt.figure(figsize=(8, 6))
sns.barplot(x="Régime_alimentaire", y="Nombre_de_sinistres", data=somme_sinistres_regime)
plt.title("Nombre de sinistres par régime alimentaire")
plt.xlabel("Régime Alimentaire")
plt.ylabel("Nombre de Sinistres")
plt.show()

#Affichage Streamlit
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="Régime_alimentaire", y="Nombre_de_sinistres", data=somme_sinistres_regime, ax=ax)
ax.set_xlabel("Régime Alimentaire")
ax.set_ylabel("Nombre de Sinistres")

# Afficher le graphique dans Streamlit
st.pyplot(fig)

st.write("#### Distribution des données")

#graphique interactif

# Sélection de la variable explicative
variable = st.selectbox(
    "Choisissez une variable à explorer",
    options=['Alcool', 'Fumeur', 'Enfants', 'Animal_de_compagnie', 'Habitudes_de_lecture','Genre_de_musique_préféré', 'Type_de_carburant']
)

# Agrégation des données pour créer le graphique
agg_data = df.groupby(variable)['Nombre_de_sinistres'].mean().reset_index()

# Création du graphique avec Altair
chart = alt.Chart(agg_data).mark_bar().encode(
    x=alt.X(variable, title=variable),
    y=alt.Y('Nombre_de_sinistres', title='Moyenne des sinistres'),
    color=alt.Color(variable, legend=None)
).properties(
    title=f"Relation entre {variable} et le nombre de sinistres",
    width=600,
    height=400
)

# Affichage du graphique
st.altair_chart(chart)



# Filtres interactifs
revenu_min, revenu_max = st.slider(
    "Filtrer par revenu annuel",
    min_value=int(df['Salaire'].min()),
    max_value=int(df['Salaire'].max()),
    value=(30000, 80000)  # Valeur par défaut
)

age_min, age_max = st.slider(
    "Filtrer par âge",
    min_value=int(df['Âge'].min()),
    max_value=int(df['Âge'].max()),
    value=(25, 60)  # Valeur par défaut
)

# Application des filtres
filtered_data = df[(df['Salaire'] >= revenu_min) & (df['Salaire'] <= revenu_max)]
filtered_data = filtered_data[(filtered_data['Âge'] >= age_min) & (filtered_data['Âge'] <= age_max)]

# Création du graphique
chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='Salaire',
    y='Nombre_de_sinistres',
    color='Âge',
    tooltip=['Salaire', 'Nombre_de_sinistres', 'Âge']
).properties(
    width=700,
    height=400
)

# Affichage du graphique
st.altair_chart(chart)

# Ajout d'un filtre avec un slider
anciennete_min, anciennete_max = st.slider(
    "Sélectionnez la plage d'ancienneté du permis (en années)",
    min_value=int(df['Ancienneté_du_permis'].min()),
    max_value=int(df['Ancienneté_du_permis'].max()),
    value=(5, 30)  # Plage par défaut
)

# Filtrage des données en fonction de l'ancienneté
filtered_data = df[(df['Ancienneté_du_permis'] >= anciennete_min) & 
                     (df['Ancienneté_du_permis'] <= anciennete_max)]

# Calcul de la moyenne des sinistres par ancienneté
agg_data = filtered_data.groupby('Ancienneté_du_permis')['Nombre_de_sinistres'].mean().reset_index()

# Création du graphique avec Altair
chart = alt.Chart(agg_data).mark_line(point=True).encode(
    x=alt.X('Ancienneté_du_permis', title='Ancienneté_du_permis'),
    y=alt.Y('Nombre_de_sinistres', title='Moyenne des sinistres'),
    tooltip=['Ancienneté_du_permis', 'Nombre_de_sinistres']
).properties(
    title="Relation entre ancienneté du permis et nombre de sinistres",
    width=700,
    height=400
)

# Affichage du graphique dans Streamlit
st.altair_chart(chart)