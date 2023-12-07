import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy.optimize import fsolve

width= 0.5
eps= 0.00001

def f(t):
    y=t**3-t
    return np.asarray([t, y])

def f_prime(t):
    return np.asarray([np.ones(len(t)), 3*t**2-1])

params=np.linspace(-1,1,1000)
pos=f(params)
speed=f_prime(params)

orth_x=speed[1]
orth_y=-speed[0]
orth=np.stack([orth_x,orth_y])

#normalisation vecteurs
norme=np.sqrt(orth_x**2 + orth_y**2)
orth_normalise = orth / norme

#affichage vecteurs vitesses
#plt.quiver(pos[0],pos[1], speed[0], speed[1], angles='xy', color= 'r')

#affichage vecteurs orthogonaux à droite
#plt.quiver(pos[0],pos[1], orth_normalise[0], orth_normalise[1], angles='xy', color='y')

#à gauche
#plt.quiver(pos[0],pos[1], -orth_normalise[0], -orth_normalise[1], angles='xy', color='y')



plt.plot(pos[0],pos[1],'b--')
#bordure droite
plt.plot(pos[0]+orth_normalise[0]*width , pos[1]+orth_normalise[1]*width, color='k' )
#bordure gauche
plt.plot(pos[0]-orth_normalise[0]*width , pos[1]-orth_normalise[1]*width, color='k' )

#gca=get current acces
plt.gca().set_aspect('equal')
plt.show()

#detection des points trop proches du circuit
def dist_min(pos, point):
    return min(np.sqrt((pos[0][i]-point[0])**2+(pos[1][i]-point[1])**2) for i in range(len(pos[0])))

liste_points_gauche=np.stack((pos[0]-orth_normalise[0]*width , pos[1]-orth_normalise[1]*width))
liste_points_droite=np.stack((pos[0]+orth_normalise[0]*width , pos[1]+orth_normalise[1]*width))

def points_gardes(pos, liste_points):
    liste=[[],[]]
    for i in range(len(pos[0])):
        point=(liste_points[0][i], liste_points[1][i])
        if abs(dist_min(pos,point)-0.5)<eps:
            liste[0].append(point[0])
            liste[1].append(point[1])
    return liste

bordure=(pos[0]+orth_normalise[0]*width , pos[1]+orth_normalise[1]*width)

l=[dist_min(pos, point) for point in bordure]
distances = np.asarray(l)
plt.plot(bordure[distances > width * 0.98])


def distance(t0, t1):
   integrate.quad(lambda t: abs(f_prime(t)), t0, t1)
   


if __name__=="__main__":
    test()                  #fonction test à definir


