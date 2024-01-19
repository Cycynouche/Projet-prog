import circuit
import checkpoint
import trajectoire
import affichage
import numpy as np
import scipy.optimize
import argparse


def main(N, rayon_circuit, x0, xf, f, scp, scpline, sv):
    
    if f=='sinus':
        
        def f(t):
            return np.asarray([t, np.sin(t)])
        
        def f_prime(t):
            try:
                t_len = np.shape(t)[0]
            except:
                t_len = 1
            return np.asarray([np.ones(t_len), np.cos(t)])
        
    elif f=='chicane':
        
        def f(t):
            return np.asarray([t, t**3-t])
    
        def f_prime(t):
            try:
                t_len = np.shape(t)[0]
            except:
                t_len = 1
            return np.asarray([np.ones(t_len), 3*t**2-1])


    else:
        raise argparse.ArgumentError(f"Fonction inconnue: {f}")
        
    #bordure
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
    
    liste_gauche_triee = circuit.points_gardes(pos, liste_points_gauche, rayon_circuit)
    liste_droite_triee = circuit.points_gardes(pos, liste_points_droite, rayon_circuit)
    
    ###CHECKPOINT####
    
    #abcisse checkpoints
    t=checkpoint.calcul_checkpoints(f_prime, x0, xf, N)
    
    #ordonnées checkpoints
    (x,y)=f(np.asarray(t))

    #checkpoint gauche et droite
    params2 = np.array(t)
    speed2 = f_prime(params2)
    orth_x2 = speed2[1]
    orth_y2 = -speed2[0]
    orth2 = np.stack([orth_x2, orth_y2])
    
    orth_normalise = orth2 / np.sqrt(orth_x2**2 + orth_y2**2)
    
    liste_points_gauche = np.stack((x- rayon_circuit*orth_normalise[0], y - rayon_circuit*orth_normalise[1]))
    liste_points_droite = np.stack((x+ rayon_circuit*orth_normalise[0], y + rayon_circuit*orth_normalise[1]))
    
    L=np.asarray((x,y))
    points_gauche_valides=checkpoint.points_gardes_ckpt(L, liste_points_gauche, rayon_circuit)
    points_droite_valides=checkpoint.points_gardes_ckpt(L, liste_points_droite, rayon_circuit)
    
    
    ###TRAJECTOIRE###
    
    D=np.transpose(points_droite_valides)
    G=np.transpose(points_gauche_valides)
    
    G[0] = (G[0]+D[0])/2
    D[0] = G[0]
    
    results= scipy.optimize.least_squares(trajectoire.calcul_f, np.repeat(1/2,len(G)), bounds=(0,1), args=(D, G))
    t=results.x
    
    #renvoie un result: object contenant t + valeur atteinte en t et autre parties de l'optimisation
    #point de depart t=1/2, attention t entre 0 et 1 (argument bounds)
    
    P= D+np.reshape(t,(len(t),1))*(G-D)
    
    lt=(liste_gauche_triee,liste_droite_triee)
    pv=(points_droite_valides, points_gauche_valides)
    ckp=(x,y)
    
    affichage.affichage(pos, lt, ckp, pv, P, scp, scpline, sv)



if __name__=="__main__":
    parser=argparse.ArgumentParser(description= 'trajectoire optimisee')
    parser.add_argument('traj', type=str, choices=["sinus", "chicane"], help='Nom de la trajectoire définissant la course')
    parser.add_argument('-N', '--checkpoints', type=int, help='Nombre de checkpoint')
    parser.add_argument('-xd', '--xdepart', type=float, help='point de départ du circuit')
    parser.add_argument('-xf', '--xfinal',type=float, help='point arrivée du circuit')
    parser.add_argument('-r', '--rayon', type=float, help='largeur du circuit')
    parser.add_argument('-scp', '--show_checkpoints', action='store_true', default = False)
    parser.add_argument('-scpline', '--show_checkpoints_trace', action='store_true', default = False)
    parser.add_argument('-sv', '--show_voiture', action='store_true', default = False)
    args= parser.parse_args()
    main(args.checkpoints, args.rayon, args.xdepart, args.xfinal, args.traj, args.show_checkpoints, args.show_checkpoints_trace, args.show_voiture)
