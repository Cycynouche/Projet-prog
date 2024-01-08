import circuit
from scipy.optimize import root_scalar
import scipy.integrate as integrate
import numpy as np

#Nombre de checkpoints
N=10


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


#Faire points bordures
params = np.array(t)
speed = circuit.f_prime(params)
orth_x = speed[1]
orth_y = -speed[0]
orth = np.stack([orth_x, orth_y])


#Normaliser les vecteurs
orth_normalise = orth / np.sqrt(orth_x**2 + orth_y**2)


liste_points_gauche = np.stack((x - circuit.rayon_circuit*orth_normalise[0],  y - circuit.rayon_circuit*orth_normalise[1]))
liste_points_droite = np.stack((x + circuit.rayon_circuit*orth_normalise[0], y + circuit.rayon_circuit*orth_normalise[1]))
