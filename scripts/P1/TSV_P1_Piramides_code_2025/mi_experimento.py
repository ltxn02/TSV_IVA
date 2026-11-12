from p1_pregunta_01 import leer_imagen_cv2, run_fusion_rgb
import numpy as np
import cv2
from pathlib import Path
import matplotlib.pyplot as plt

if __name__ == "__main__":
    path_img = Path(__file__).resolve().parent / "img"
    
    niveles = 4
    name_imgA = "apple2.jpg"
    name_imgB = "orange2.jpg"
    name_mask = "mask_apple2_orange2.jpg"
    
    imgA = leer_imagen_cv2(path_img / name_imgA, cv2.IMREAD_COLOR)
    imgB = leer_imagen_cv2(path_img / name_imgB, cv2.IMREAD_COLOR)
    mask = leer_imagen_cv2(path_img / name_mask, cv2.IMREAD_GRAYSCALE)
    
    imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
    imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)
    
    img_fus = run_fusion_rgb(imgA, imgB, mask, niveles)
    plt.imshow(img_fus)
    plt.show()
    
    print("Imagen A: " + str(imgA.shape))
    print("Imagen B: " + str(imgB.shape))
    print("Imagen fusionada: " + str(img_fus.shape))
    print("Tipo de dato: " + img_fus.dtype())
    print("Número niveles: " + niveles)