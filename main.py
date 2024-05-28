from process_image import *
from detection import *

def Main():
    images_path = "validation"
    json_images_path = "json_files"
    images,json_images = process_images_in_folder(images_path, json_images_path)
    
    print(images)
    print(json_images)
    
Main()