from cv2 import cv2 
import numpy as np #matrices 

def ordenar_puntos(puntos):
    n_puntos = np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    y_order = sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    x1_order = y_order[:2]
    # = sorted.(x1_order,k)
