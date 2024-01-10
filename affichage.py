import matplotlib.pyplot as plt 
import circuit 
import checkpoint

#circuit
plt.plot(circuit.pos[0], circuit.pos[1], 'b--')
plt.gca().set_aspect('equal')
plt.plot(circuit.liste_gauche_triee[0], circuit.liste_gauche_triee[1])
plt.plot(circuit.liste_droite_triee[0], circuit.liste_droite_triee[1])



#checkpoints
plt.scatter(checkpoint.x, checkpoint.y)
plt.scatter(checkpoint.liste_points_droite[0], checkpoint.liste_points_droite[1])
plt.scatter(checkpoint.liste_points_gauche[0], checkpoint.liste_points_gauche[1])

#Relier les checkpoints
plt.plot((checkpoint.liste_points_gauche[0],checkpoint.liste_points_droite[0]),(checkpoint.liste_points_gauche[1],checkpoint.liste_points_droite[1]))
plt.show()
