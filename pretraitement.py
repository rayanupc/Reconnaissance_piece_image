import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2
import time

def color_to_gray(img):
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return imgGray
        

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

def seuillage(seuil, image):
    return np.where(image>seuil/256, 1, image)


'''image = '147.jpg'
best_threshold_image = find_best_threshold(image)
print(best_threshold_image)'''

#color_to_gray()