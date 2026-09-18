# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Práctica 0: Introducción a Python
# AUTORA: Lidia Martín Terés
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

print("Práctica 0 - Tarea 6\n")

# 1. Lista vacía
lista_img = []

# 2. Leer astronaut y añadirla a la lista. Identifica si es a color o en escala de grises
astronaut = data.astronaut()
lista_img.append(astronaut)

print("Astronaut: ")
if len(astronaut.shape) == 2:
    print("- Imagen en escala de grises\n")
else:
    print("- Imagen a color\n")
    
# 3. Leer camera y añadirla a la lista. Identifica si es a color o en escala de grises
camera = data.camera()
lista_img.append(camera)

print("Camera: ")
if len(camera.shape) == 2:
    print("- Imagen en escala de grises\n")
else:
    print("- Imagen a color\n")
    
# 4. Array bidimensional 10x10 de ceros y añadirlo a la lista. Identifica si es a color o en escala de grises
matrix = np.zeros((10, 10))
lista_img.append(matrix)

print("Matrix: ")
if len(matrix.shape) == 2:
    print("- Imagen en escala de grises\n")
else:
    print("- Imagen a color\n")
    
# 5. Recorra la lista mediante un bucle. Muestre dimensiones, tipo y máximo. Visualice la imagen.
for i in range(len(lista_img)):
    img = lista_img[i]
    
    print("Elemento ", i)
    print("- Dimensiones: ", img.shape)
    print("- Tipo: ", img.dtype)
    print("- Valor máximo: ", img.max(), "\n")
    
    plt.imshow(img)
    plt.show()
    
# 6. Nueva lista con los dos primeros elementos de lista_img
nueva_lista = lista_img[:2]
print("Número de elementos de la nueva lista: ", len(nueva_lista))