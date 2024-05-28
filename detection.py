from hough import HoughTreeatement
from pretraitement import *
from evaluation import *
import matplotlib.pyplot as plt
import os



def see(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.gca()
    plt.show()

def detection(img,img_json):
    # Extraire le nom de l'image à partir du chemin
    nom_image = os.path.basename(img)
    image = mpimg.imread(img)
    images_data = HoughTreeatement(image, nom_image)
    eval = evaluation_detection(images_data,img_json)
    taux_piece_fausse = evaluation_nombre_piece(images_data,img_json)
    print("eval = " + str(eval) + ", taux piece fausse = " + str(taux_piece_fausse))
    return eval,taux_piece_fausse

img = "validation/0.jpg"
img_json = "json_files/0.json"
detection(img,img_json)