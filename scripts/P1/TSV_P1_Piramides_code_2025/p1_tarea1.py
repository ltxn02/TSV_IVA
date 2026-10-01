# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 1: metodos reduce y expand

# AUTORA: Lidia Martín Terés
import numpy as np
import scipy.signal

from p1_tests import test_p1_tarea1
from p1_utils import generar_kernel_suavizado

def reduce(imagen):
    """  
    # Esta funcion implementa la operacion "reduce" sobre una imagen
    # 
    # Argumentos de entrada:
    #    imagen: numpy array de tamaño [imagen_height, imagen_width].
    # 
    # Devuelve:
    #    output: numpy array de tamaño [imagen_height/2, imagen_width/2] (output).
    #
    # NOTA: si imagen_height/2 o imagen_width/2 no son numeros enteros, 
    #        entonces se redondea al entero mas cercano por arriba 
    #        Por ejemplo, si la imagen es 5x7, la salida sera 3x4  
    """   
    output = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)

    # 1. Crea el kernel de suavizado con a = 0.4
    kernel = generar_kernel_suavizado(0.4)
    
    # 2. Convoluciona la imagen con el kernel, manteniendo las dimensiones de la imagen
    img_suavizada = scipy.signal.convolve2d(imagen, kernel, 'same')
    
    # 3. Muestrea la imagen por 2 en ambas direcciones (resulta en una imagen más pequeña)
    output = img_suavizada[::2, ::2]
   
    return output  

def expand(imagen):
    """  
    # Esta funcion implementa la operacion "expand" sobre una imagen
    # 
    # Argumentos de entrada:
    #    imagen: numpy array de tamaño [imagen_height, imagen_width].
    #     
    # Devuelve:
    #    output: numpy array de tamaño [imagen_height*2, imagen_width*2].
    """ 
    output = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)

    # 1. Define una imagen completamente negra del tamaño expandido
    alto, ancho = imagen.shape
    img_expandida = np.zeros((alto*2, ancho*2), dtype=float)
    
    # 2. Coloca la imagen original en las posiciones pares
    img_expandida[::2, ::2] = imagen
    
    # 3. Crea el kernel de suavizado con a = 0.4
    kernel = generar_kernel_suavizado(0.4)
    
    # 4. Convoluciona la imagen con el kernel, manteniendo las dimensiones de la imagen
    img_suavizada = scipy.signal.convolve2d(img_expandida, kernel, 'same')
    
    # 5. Multiplica por 4 para mantener el rango
    #       Este paso se hace para evitar que los colores queden artificialmente oscurecidos
    #       al haberlos suavizado con píxeles de valor 0.
    output = 4 * img_suavizada

    return output

if __name__ == "__main__":    
    print("Practica 1 - Tarea 1 - Test autoevaluación\n")                
    print("Tests completados = " + str(test_p1_tarea1())) 