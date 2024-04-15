import math

#Précision = VraisPositif / (VraisPositif + FauxPositif)
#Rappel = VraisPositif / (VraisPositif + FauxNegatif) 
#score = 2 * (Précision * Rappel) / (Précision + Rappel) 

def distance_entre_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def calculer_rayon(centre, point_sur_cercle):
    x_c, y_c = centre
    x_p, y_p = point_sur_cercle
    rayon = math.sqrt((x_p - x_c)**2 + (y_p - y_c)**2)
    return rayon

def calcul_air(rayon):
    return 3.14*(rayon*rayon)

def calculer_surface_chevauchement(rayon1, rayon2, distance_centres):
    # Si la distance entre les centres est supérieure à la somme des rayons, il n'y a pas de chevauchement
    if distance_centres >= rayon1 + rayon2:
        return 0.0
    
    # Si l'un des cercles est entièrement inclus dans l'autre, la surface de chevauchement est égale à la surface du plus petit cercle
    if distance_centres + min(rayon1, rayon2) <= max(rayon1, rayon2):
        return math.pi * min(rayon1, rayon2)**2
    
    # Calcul de la surface de chevauchement en utilisant la formule des secteurs circulaires
    angle1 = math.acos((rayon1**2 + distance_centres**2 - rayon2**2) / (2 * rayon1 * distance_centres))
    angle2 = math.acos((rayon2**2 + distance_centres**2 - rayon1**2) / (2 * rayon2 * distance_centres))
    surface_chevauchement = rayon1**2 * angle1 + rayon2**2 * angle2 - 0.5 * (rayon1**2 * math.sin(2 * angle1) + rayon2**2 * math.sin(2 * angle2))
    
    return surface_chevauchement

# Exemple d'utilisation

Centre_point_a = (725.2222222222222,2434.222222222222)
Centre_point_b = (1730.7777777777778, 1773.111111111111)
Centre_point_c = (1430.7777777777778, 2584.222222222222)

point_a = [Centre_point_a,(1080.7777777777778,2539.777777777778)]
point_b = [Centre_point_b,(2069.666666666667,2112.0)]
point_c = [Centre_point_c,(1775.2222222222222,2589.777777777778)]

rayon1 = calculer_rayon(Centre_point_a, point_a[1])
rayon2 = calculer_rayon(Centre_point_b, point_b[1])
distance_centres = distance_entre_points(Centre_point_a,Centre_point_b)
overlap = calculer_surface_chevauchement(rayon1, rayon2, distance_centres)
print("Surface de chevauchement des deux cercles :", overlap)
