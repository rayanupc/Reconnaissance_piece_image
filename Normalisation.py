import cv2
import numpy as np
import json

def normalize_image_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    image_path = data["imagePath"]
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Erreur : Impossible de charger l'image à partir de {image_path}")
        return
    
    if len(image.shape) > 2 and image.shape[2] > 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    normalized_image = image / 255.0
    
    cv2.imshow("Image normalisée", normalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

testJsonPath = "json_file/0.json"
normalize_image_from_json(testJsonPath) 