# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Práctica 0: Introducción a Python
# AUTORA: Lidia Martín Terés

import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color

# 1. Leer y visualizar la imagen
img = io.imread('images/A_small_cup_of_coffee.jfif')
# La URL dada (https://bit.ly/2Zjkcm7) estaba dando problemas para la lectura de la imagen, así que se ha decidido
# descargar la imagen y leer la imagen descargada en su lugar.

plt.imshow(img)
plt.show()

# 2. Dimensiones, tipo y valor máximo de la imagen
print("Dimensiones: ", img.shape)
print("Tipo: ", img.dtype)
print("Valor máximo: ", img.max())

# 3. Pasar imagen a float y normalizar (los valores originales de la imagen estarán en [0, 255])
img = img.astype(float)/255

print("Dimensiones: ", img.shape)
print("Tipo: ", img.dtype)

# 4. Transforme la imagen a color HSV
hsv_img = color.rgb2hsv(img)

# 5. Mostrar cada canal en una ventana y mostrar una imagen en escala de grises (ventana con tres columnas y una fila)
#                                           - Formato: [alto, ancho, canal]
hue_channel = hsv_img[:, :, 0]
saturation_channel = hsv_img[:, :, 1]
value_channel = hsv_img[:, :, 2]

# Hue
plt.subplot(1, 3, 1)    # Se indica que va a ser una ventana de 1x3 y que vamos a pintar la primera columna
plt.imshow(hue_channel, cmap='gray')
plt.title('Hue')

# Saturation
plt.subplot(1, 3, 2)    # Segunda columna
plt.imshow(saturation_channel, cmap='gray')
plt.title('Saturation')

# Value
plt.subplot(1, 3, 3)    # Tercera columna
plt.imshow(value_channel, cmap='gray')
plt.title('Value')

plt.show()