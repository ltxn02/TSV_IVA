# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Memoria: codigo de la pregunta 1

# AUTORA: Lidia Martín Terés

import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

from p1_utils import visualizar_fusion, visualizar_gaus_piramide, visualizar_lapl_piramide
from pathlib import Path
import p1_tarea4
import p1_tarea3

# =========================================================
#  HELPERS
# =========================================================
def leer_imagen_cv2(path, flags):
    """Lee una imagen desde una ruta de Windows con caracteres Unicode."""
    data = np.fromfile(str(path), dtype=np.uint8)
    img = cv2.imdecode(data, flags)

    if img is None:
        raise ValueError(f"No se pudo decodificar la imagen: {path}")

    return img

def mostrar_resultados(name_A, name_B, imgA, imgB, img_fus, Gpyr_mask, Lpyr_fus_channels):
    """Muestra imágenes y pirámides de un caso de fusión RGB."""

    channel_names = ["R", "G", "B"]
    
    # =====================================================
    # Figura 1: imágenes principales
    # =====================================================
    fig1, axes1 = plt.subplots(nrows=1, ncols=4, figsize=(16, 5))
    fig1.canvas.manager.set_window_title(f"Fusión RGB: {name_A} + {name_B}")

    axes1[0].imshow(imgA)
    axes1[0].set_title("Imagen A")
    axes1[0].axis("off")

    axes1[1].imshow(imgB)
    axes1[1].set_title("Imagen B")
    axes1[1].axis("off")
    
    axes1[2].imshow(mask, cmap="gray")
    axes1[2].set_title("Máscara")
    axes1[2].axis("off")

    axes1[3].imshow(img_fus)
    axes1[3].set_title("Imagen fusionada")
    axes1[3].axis("off")
    
    fig1.tight_layout()

    # =====================================================
    # Figura 2: pirámides representativas
    # =====================================================
    fig2, axes2 = plt.subplots(nrows=1, ncols=4, figsize=(16, 10))
    fig2.canvas.manager.set_window_title(f"Pirámides de fusión: {name_A} + {name_B}")
    
    # Pirámide Gaussiana de la máscara
    gauss_mask = visualizar_gaus_piramide(Gpyr_mask)
    
    axes2[0].imshow(gauss_mask, cmap="gray")
    axes2[0].set_title("Pirámide Gaussiana\nmáscara")
    axes2[0].axis("off")
    
    # Pirámides Laplacianas fusionadas de R, G, B
    for canal, name_channel in enumerate(channel_names):
        lapl_fus = visualizar_lapl_piramide(Lpyr_fus_channels[canal])
        
        axes2[canal+1].imshow(lapl_fus)
        axes2[canal+1].set_title(f"Pirámide Laplaciana fusionada\ncanal {name_channel}")
        axes2[canal+1].axis("off")

    fig2.tight_layout()
    
    # Mostrar todas las figuras de una única vez
    plt.show()

# ========================================================

def run_fusion_rgb(imgA, imgB, mask, niveles):
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

    if imgA.ndim != 3 or imgA.shape[2] != 3:
        raise ValueError("imgA debe ser una imagen RGB")

    if imgB.ndim != 3 or imgB.shape[2] != 3:
        raise ValueError("imgB debe ser una imagen RGB")

    # Convertir a float y normalizar a [0, 1]
    imgA = imgA.astype(float) / 255.0
    imgB = imgB.astype(float) / 255.0
    mask = mask.astype(float) / 255.0

    # Listas para almacenar los resultados de los tres canales
    channel_fus = []

    Gpyr_A_channels = []
    Gpyr_B_channels = []
    Gpyr_mask = None

    Lpyr_A_channels = []
    Lpyr_B_channels = []
    Lpyr_fus_channels = []

    for canal in range(3):
        # Cada canal es ahora una imagen 2D
        channel_A = imgA[:, :, canal]
        channel_B = imgB[:, :, canal]

        # Utilizar la función desarrollada en la tarea 4
        (   Gpyr_A, Gpyr_B, Gpyr_mask_actual,
            Lpyr_A, Lpyr_B, Lpyr_fus, channel_rec
        ) = p1_tarea4.run_fusion(channel_A, channel_B, mask, niveles)

        # La pirámide de la máscara es la misma para los tres canales. Solo es necesario una copia
        if Gpyr_mask is None:
            Gpyr_mask = Gpyr_mask_actual
        
        # Guardar pirámides
        Gpyr_A_channels.append(Gpyr_A)
        Gpyr_B_channels.append(Gpyr_B)

        Lpyr_A_channels.append(Lpyr_A)
        Lpyr_B_channels.append(Lpyr_B)
        Lpyr_fus_channels.append(Lpyr_fus)

        # Reconstruir este canal
        channel_fus.append(channel_rec)

    # Reunir los canales R, G y B
    img_fus = np.stack(channel_fus, axis=2)

    # Limitar la imagen final a [0, 1]
    img_fus = np.clip(img_fus, 0.0, 1.0)
    img_fus = img_fus.astype(float)

    return (
        img_fus, Gpyr_A_channels, Gpyr_B_channels, Gpyr_mask,
        Lpyr_A_channels, Lpyr_B_channels, Lpyr_fus_channels
    )


if __name__ == "__main__":
    path_img = Path(__file__).resolve().parent / "img"

    config = {
        "orchid_mask.jpg": (
            "orchid.jpg",
            "violet.jpg"
        ),
        "mask_apple1_orange1.jpg": (
            "apple1.jpg",
            "orange1.jpg"
        ),
        "mask_apple2_orange2.jpg": (
            "apple2.jpg",
            "orange2.jpg"
        )
    }

    niveles = 4

    for name_mask, names_images in config.items():
        name_A, name_B = names_images

        path_A = path_img / name_A
        path_B = path_img / name_B
        path_mask = path_img / name_mask

        print(f"Procesando caso: {name_A} + {name_B}")

        # Leer imágenes
        imgA = leer_imagen_cv2(path_A, cv2.IMREAD_COLOR)
        imgB = leer_imagen_cv2(path_B, cv2.IMREAD_COLOR)
        mask = leer_imagen_cv2(path_mask, cv2.IMREAD_GRAYSCALE)

        # OpenCV lee en BGR; convertir a RGB
        imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
        imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)

        # Ejecutar la fusión
        (   img_fus, Gpyr_A_channels, Gpyr_B_channels, Gpyr_mask, 
            Lpyr_A_channels, Lpyr_B_channels, Lpyr_fus_channels
        ) = run_fusion_rgb(imgA, imgB, mask, niveles)

        # Mostrar todo el caso en una ventana
        mostrar_resultados(name_A, name_B, imgA, imgB, img_fus, Gpyr_mask, Lpyr_fus_channels)