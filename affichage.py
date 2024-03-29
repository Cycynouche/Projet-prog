import matplotlib.pyplot as plt 
import circuit 
import checkpoint
import trajectoire

#circuit
plt.plot(circuit.pos[0], circuit.pos[1], 'b--')
plt.gca().set_aspect('equal')
plt.plot(circuit.liste_gauche_triee[0], circuit.liste_gauche_triee[1])
plt.plot(circuit.liste_droite_triee[0], circuit.liste_droite_triee[1])



#checkpoints au centre
#plt.scatter(checkpoint.x, checkpoint.y)

#checkpoints à droite
#plt.scatter(checkpoint.points_droite_valides[0], checkpoint.points_droite_valides[1])
#checkpoints à gauche
#plt.scatter(checkpoint.points_gauche_valides[0], checkpoint.points_gauche_valides[1])

#tracé checkpoints
#plt.plot((checkpoint.points_gauche_valides[0],checkpoint.points_droite_valides[0]),(checkpoint.points_gauche_valides[1],checkpoint.points_droite_valides[1]))

#tracé trajectoire
plt.plot(trajectoire.P[:,0], trajectoire.P[:,1], color='b')

voiture.ax.add_artist(voiture.ab)

# Créer l'animation
animation = FuncAnimation(voiture.fig, voiture.changmt_position, frames=len(voiture.trajectoire.P[:,0]), interval=100, blit=True)

plt.show()


###NINA

import matplotlib.pyplot as plt 
import circuit 
import checkpoint
import trajectoire

def affichage(scp1=False, scp2=False):
    #circuit
    plt.plot(circuit.pos[0], circuit.pos[1], 'b--')
    plt.gca().set_aspect('equal')
    plt.plot(circuit.liste_gauche_triee[0], circuit.liste_gauche_triee[1])
    plt.plot(circuit.liste_droite_triee[0], circuit.liste_droite_triee[1])
    if scp1:
        #checkpoints au centre
        plt.scatter(checkpoint.x, checkpoint.y)
    
        #checkpoints à droite
        plt.scatter(checkpoint.points_droite_valides[0], checkpoint.points_droite_valides[1])
        #checkpoints à gauche
        plt.scatter(checkpoint.points_gauche_valides[0], checkpoint.points_gauche_valides[1])
    
    if scp2:
        #tracé checkpoints
        plt.plot((checkpoint.points_gauche_valides[0],checkpoint.points_droite_valides[0]),(checkpoint.points_gauche_valides[1],checkpoint.points_droite_valides[1]))

    #tracé trajectoire
    plt.plot(trajectoire.P[:,0], trajectoire.P[:,1])

    plt.show()

