import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import feature


def threshold_image(im, th):
    thresholded_im = np.zeros(im.shape)
    thresholded_im[im >= th] = 1
    return thresholded_im

def compute_otsu_criteria(im, th):
    thresholded_im = threshold_image(im, th)
    nb_pixels = im.size
    nb_pixels1 = np.count_nonzero(thresholded_im)
    weight1 = nb_pixels1 / nb_pixels
    weight0 = 1 - weight1
    if weight1 == 0 or weight0 == 0:
        return np.inf

    val_pixels1 = im[thresholded_im == 1]
    val_pixels0 = im[thresholded_im == 0]
    var0 = np.var(val_pixels0) if len(val_pixels0) > 0 else 0
    var1 = np.var(val_pixels1) if len(val_pixels1) > 0 else 0

    return weight0 * var0 + weight1 * var1

def find_best_threshold(im):
    threshold_range = range(np.max(im) + 1)
    criterias = [compute_otsu_criteria(im, th) for th in threshold_range]
    best_threshold = threshold_range[np.argmin(criterias)]
    return best_threshold

path_image = '/Users/rayanalmohaize/Documents/L3/image/Images/100.jpg'
im = np.asarray(Image.open(path_image).convert('L'))  # Convertir l'image en niveaux de gris
im_otsu = threshold_image(im, find_best_threshold(im))

# Afficher les images
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
plt.title('Original Image', fontsize=20)
plt.imshow(im, cmap='gray')  # Spécifier que l'image est en niveaux de gris
plt.subplot(1, 2, 2)
plt.title('Otsu Method Image', fontsize=20)
plt.imshow(im_otsu, cmap='gray')  # Spécifier que l'image est en niveaux de gris
plt.tight_layout()
plt.show()

