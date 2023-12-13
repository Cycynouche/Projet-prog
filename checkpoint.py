import matplotlib.pyplot as plt
import Circuit

abscisse_g = Circuit.liste_gauche_triee[0]
ordonnee_g = Circuit.liste_gauche_triee[1]
abscisse_d = Circuit.liste_droite_triee[0]
ordonnee_d = Circuit.liste_droite_triee[1]

checkpoint_gauche_abscisse = abscisse_g[0: len(abscisse_g): 80]
checkpoint_gauche_ordonnee = ordonnee_g[0: len(ordonnee_g): 80]
checkpoint_droit_abscisse = abscisse_d[0: len(abscisse_d): 80]
checkpoint_droit_ordonnee = ordonnee_d[0: len(ordonnee_d): 80]
