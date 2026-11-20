# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 2: Extraccion, descripcion y correspondencia de caracteristicas locales
# Tarea 2: Descripcion de puntos de interes mediante histogramas.

# AUTORA: Lidia Martín Terés

# librerias y paquetes por defecto
import numpy as np
from p2_tests import test_p2_tarea2

# Incluya aqui las librerias que necesite en su codigo
import scipy

def descripcion_puntos_interes(imagen, coords_esquinas, vtam = 8, nbins = 16, tipoDesc='hist', umbral_mag=0.05):
    """
    # Esta funcion describe puntos de interes de una imagen mediante histogramas, analizando 
    # vecindarios con dimensiones "vtam+1"x"vtam+1" centrados en las coordenadas de cada punto de interes
    #   
    # La descripcion obtenida depende del parametro 'tipoDesc'
    #   - Caso 'hist': histograma normalizado de valores de gris 
    #   - Caso 'mag-ori': histograma de orientaciones de gradiente
    #
    # En el caso de que existan puntos de interes en los bordes de la imagen, el descriptor no
    # se calcula y el punto de interes se elimina de la lista <new_coords_esquinas> que devuelve
    # esta funcion. Esta lista indica los puntos de interes para los cuales existe descriptor.
    #
    # Argumentos de entrada:
    #   - imagen: numpy array con dimensiones [imagen_height, imagen_width].        
    #   - coords_esquinas: numpy array con dimensiones [num_puntos_interes, 2] con las coordenadas 
    #                      de los puntos de interes detectados en la imagen. Tipo int64
    #                      Cada punto de interes se encuentra en el formato [fila, columna]
    #   - vtam: valor de tipo entero que indica el tamaño del vecindario a considerar para
    #           calcular el descriptor correspondiente.
    #   - nbins: valor de tipo entero que indica el numero de niveles que tiene el histograma 
    #           para calcular el descriptor correspondiente.
    #   - tipoDesc: cadena de caracteres que indica el tipo de descriptor calculado
    #
    # Argumentos de salida
    #   - descriptores: numpy array con dimensiones [num_puntos_interes, nbins] con los descriptores 
    #                   de cada punto de interes (i.e. histograma de niveles de gris)
    #   - new_coords_esquinas: numpy array con dimensiones [num_puntos_interes, 2], solamente con las coordenadas 
    #                      de los puntos de interes descritos. Tipo int64  <class 'numpy.ndarray'>
    #
    # NOTA: no modificar los valores por defecto de las variables de entrada vtam y nbins, 
    #       pues se utilizan para verificar el correcto funciomaniento de esta funcion
    """
    # Iniciamos variables de salida
    descriptores = np.empty(shape=[0,nbins], dtype=float) # iniciamos la variable de salida (numpy array)
    new_coords_esquinas = np.empty(shape=[0,2], dtype=int) # iniciamos la variable de salida (numpy array)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 1. Convertir la imagen a float y normalizar la imagen  
    # ----------------------------------------------------------------------------------------------------------------------------------------
    imagen = imagen.astype(float)
    
    if imagen.max() > 1.0:
        imagen = imagen / 255.0
    
    # Definir el tamaño del vecindario (para vtam=8, será de 9x9)
    mitad = vtam // 2
    
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 2. Calcular magnitud y orientación del gradiente (solo necesario para el descriptor 'mag-ori')
    # ----------------------------------------------------------------------------------------------------------------------------------------
    if tipoDesc == 'mag-ori':
        grad_x = scipy.ndimage.sobel(imagen, axis=1)
        grad_y = scipy.ndimage.sobel(imagen, axis=0)
        
        # Magnitud del gradiente
        magnitud = np.sqrt(grad_x ** 2 + grad_y ** 2)
        
        # Orientación del gradiente en radianes (pasado a grados)
        orientacion = np.arctan2(grad_y, grad_x)
        
        orientacion = np.rad2deg(orientacion)
        orientacion = orientacion % 360.0       # Pasar ángulos negativos a [0, 360)
        
        # Crear nbins intervalos homogéneos (nbins+1 límites para nbins intervalos)
        niveles = np.linspace(
            0.0,
            360.0,
            nbins + 1
        )
        
        # Ventana espacial gaussiana 2D de tamaño (vtam+1)x(vtam+1) centrada en la esquina
        ventana_gauss = np.zeros((vtam + 1, vtam + 1), dtype=float)
        ventana_gauss[mitad, mitad] = 1.0
        ventana_gauss = scipy.ndimage.gaussian_filter(ventana_gauss, sigma=vtam / 2.0)
    
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 3. Recorrer todos los puntos de interés recibidos
    # ----------------------------------------------------------------------------------------------------------------------------------------
    for coordenada in coords_esquinas:
        fila = int(coordenada[0])
        columna = int(coordenada[1])
        
        # i) Cálculo de los límites del vecindario alrededor del punto
        fila_inicio = fila - mitad
        fila_fin = fila + mitad + 1
        
        columna_inicio = columna - mitad
        columna_fin = columna + mitad + 1
        
        # ------------------------------------------------------------------------------------------------------------------------------------
        # 4. Comprobar que el vecindario está dentro de los límites de la imagen
        # ------------------------------------------------------------------------------------------------------------------------------------
        if (
            fila_inicio < 0
            or fila_fin > imagen.shape[0]
            or columna_inicio < 0
            or columna_fin > imagen.shape[1]
        ):
            continue    # Se descarta por estar demasiado cerca del borde, por lo que no se puede calcular su vecindario
        
        # ------------------------------------------------------------------------------------------------------------------------------------
        # 5. Extraer el vecindario centrado en el punto
        # ------------------------------------------------------------------------------------------------------------------------------------
        if tipoDesc == 'hist':
            # Extraer el vecindario de niveles de gris
            vecindario = imagen[
                fila_inicio : fila_fin,
                columna_inicio : columna_fin
            ]
        
            # i) Convertir la matriz 2D a vector 1D
            # ----------------------------------------
            valores = vecindario.flatten()
        
            # ii) Cálculo del histograma, dividiendo el rango [0, 1] en nbins intervalos iguales
            # ----------------------------------------
            histograma, _ = np.histogram(
                valores,
                bins=nbins,
                range=(0.0, 1.0)
            )
        
            # iii) Convertir el histograma a float y normalizarlo para que la suma de todos sus elementos sea 1
            # ----------------------------------------
            histograma = histograma.astype(float)
            histograma = histograma/histograma.sum()
        
            # iv) Guardar el descriptor y las coordenadas
            # ----------------------------------------
            descriptores = np.vstack((descriptores, histograma))
            new_coords_esquinas = np.vstack((new_coords_esquinas, [fila, columna]))
        
        # ----------------------------------------------------------------------------------------------------------------------------------------
        # 6. Descriptor de magnitud y orientación
        # ----------------------------------------------------------------------------------------------------------------------------------------
        elif tipoDesc == 'mag-ori':
            # Extraer las orientaciones del vecindario
            vecindario_orientacion = orientacion[
                fila_inicio : fila_fin,
                columna_inicio : columna_fin
            ]
            
            # Extraer las magnitudes del vecindario
            vecindario_magnitud = magnitud[
                fila_inicio : fila_fin,
                columna_inicio : columna_fin
            ]
            
            # i) Aplanar ambos vecindarios para procesarlos como vectores
            # ----------------------------------------
            orientaciones = vecindario_orientacion.flatten()
            magnitudes_orig = vecindario_magnitud.flatten()
            magnitudes_pond = (vecindario_magnitud * ventana_gauss).flatten()
            
            # ii) Asignar cada orientación a un intervalo (np.digitize devuelve índices empezando por 1, por eso se resta 1)
            # ----------------------------------------
            mascara = magnitudes_orig >= umbral_mag
            orientaciones_filtradas = orientaciones[mascara]
            pesos_filtrados = magnitudes_pond[mascara]

            histograma, _ = np.histogram(
                orientaciones_filtradas,
                bins=niveles,
                weights=pesos_filtrados
            )
            
            histograma = histograma.astype(float)
            
            # iv) Normalización L2 segura (evitando división por cero -> NaN)
            norma_l2 = np.linalg.norm(histograma)
            if norma_l2 > 0:
                histograma = histograma / norma_l2
            
            # v) Guardar el descriptor y las coordenadas
            # ----------------------------------------
            descriptores = np.vstack((descriptores, histograma))
            new_coords_esquinas = np.vstack((new_coords_esquinas, [fila, columna]))
        
        else:
            raise ValueError("tipoDesc debe ser 'hist' o 'mag-ori'")

    return descriptores, new_coords_esquinas

if __name__ == "__main__":    
    print("Practica 2 - Tarea 2 - Test autoevaluación\n")                

    ## tests descriptor tipo 'hist' (tarea 2a)
    print("Tests completados = " + str(test_p2_tarea2(disptime=-1,stop_at_error=False,debug=False,tipoDesc='hist'))) #analizar todas las imagenes y esquinas del test
    print("Tests completados = " + str(test_p2_tarea2(disptime=1,stop_at_error=False,debug=False,tipoDesc='hist'))) #analizar todas las imagenes y esquinas del test, mostrar imagenes con resultados (1 segundo)
    print("Tests completados = " + str(test_p2_tarea2(disptime=-1,stop_at_error=True,debug=True,tipoDesc='hist'))) #analizar todas las imagenes y esquinas del test, pararse en errores y mostrar datos
    print("Tests completados = " + str(test_p2_tarea2(disptime=-1,stop_at_error=True,debug=True,tipoDesc='hist',imgIdx = 3, poiIdx = 7))) #analizar solamente imagen #2 y esquina #7    

    ## tests descriptor tipo 'mag-ori' (tarea 2b)
    #print("Tests completados = " + str(test_p2_tarea2(disptime=-1,stop_at_error=False,debug=False,tipoDesc='mag-ori'))) #analizar todas las imagenes y esquinas del test
    #print("Tests completados = " + str(test_p2_tarea2(disptime=0.1,stop_at_error=False,debug=False,tipoDesc='mag-ori'))) #analizar todas las imagenes y esquinas del test, mostrar imagenes con resultados (1 segundo)
    print("Tests completados = " + str(test_p2_tarea2(disptime=-1,stop_at_error=True,debug=True,tipoDesc='mag-ori'))) #analizar todas las imagenes y esquinas del test, pararse en errores y mostrar datos
    #print("Tests completados = " + str(test_p2_tarea2(disptime=1,stop_at_error=True,debug=True,tipoDesc='mag-ori',imgIdx = 3,poiIdx = 7))) #analizar solamente imagen #1 y esquina #7       