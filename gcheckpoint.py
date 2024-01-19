import circuit
from scipy.optimize import root_scalar
import scipy.integrate as integrate
import numpy as np



def distance(t0, t1, f_prime):
   return integrate.quad(lambda t: np.linalg.norm(f_prime(t)), t0, t1)[0]
     

def calcul_checkpoints(f_prime, td, ta, n):
    L=[]
    t_prec=td
    D=distance(td, ta, f_prime)/n   #Distance entre les checkpoints 
    for i in range(n-1):
        g=lambda t: distance(t_prec, t, f_prime)-D
        x0_guess= t_prec + D
        if x0_guess> ta:
            x0_guess=(ta + t_prec)/2
        t_prec=root_scalar(g, bracket=(t_prec,ta),fprime=lambda t:np.linalg.norm(f_prime(t)), x0=x0_guess).root
        L.append(t_prec)
    L.append(ta)
    return L


#garder que les points sur la courbes et placer checkpoints sur points valides
def points_gardes_ckpt(L, liste_points, rayon_circuit):
    liste = []
    eps=0.01
    for i in range(len(L[0])):
        point = liste_points[:,i]
        if abs(circuit.distance_min(L,point)-rayon_circuit)<eps:
            liste.append(point)
        else:
            liste.append(liste[-1])
    return np.asarray(liste).T
