import numpy as np
import matplotlib.pyplot as plt

rayon_circuit = 0.5
eps = 0.01


#Courbe paramétrique centrale
def f(t):
    return np.asarray([t, t**3-t])

def f_prime(t):
    return np.asarray([np.ones(len(t)), 3*t**2-1])

params = np.linspace(-1.5,1.5, 1000)
pos = f(params)
speed = f_prime(params)
orth_x = speed[1]
orth_y = -speed[0]
orth = np.stack([orth_x, orth_y])


#Normaliser les vecteurs
orth_normalise = orth / np.sqrt(orth_x**2 + orth_y**2)


#Détection des points trop proches du circuit
def distance_min(pos, point):
    #print(np.linalg.norm(pos.T-point, axis=1))
    return np.min(np.linalg.norm(pos.T-point, axis=1))

def points_gardes(pos, liste_points):
    liste = []
    for i in range(len(pos[0])):
        point = liste_points[:,i]
        if abs(distance_min(pos,point)-rayon_circuit)<eps:
            liste.append(point)
    return np.asarray(liste).T

liste_points_gauche = np.stack((pos[0]- rayon_circuit*orth_normalise[0], pos[1] - rayon_circuit*orth_normalise[1]))
liste_points_droite = np.stack((pos[0]+ rayon_circuit*orth_normalise[0], pos[1] + rayon_circuit*orth_normalise[1]))

liste_gauche_triee = points_gardes(pos, liste_points_gauche)
liste_droite_triee = points_gardes(pos, liste_points_droite)
