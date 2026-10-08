# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 4: fusion de imagenes

# AUTOR1: APELLIDO1 APELLIDO1, NOMBRE1
# AUTOR2: APELLIDO2 APELLIDO2, NOMBRE2
# PAREJA/TURNO: NUMERO_PAREJA/NUMERO_TURNO

import numpy as np
import math

from p1_tests import test_p1_tarea4
from p1_utils import visualizar_fusion
from pathlib import Path
import p1_tarea1
import p1_tarea2
import p1_tarea3

def run_fusion(imgA, imgB, mask, niveles): 
    """ 
    # Esta funcion implementa la fusion de dos imagenes calculando las 
    # pirámides Laplacianas de las imagenes de entrada y la pirámide
    # Gausiana de una mascara.
    #  
    # Argumentos de entrada:
    #   imgA: numpy array de tamaño [imagen_height, imagen_width].
    #   imgB: numpy array de tamaño [imagen_height, imagen_width].
    #   mask: numpy array de tamaño [imagen_height, imagen_width].
    #
    # Devuelve:
    #   Gpyr_imgA: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la imagen A
    #   Gpyr_imgB: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la imagen B
    #   Gpyr_mask: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la máscara
    #   Lpyr_imgA: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la imagen A
    #   Lpyr_imgB: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la imagen B
    #   Lpyr_fus: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la fusion imagen A & B
    #   Lpyr_fus_rec:  numpy array de tamaño [imagen_height, imagen_width] correspondiente
    #               a la reconstruccion de la pirámide Lpyr_fus
    """ 
    
    # iniciamos las variables de salida    
    Gpyr_imgA = []      # Pirámide Gaussiana imagen A
    Gpyr_imgB = []      # Pirámide Gaussiana imagen B
    Gpyr_mask = []      # Pirámide Gaussiana máscara    
    Lpyr_imgA = []      # Pirámide Laplaciana imagen A
    Lpyr_imgB = []      # Pirámide Laplaciana imagen B
    Lpyr_fus = []       # Pirámide Laplaciana fusionada
    Lpyr_fus_rec = []   # Imagen reconstruida de la pirámide Laplaciana fusionada

    # Verificación de que las imágenes son en escala de grises
    if not (len(imgA.shape) == len(imgB.shape) == 2):
        raise ValueError("Las matrices deberían ser bidimensionales (imágenes en escala de grises)")
    
    # Conversión de imágenes y máscaras a tipo float
    # IMPORTANTE: la normalización se está llevando a cabo en las funciones de los otros .py
    imgA = imgA.astype(float)
    imgB = imgB.astype(float)
    mask = mask.astype(float)
    
    # Cálculo de las pirámides Gaussianas de las imágenes
    Gpyr_imgA = p1_tarea2.gaus_piramide(imgA, niveles)
    Gpyr_imgB = p1_tarea2.gaus_piramide(imgB, niveles)
    
    # Cálculo de las pirámides Laplacianas de las imágenes
    Lpyr_imgA = p1_tarea2.lapl_piramide(Gpyr_imgA)
    Lpyr_imgB = p1_tarea2.lapl_piramide(Gpyr_imgB)
    
    # Fusionado de las pirámides Laplacianas de las imágenes y la Gaussiana de la máscara
    Gpyr_mask = p1_tarea2.gaus_piramide(mask, niveles)
    Lpyr_fus = p1_tarea3.fusionar_lapl_pyr(Lpyr_imgA, Lpyr_imgB, Gpyr_mask)
    
    # Reconstrucción de la imagen con la pirámide resultante para obtener la imagen
    Lpyr_fus_rec = p1_tarea3.reconstruir_lapl_pyr(Lpyr_fus)
    
    # Recorta valores al intervalo [0, 1] y asegura valores en float
    Lpyr_fus_rec = np.clip(Lpyr_fus_rec, 0.0, 1.0)
    Lpyr_fus_rec = Lpyr_fus_rec.astype(float)
    
    return Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec

if __name__ == "__main__":    
    # Se espera una cadena de texto como path para imágenes
    path_imagenes = str(Path(__file__).resolve().parent / "img") + "/"
    print("Practica 1 - Tarea 4 - Test autoevaluación\n")    
    result,imgAgray,imgBgray,maskgray,\
        Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec \
            = test_p1_tarea4(path_img=path_imagenes,precision=2)
    print("Tests completado = " + str(result)) 

    if result==True:
        #visualizar piramides de la fusion (puede consultar el codigo en el fichero p1_utils.py)
        visualizar_fusion(imgAgray,imgBgray,maskgray,Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec)