import math



def distance_entre_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculer_rayon(centre, point_sur_cercle):
    x_c, y_c = centre
    x_p, y_p = point_sur_cercle
    return math.sqrt((x_p - x_c)**2 + (y_p - y_c)**2)

def calculer_surface_chevauchement(rayon1, rayon2, distance):
    if distance >= rayon1 + rayon2:
        return 0  # Pas de chevauchement
    elif distance <= abs(rayon1 - rayon2):
        return math.pi * min(rayon1, rayon2) ** 2  # Un cercle est à l'intérieur de l'autre
    else:
        part1 = (rayon1**2) * math.acos((distance**2 + rayon1**2 - rayon2**2) / (2 * distance * rayon1))
        part2 = (rayon2**2) * math.acos((distance**2 + rayon2**2 - rayon1**2) / (2 * distance * rayon2))
        part3 = 0.5 * math.sqrt((-distance + rayon1 + rayon2) * (distance + rayon1 - rayon2) * (distance - rayon1 + rayon2) * (distance + rayon1 + rayon2))
        return part1 + part2 - part3
    
def calculer_taux_chevauchement(surface_chevauchement, rayon):
    return (surface_chevauchement / (math.pi * rayon ** 2)) * 100

# Exemple d'utilisation

'''Centre_point_a = (1730.2222222222222, 1773.222222222222)
Centre_point_b = (1730.2222222222222, 1773.222222222222)  # Les centres sont identiques

point_a = [Centre_point_a, (1080.7777777777778, 2535.777777777778)]
point_b = [Centre_point_b, (1080.7777777777778, 2535.777777777778)]  # Les points sur les cercles sont identiques

rayon1 = calculer_rayon(Centre_point_a, point_a[1])
rayon2 = calculer_rayon(Centre_point_b, point_b[1])
distance_centres = distance_entre_points(Centre_point_a, Centre_point_b)

surface_chevauchement = calculer_surface_chevauchement(rayon1, rayon2, distance_centres)
taux_chevauchement = calculer_taux_chevauchement(surface_chevauchement, rayon1)
print("Surface de chevauchement des deux cercles :", surface_chevauchement)
print("Taux de chevauchement des deux cercles :", taux_chevauchement)'''
