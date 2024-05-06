from hough import HoughTreeatement
from candyTest import CandiTreatement
from pretraitement import *
import matplotlib.pyplot as plt



def see(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.gca()
    plt.show()

def main(img):
    # Extraire le nom de l'image à partir du chemin
    nom_image = os.path.basename(img)
    image = mpimg.imread(img)
    image_traitee = HoughTreeatement(image, nom_image)
    see(image_traitee)

img = '19.jpg'
main(img)