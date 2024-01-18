import circuit
import checkpoint
import trajectoire
import affichage
import numpy as np
import scipy.optimize
import argparse

parser=argparse.ArgumentParser()
parser.add_argument(name_or_flags, kwargs)

def main(N, rayon_circuit, x0, xf, f, f_prime):
    params = np.linspace(x0,xf, 1000)
    pos = f(params)
    speed = f_prime(params)
    orth_x = speed[1]
    orth_y = -speed[0]
    orth = np.stack([orth_x, orth_y])
    
    
    #Normaliser les vecteurs
    orth_normalise = orth / np.sqrt(orth_x**2 + orth_y**2)
    
    liste_points_gauche = np.stack((pos[0]- rayon_circuit*orth_normalise[0], pos[1] - rayon_circuit*orth_normalise[1]))
    liste_points_droite = np.stack((pos[0]+ rayon_circuit*orth_normalise[0], pos[1] + rayon_circuit*orth_normalise[1]))
    
    liste_gauche_triee = circuit.points_gardes(pos, liste_points_gauche)
    liste_droite_triee = circuit.points_gardes(pos, liste_points_droite)
    
    ###CHECKPOINT####
    
    #abcisse checkpoints
    t=checkpoint.calcul_checkpoints(circuit.f_prime, x0, xf)
    
    #ordonnées checkpoints
    (x,y)=circuit.f(np.asarray(t))

    #checkpoint gauche et droite
    params2 = np.array(t)
    speed2 = circuit.f_prime(params2)
    orth_x = speed2[1]
    orth_y = -speed2[0]
    orth = np.stack([orth_x, orth_y])
    
    orth_normalise = orth / np.sqrt(orth_x**2 + orth_y**2)
    
    liste_points_gauche = np.stack((x- circuit.rayon_circuit*orth_normalise[0], y - circuit.rayon_circuit*orth_normalise[1]))
    liste_points_droite = np.stack((x+ circuit.rayon_circuit*orth_normalise[0], y + circuit.rayon_circuit*orth_normalise[1]))
    
    L=np.asarray((x,y))
    points_gauche_valides=checkpoint.points_gardes_ckpt(L, liste_points_gauche)
    points_droite_valides=checkpoint.points_gardes_ckpt(L, liste_points_droite)
    
    
    ###TRAJECTOIRE###
    
    D=np.transpose(points_droite_valides)
    G=np.transpose(points_gauche_valides)
    
    G[0] = (G[0]+D[0])/2
    D[0] = G[0]
    
    results= scipy.optimize.least_squares(trajectoire.calcul_f, np.repeat(1/2,len(G)), bounds=(0,1))
    t=results.x
    
    #renvoie un result: object contenant t + valeur atteinte en t et autre parties de l'optimisation
    #point de depart t=1/2, attention t entre 0 et 1 (argument bounds)
    
    P= D+np.reshape(t,(len(t),1))*(G-D)
    
    affichage.circuit(pos)
    affichage.bordure(liste_gauche_triee,liste_droite_triee)
    
if __name__=="__main__":
    main()
