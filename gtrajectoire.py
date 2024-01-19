import numpy as np

def calcul_f(t, D, G):
    P= D+np.reshape(t,(len(t),1))*(G-D)
    result=np.linalg.norm(P[1:]-P[:-1], axis=1)
    return result
