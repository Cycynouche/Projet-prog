import circuit
from scipy.optimize import root_scalar
import scipy.integrate as integrate
import numpy as np

#Nombre de checkpoints
N=10


abscisse_g = circuit.liste_gauche_triee[0]
ordonnee_g = circuit.liste_gauche_triee[1]
abscisse_d = circuit.liste_droite_triee[0]
ordonnee_d = circuit.liste_droite_triee[1]



def distance(t0, t1):
   return integrate.quad(lambda t: np.linalg.norm(circuit.f_prime(t)), t0, t1)[0]
   
#Distance entre les checkpoints   
D=distance(-1.5,1.5)/N

def calcul_checkpoints(f_prime, td, ta, n):
    L=[td]
    t_prec=td
    for i in range(n-1):
        g=lambda t: distance(td, t)-D
        xo_guess= t_prec + D
        if xo_guess> ta:
            xo_guess=(ta + t_prec)/2
        t_prec= root_scalar(g, bracket=(t_prec,ta),fprime=lambda t:np.linalg.norm(f_prime(t)), x0=xo_guess).root
        L.append(t_prec)
    return L
