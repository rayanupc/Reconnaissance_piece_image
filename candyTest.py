import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def CandiTreatement(img):

    # Charger une image
    image = cv2.imread(img)

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer Canny Edge Detection pour détecter les contours
    edges = cv2.Canny(gray, 50, 150)

    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les contours sur l'image originale
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Extraire le nom de l'image à partir du chemin
    nom_image = os.path.basename(img)

    # Retourner à la fois l'image traitée et le nom de l'image
    return image, nom_image

'''img = "149.jpg"
image, image_name = CandiTreatement(img)
print(image_name)
plt.imshow(image, cmap=plt.cm.gray)
plt.gca()
plt.show()'''