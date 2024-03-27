import json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import os

# Fonction pour charger les données annotées à partir des fichiers JSON
def load_data_from_folder(folder_path):
    X = []  # Features
    y = []  # Labels

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                data = json.load(f)
                for shape in data['shapes']:
                    label = shape['label']
                    # Ici, vous pouvez extraire les fonctionnalités des annotations JSON si nécessaire
                    X.append(...)  # Extraire les fonctionnalités des annotations JSON si nécessaire
                    y.append(label)
                
    return np.array(X), np.array(y)

# Fonction pour extraire les caractéristiques d'une image
def extract_features_from_image(image):
    # Prétraitement de l'image (redimensionnement, normalisation, etc.) si nécessaire
    # Par exemple, redimensionnez l'image à 100x100 et convertissez-la en niveaux de gris
    image_resized = image.resize((100, 100)).convert('L')
    
    # Convertir l'image en un tableau numpy
    image_array = np.array(image_resized)
    
    # Aplatir le tableau pour obtenir un vecteur de caractéristiques
    features = image_array.flatten()
    
    return features

# Chemin vers le dossier contenant les fichiers JSON annotés
folder_path = '/chemin/vers/votre/dossier/contenant/les/images'

# Charger les données à partir du dossier contenant les fichiers JSON
X_train, y_train = load_data_from_folder(folder_path)

# Encoder les étiquettes en valeurs numériques
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y_train)

# Initialiser et entraîner le modèle KNN
knn_model = KNeighborsClassifier(n_neighbors=8)  # Vous pouvez ajuster le nombre de voisins
knn_model.fit(X_train, y_encoded)

# Chemin vers l'image à tester
image_path = '/chemin/vers/votre/image.jpg'

# Charger et prétraiter l'image
image = Image.open(image_path)

# Extraire les caractéristiques de l'image
features = extract_features_from_image(image)

# Faire des prédictions avec le modèle KNN
predicted_label = knn_model.predict(features.reshape(1, -1))
predicted_label = label_encoder.inverse_transform(predicted_label)

print("Montant de la pièce prédit :", predicted_label[0])
