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

#affichage voiture
voiture.ax.add_artist(voiture.ab)

plt.show()
