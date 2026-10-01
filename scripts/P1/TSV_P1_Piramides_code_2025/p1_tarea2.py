# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 2: piramide Gaussiana y piramide laplaciana

# AUTORA: Lidia Martín Terés
import numpy as np
from p1_tests import test_p1_tarea2
from p1_tarea1 import reduce, expand

def gaus_piramide(imagen, niveles):
    """ 
    # Esta funcion crea una piramide Gaussiana a partir de una imagen
    #
    # Argumentos de entrada:
    #   imagen: numpy array de tamaño [imagen_height, imagen_width].
    #   niveles: entero positivo que especifica el numero de veces que se aplica la operacion 'reduce'.
    #           Si niveles=0 entonces se debe devolver una lista con la imagen de entrada
    #           Si niveles=1 entonces se debe realizar una operacion de reduccion               
    #
    # Devuelve:
    #   gauss_pyr: lista de numpy arrays con variable tamaño con "niveles+1" elementos.
    #       output[0] es la imagen de entrada
    #       output[i] es el nivel i de la piramide
    #  
    """ 
    gaus_pyr = []  # iniciamos la variable de salida (lista)

    gaus_pyr.append(imagen)
    img_actual = imagen
    
    for _ in range(niveles):
        img_actual = reduce(img_actual)
        gaus_pyr.append(img_actual)

    return gaus_pyr

def lapl_piramide(gaus_pyr):
    """ 
    # Esta funcion crea una piramide Laplaciana a partir de una piramide Gaussiana    
    #  
    # Argumentos de entrada:
    #   gauss_pyr: lista de numpy arrays creada con la funcion 'gauss_piramide'.               
    #
    # Devuelve:
    #   lapla_pyr: lista de numpy arrays con variable tamaño con "niveles+1" elementos.    
    #       lapla_pyr[0] es el primera nivel de la piramide que contiene bordes
    #       lapla_pyr[i] es el nivel i de la piramide que contiene bordes
    #       lapla_pyr[niveles-1] es una imagen (escala de grises)    
    #
    # NOTA: algunas veces, la operacion 'expand' devuelve una imagen de tamaño mayor 
    # que el esperado. Entonces no coinciden las dimensiones de la imagen expandida 
    #   del nivel k+1 y las dimensiones del nivel k. Verifique si ocurre esta 
    #   situacion y en caso afirmativo, elimine los ultimos elementos de la 
    #   imagen expandida hasta coincidir las dimensiones del nivel k
    #   Por ejemplo, si el nivel tiene tamaño 5x7, tras aplicar 'reduce' y 'expand' 
    #   obtendremos una imagen de tamaño 6x8. En este caso, elimine la 6 fila y 8 
    #   columna para obtener una imagen de tamaño 5x7 donde pueda aplicar la resta      
    """ 
    lapl_pyr = [] # iniciamos la variable de salida (lista) 
    
    # Calcula todos los niveles que sí tienen el siguiente nivel
    for i in range(len(gaus_pyr) - 1):
        img_expandida = expand(gaus_pyr[i+1])
        
        # Puede darse que las dimensiones de la imagen expandida sean mayores que la que necesitamos,
        # así que se recorta.
        alto, ancho = gaus_pyr[i].shape
        img_expandida = img_expandida[:alto, :ancho]
        
        # Nivel Laplaciano = Nivel Gaussiano - expansión del siguiente Nivel Gaussiano
        nvl_lapl = gaus_pyr[i] - img_expandida
        lapl_pyr.append(nvl_lapl)

    lapl_pyr.append(gaus_pyr[-1])
    return lapl_pyr
   
if __name__ == "__main__":    
    print("Practica 1 - Tarea 2 - Test autoevaluación\n")                
    print("Tests completados = " + str(test_p1_tarea2())) 