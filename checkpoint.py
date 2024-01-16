import circuit
from scipy.optimize import root_scalar
import scipy.integrate as integrate
import numpy as np

#Nombre de checkpoints
N=200


def distance(t0, t1):
   return integrate.quad(lambda t: np.linalg.norm(circuit.f_prime(t)), t0, t1)[0]
   
#Distance entre les checkpoints   
D=distance(-1.5,1.5)/N

def calcul_checkpoints(f_prime, td, ta, n):
    L=[]
    t_prec=td
    for i in range(n-1):
        g=lambda t: distance(t_prec, t)-D
        x0_guess= t_prec + D
        if x0_guess> ta:
            x0_guess=(ta + t_prec)/2
        t_prec=root_scalar(g, bracket=(t_prec,ta),fprime=lambda t:np.linalg.norm(f_prime(t)), x0=x0_guess).root
        L.append(t_prec)
    L.append(ta)
    return L

#abcisse checkpoints
t=calcul_checkpoints(circuit.f_prime, -1.5, 1.5, N)
#ordonnées checkpoints
(x,y)=circuit.f(np.asarray(t))

#checkpoint gauche et droite
params = np.array(t)
speed = circuit.f_prime(params)
orth_x = speed[1]
orth_y = -speed[0]
orth = np.stack([orth_x, orth_y])

orth_normalise = orth / np.sqrt(orth_x**2 + orth_y**2)

liste_points_gauche = np.stack((x- circuit.rayon_circuit*orth_normalise[0], y - circuit.rayon_circuit*orth_normalise[1]))
liste_points_droite = np.stack((x+ circuit.rayon_circuit*orth_normalise[0], y + circuit.rayon_circuit*orth_normalise[1]))


#garder que les points sur la courbes et placer checkpoints sur points valides
def points_gardes_ckpt(L, liste_points):
    liste = []
    for i in range(len(L[0])):
        point = liste_points[:,i]
        if abs(circuit.distance_min(L,point)-circuit.rayon_circuit)<circuit.eps:
            liste.append(point)
        else:
            liste.append(liste[-1])
    return np.asarray(liste).T

L=np.asarray((x,y))
points_gauche_valides=points_gardes_ckpt(L, liste_points_gauche)
points_droite_valides=points_gardes_ckpt(L, liste_points_droite)
