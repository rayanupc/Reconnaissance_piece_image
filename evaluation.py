import json
from metrique_entrainement import *

#image_data c'est une liste de tuple, dans les tuples il y a un tuple centre/rayon 
def evaluation_detection(image_data, image_json):
    with open(image_json, 'r') as js:
        data = json.load(js)

    circles = len(image_data)
    circle_shapes = [shape for shape in data['shapes'] if shape['shape_type'] == 'circle']
    circle_count = len(circle_shapes)
    circle_empty = circles - circle_count

    liste_overlap = []
    
    for i in range(circle_count):
        centre_json, pt_json = circle_shapes[i]['points'][0], circle_shapes[i]['points'][1]
        rayon_pred = calculer_rayon(image_data[i][0],image_data[i][1])
        rayon_ver = calculer_rayon(centre_json, pt_json)
        distance = distance_entre_points(image_data[i][0], centre_json)#le deuxième data[0] doit être remplacer par le centre ds le fichier json
        surface_chevauchement = calculer_surface_chevauchement(rayon_pred,rayon_ver,distance)
        taux_chevauchement = calculer_taux_chevauchement(surface_chevauchement, rayon_ver)
        liste_overlap.append(taux_chevauchement)
    
    for j in range(circle_empty):
        liste_overlap.append(0)
    
    return sum(liste_overlap)/circles

def evaluation_nombre_piece(image_data, image_json):
    with open(image_json, 'r') as js:
        data = json.load(js)

    shapes = [shape for shape in data['shapes'] if shape['shape_type'] == 'circle']
    
    circle_nb_pred = len(image_data)
    circle_nb_ver = len(shapes)
    circle_nb_FAUX = circle_nb_pred - circle_nb_ver
    
    return (circle_nb_FAUX*100)/circle_nb_pred
        
        