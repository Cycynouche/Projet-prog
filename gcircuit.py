import numpy as np

#Détection des points trop proches du circuit
def distance_min(pos, point):
    return np.min(np.linalg.norm(pos.T-point, axis=1))    
#axis=1 spécifie que la norme doit être calculée le long de l'axe 1, qui correspond aux lignes


def points_gardes(pos, liste_points, rayon_circuit):
    liste = []
    eps = 0.01
    for i in range(len(pos[0])):
        point = liste_points[:,i]
        if abs(distance_min(pos,point)-rayon_circuit)<eps:
            liste.append(point)
    return np.asarray(liste).T
