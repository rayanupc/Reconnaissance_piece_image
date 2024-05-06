from hough import HoughTreeatement
from candyTest import CandiTreatement
import matplotlib.pyplot as plt



def see(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.gca()
    plt.show()

def main(img):
    image, image_name = CandiTreatement(img)
    image_traiter = HoughTreeatement(image, image_name)
    see(image_traiter)

img = '149.jpg'
main(img)