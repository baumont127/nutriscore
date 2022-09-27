# Projet 1 - Groupe 5

### Utilisation de du modèle :

`
from joblib import load
features = [energy_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, fibre_100g, proteins_100g, salt_100g]
clf = load('nutriscore.joblib')
prediction = clf.predict(features)
`

Il s'agit d'un modèle de classification de type Random Forest.  
Features est une liste contenant les valeurs nutritionnelles utilisées pour la prédiction du Nutriscore.

# Installation de l' application

### 1 - Téléchargement du dépôt git :

`git clone https://gitlab.com/simplon-dev-ia/grenoble-2021-2022/projets/projet-1/projet-1-groupe-5.git
`

### 2 - Installation de l'environnement virtuel:

`pipenv install`

### 3 - Lancement du serveur flask

`3.export FLASK_APP=main.py
4.flask run`

# Utilisation de l'application en remplissant le formulaire

Ouvrez votre navigateur internet et tapez l'adresse `http://127.0.0.1:5000/`
