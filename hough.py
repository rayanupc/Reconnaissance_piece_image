import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
from pretraitement import *


def HoughTreeatement(img, nom_image):
    default_file = img

    # Charger une image
    src = cv.imread(cv.samples.findFile(nom_image), cv.IMREAD_COLOR)
    # Vérifier si l'image est chargée correctement
    if src is None:
        print("Erreur lors de l'ouverture de l'image!")
        print("Utilisation: hough_circle.py [nom_image -- par défaut"  + default_file + '] \n')
        return -1

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    seuil = find_best_threshold(gray)
    seuillage(seuil, gray)
    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    # Augmentez la valeur de minRadius pour rechercher des cercles plus grands
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=50, maxRadius=200)

    circle_data = []  # Liste pour stocker les données des cercles
    max_circles = 12
    if circles is not None:
        circles = np.uint16(np.around(circles))
        count = 0
        for i in circles[0, :]:
            if count >= max_circles:
                break
            center = (i[0], i[1])
            radius = i[2]
            # centre du cercle
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # contour du cercle
            cv.circle(src, center, radius, (255, 0, 255), 3)

            # Ajouter les coordonnées du centre et un point sur le contour (à droite du centre)
            circle_data.append((center, (center[0] + radius, center[1])))

            count += 1

    return src, circle_data

'''img = "149.jpg"
image_name = "149.jpg"
image = HoughTreeatement(img, image_name)

plt.imshow(image, cmap=plt.cm.gray)
plt.gca()
plt.show()'''