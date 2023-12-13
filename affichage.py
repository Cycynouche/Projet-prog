import matplotlib.pyplot as plt 
import circuit 
import checkpoint

#circuit
plt.plot(circuit.pos[0], circuit.pos[1], 'b--')
plt.gca().set_aspect('equal')
plt.plot(circuit.liste_gauche_triee[0], circuit.liste_gauche_triee[1])
plt.plot(circuit.liste_droite_triee[0], circuit.liste_droite_triee[1])



#checkpoints
plt.plot(checkpoint.checkpoint_gauche_abscisse, checkpoint.checkpoint_gauche_ordonnee, 'b+' )
plt.plot(checkpoint.checkpoint_droite_abscisse, checkpoint.checkpoint_droite_ordonnee, 'r+' )
plt.show()
