import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from scipy import ndimage

# 1. Leer y visualizar la imagen
img = data.brick()

plt.imshow(img, cmap='gray')
plt.show()

# 2. Muestre las dimensiones y tipo
print("Dimensiones: ", img.shape)   # (512, 512)
print("Tipo: ", img.dtype)          # uint8

# 3. Aplicar un filtrado de Sobel horizontal y un filtrado Gaussiano con sigma = 10
img_sobel = ndimage.sobel(img, axis=1)
img_gauss = ndimage.gaussian_filter(img, sigma=10)

# 4. Visualizar imágenes
plt.imshow(img_sobel, cmap='gray')
plt.title("Sobel horizontal")
plt.show()

plt.imshow(img_gauss, cmap='gray')
plt.title("Filtro Gaussiano (sigma=10)")
plt.show()