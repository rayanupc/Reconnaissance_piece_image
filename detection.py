from hough import HoughTreeatement
from pretraitement import *
import matplotlib.pyplot as plt
import os



def see(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.gca()
    plt.show()

def main(img):
    # Extraire le nom de l'image à partir du chemin
    nom_image = os.path.basename(img)
    image = mpimg.imread(img)
    image_traitee, images_data = HoughTreeatement(image, nom_image)
    '''for data in images_data:
        print("center 1 : " + str(data[0]) + ", dimaètre_point : " + str(data[1]))'''
    see(image_traitee)

img = "17.jpg"
main(img)