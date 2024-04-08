import cv2
import numpy as np
import os 

def normalize_image(image_folder, output_folder):

    if not os.path.exists(output_folder) :
        os.makedirs(output_folder)


    listeImg = os.listdir(image_folder)
    for img_name in listeImg:
        img_path = os.path.join(image_folder, img_name)
        image = cv2.imread(img_path)
        
        if image is None:
            print(f"Erreur : Impossible de charger l'image {img_path}")
            continue
        
        if len(image.shape) > 2 and image.shape[2] > 1:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        normalized_image = image / 255.0

        output_path = os.path.join(output_folder, img_name)
        cv2.imwrite(output_path, normalized_image * 255)
        
        print(f"Image normalisée enregistrée sous : {output_path}")

folderPath = "imgTrain"
output_folder = "images_Normalisées"
normalize_image(folderPath, output_folder)