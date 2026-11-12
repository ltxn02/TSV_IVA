# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 2: Extraccion, descripcion y correspondencia de caracteristicas locales
# Tarea 1: Deteccion de puntos de interes con Harris corner detector.

# AUTORA: Lidia Martín Terés

# librerias y paquetes por defecto
import numpy as np
from p2_tests import test_p2_tarea1

# Incluya aqui las librerias que necesite en su codigo
import scipy
import skimage

def detectar_puntos_interes_harris(imagen, sigma = 1.0, k = 0.05, threshold_rel = 0.2):
    """
    # Esta funcion detecta puntos de interes en una imagen con el algoritmo de Harris.
    #
    # Argumentos de entrada:
    #   - imagen: numpy array con dimensiones [imagen_height, imagen_width].  
    #   - sigma: valor de tipo double o float que determina el factor de suavizado aplicado
    #   - k: valor de tipo double o float que determina la respuesta R de Harris
    #   - threshold_rel: valor de tipo double o float que define el umbral relativo aplicado sobre el valor maximo de R
    # Argumentos de salida
    #   - coords_esquinas: numpy array con dimensiones [num_puntos_interes, 2] con las coordenadas 
    #                      de los puntos de interes detectados en la imagen. Cada punto de interes 
    #                      se encuentra en el formato [fila, columna] de tipo int64
    #
    # NOTA: no modificar los valores por defecto de las variables de entrada sigma y k, 
    #       pues se utilizan para verificar el correcto funciomaniento de esta funcion
    """
    coords_esquinas = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)

    # 1. Convertir la imagen a float y normalizar
    # -----------------------------------------------------------------------------------------
    imagen = imagen.astype(float)/255
    
    # 2. Aplicar filtros de Sobel
    # -----------------------------------------------------------------------------------------
    #   i) Definición de filtros
    sobel_horizontal = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    sobel_vertical = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])
    
    #  ii) Aplicar filtros
    grad_horizontal = scipy.signal.convolve2d(
        imagen,
        sobel_horizontal,
        mode="same",        # Para que la salida tenga el mismo (==) tamaño que la entrada
        boundary="symm"     # Refleja la imagen en los bordes (en vez de valores negros)
    )
    
    grad_vertical = scipy.signal.convolve2d(
        imagen,
        sobel_vertical,
        mode="same",
        boundary="symm"
    )
    
    # 3. Combinar derivadas: (grad horizontal)^2, grad horizontal * grad vertical, (grad vertical)^2
    # -----------------------------------------------------------------------------------------
    Ix2 = grad_horizontal ** 2
    Iy2 = grad_vertical ** 2
    IxIy = grad_horizontal * grad_vertical
    
    # 4. Definir componentes matriz local Harris suavizándolos
    # -----------------------------------------------------------------------------------------
    Sxx = scipy.ndimage.filters.gaussian_filter(Ix2, sigma=sigma, mode="constant")
    Syy = scipy.ndimage.filters.gaussian_filter(Iy2, sigma=sigma, mode="constant")
    Sxy = scipy.ndimage.filters.gaussian_filter(IxIy, sigma=sigma, mode="constant")
    
    # 5. Calcular la respuesta de Harris (determinante y traza de la matriz junto al parámetro k)
    # -----------------------------------------------------------------------------------------
    determinante = Sxx * Syy - Sxy ** 2
    traza = Sxx + Syy
    
    respuesta_harris = determinante - k * (traza ** 2)
    
    # 6. Seleccionar máximos locales suficientemente importantes
    # -----------------------------------------------------------------------------------------
    coords_esquinas = skimage.feature.corner_peaks(
        respuesta_harris,               # Imagen obtenida por algoritmo Harris
        min_distance=5,                 # Dos máximos deben estar separados al menos 5px
        threshold_rel=threshold_rel     # Descarta píxeles con valor menor que el umbral
    )
    
    return coords_esquinas

if __name__ == "__main__":    
    print("Practica 2 - Tarea 1 - Test autoevaluación\n")                
    
    print("Tests completados = " + str(test_p2_tarea1(disptime=-1,stop_at_error=False,debug=False))) #analizar todos los casos sin pararse en errores
    print("Tests completados = " + str(test_p2_tarea1(disptime=1,stop_at_error=False,debug=False))) #analizar y visualizar todos los casos sin pararse en errores
    print("Tests completados = " + str(test_p2_tarea1(disptime=-1,stop_at_error=True,debug=False))) #analizar todos los casos y pararse en errores 
    print("Tests completados = " + str(test_p2_tarea1(disptime=-1,stop_at_error=True,debug=True))) #analizar todos los casos, pararse en errores y mostrar informacion