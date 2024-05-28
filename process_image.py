import os

def process_images_in_folder(folder_path, json_folder_path):
    
    image_files = [i for i in os.listdir(folder_path) if i.lower().endswith(('.png', '.jpg', '.jpeg'))]
    json_image_files = [j for j in os.listdir(json_folder_path) if j.lower().endswith('.json')]
    
    return image_files,json_image_files