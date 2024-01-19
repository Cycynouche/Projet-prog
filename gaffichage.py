import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D # à utiliser pour faire tourner la voiture
import numpy as np


def affichage(pos, lt, ckp, pv, P, scp, scpline, sv):
    fig, ax = plt.subplots()
    plt.plot(pos[0], pos[1], 'b--')
    ax.set_aspect('equal')

    ax.plot(lt[0][0], lt[0][1], color='orange')
    ax.plot(lt[1][0], lt[1][1], color='orange')

    if scp:
        #checkpoints au centre
        ax.scatter(ckp[0], ckp[1])
    
        #checkpoints à droite
        ax.scatter(pv[1][0], pv[1][1])
        
        #checkpoints à gauche
        ax.scatter(pv[0][0], pv[0][1], color='orange')

    if scpline:
        #tracé checkpoints
        ax.plot((pv[0][0],pv[1][0]),(pv[0][1],pv[1][1]))
        
    if sv:
        #tracé de voiture
        # Charger une image de voiture
        chemin_image_voiture = r"/media/vuattocy/3E25-25D2/voiture.png"
        image_voiture = plt.imread(chemin_image_voiture) #pour lire une image à partir d'un fichier et la charger en tant qu'objet NumPy array

        # Définir la position et l'orientation initiales de la voiture
        position_initiale = [P[0,0], P[0,1]]
        orientation_initiale = np.pi/4  # Angle initial en radians (0 signifie que la voiture est alignée avec l'axe x)

        # Afficher l'image sur le graphique
        image_offset = OffsetImage(image_voiture, zoom=0.2) #pour représenter une image dans un graphique

        # Créer une transformation affine pour la rotation de l'image
        transformation_affine = Affine2D().rotate(orientation_initiale)
        image_offset.set_transform(transformation_affine + ax.transData)

        ab = AnnotationBbox(image_offset, position_initiale, frameon=False, pad=0) #pour créer une boîte d'annotation contenant un objet (ici OffsetImage)

        ax.add_artist(ab)

        # Fonction pour mettre à jour la position de la voiture à chaque étape de l'animation
        def changmt_position(i):
            nouvelle_position = [P[i,0], P[i,1]]
            orientation = np.degrees(np.arctan2(P[i, 1] - P[i - 1, 1], P[i, 0] - P[i - 1, 0]))
            ab.xybox = nouvelle_position
            ab.xy = nouvelle_position
         # Mettre à jour l'orientation de la voiture
            transformation_affine = Affine2D().rotate(orientation)
            image_offset.set_transform(transformation_affine + ax.transData)
            return ab

        # Créer l'animation
        animation = FuncAnimation(fig, changmt_position, frames=range(len(P)))
               


    #tracé trajectoire
    ax.plot(P[:,0], P[:,1], color='b')
    plt.title("Trajectoire optimisée d'une course automobile")

    plt.show()
