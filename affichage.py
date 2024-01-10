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
plt.scatter(checkpoint.points_droite_valides[0], checkpoint.points_droite_valides[1])
plt.scatter(checkpoint.points_gauche_valides[0], checkpoint.points_gauche_valides[1])
plt.plot((checkpoint.points_gauche_valides[0],checkpoint.points_droite_valides[0]),(checkpoint.points_gauche_valides[1],checkpoint.points_droite_valides[1]))

plt.show()
