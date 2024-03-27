import json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os


# Charger les données annotées à partir des fichiers JSON
def charger_donnees_de_dossier(chemin_dossier):
    X = []  # Caractéristiques
    y = []  # Étiquettes

    for nom_fichier in os.listdir(chemin_dossier):
        if nom_fichier.endswith('.json'):
            with open(os.path.join(chemin_dossier, nom_fichier), 'r') as f:
                donnees = json.load(f)
                for forme in donnees['shapes']:
                    # Exemple: annotation = {'label': '2 euros', 'bbox': [x, y, width, height]}
                    etiquette = forme['label']
                    caractéristique = extraire_caractéristique(forme)  
                    X.append(caractéristique)
                    y.append(etiquette)
                
    return np.array(X), np.array(y)

def extraire_caractéristique(annotation):
    """
    Extrait la valeur de la pièce à partir du fichier JSON annoté par Labelme.
    
    Parameters:
    annotation (dict): Données d'annotation.
    
    Returns:
    float: La valeur de la pièce annotée dans le fichier JSON.
    """
    # Extraire la valeur de la pièce à partir de l'annotation
    etiquette_piece = annotation['label']
    
    montants_pieces = {
    '2 euro': 2.0,
    '1 euro': 1.0,
    '50 centime': 0.50,
    '20 centime': 0.20,
    '10 centime': 0.10,
    '5 centime': 0.05,
    '2 centime': 0.02,
    '1 centime': 0.01,
    }

    # Rechercher la sous-chaîne indiquant le montant de la pièce
    # Par exemple, si l'étiquette est "pièce de 50 centimes", extraire "50 centime"
    valeur_piece = None
    for cle in montants_pieces:
        if cle in etiquette_piece:
            valeur_piece = cle
            break

    # Si la valeur de la pièce est trouvée dans le dictionnaire, retourner sa valeur numérique
    if valeur_piece is not None:
        return montants_pieces[valeur_piece]
    else:
        # Gérer le cas où la valeur de la pièce n'est pas trouvée
        return None  # ou toute valeur par défaut que vous souhaitez

def extraire_caractéristiques_de_image(image):
    image_redimensionnee = image.resize((100, 100)).convert('L')
    
    # Convertir l'image en un tableau numpy
    tableau_image = np.array(image_redimensionnee)
    
    # Aplatir le tableau pour obtenir un vecteur de caractéristiques
    caractéristiques = tableau_image.flatten()
    
    return caractéristiques

# Chemin vers le dossier contenant les fichiers JSON annotés
chemin_dossier = '/Users/rayanalmohaize/Documents/L3/image/image_entrainement'

# Charger les données à partir du dossier contenant les fichiers JSON
X, y = charger_donnees_de_dossier(chemin_dossier)

# Encoder les étiquettes en valeurs numériques
encodeur_etiquettes = LabelEncoder()
y_encodé = encodeur_etiquettes.fit_transform(y)

# Diviser les données en ensembles d'entraînement et de test
X_entrainement, X_test, y_entrainement, y_test = train_test_split(X, y_encodé, test_size=0.2, random_state=42)

# Remodeler les données d'entraînement et de test
X_entrainement = X_entrainement.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Initialiser et entraîner le modèle KNN
modele_knn = KNeighborsClassifier(n_neighbors=8)  
modele_knn.fit(X_entrainement, y_entrainement)

# Faire des prédictions sur l'ensemble de test
y_pred = modele_knn.predict(X_test)

# Calculer la précision du modèle
precision = accuracy_score(y_test, y_pred)
print("Précision:", precision)