# Tratamiento de Señales Visuales/Introducción a la Visión Artificial @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Memoria: codigo de la pregunta 2

# AUTORA: Lidia Martín Terés

import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from p1_pregunta_01 import (leer_imagen_cv2, run_fusion_rgb)


if __name__ == "__main__":
    path_img = Path(__file__).resolve().parent / "img"

    data = {
        "orchid-violet": (
            "orchid.jpg",
            "violet.jpg",
            "orchid_mask.jpg"
        ),
        "apple-orange": (
            "apple1.jpg",
            "orange1.jpg",
            "mask_apple1_orange1.jpg"
        )
    }

    niveles_exp = [1, 2, 3, 4, 5]

    for name_case, name_files in data.items():
        name_A, name_B, name_mask = name_files

        path_A = path_img / name_A
        path_B = path_img / name_B
        path_mask = path_img / name_mask

        imgA = leer_imagen_cv2(path_A, cv2.IMREAD_COLOR)
        imgB = leer_imagen_cv2(path_B, cv2.IMREAD_COLOR)
        mask = leer_imagen_cv2(path_mask, cv2.IMREAD_GRAYSCALE)

        # OpenCV carga en BGR
        imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
        imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)

        fig, axes = plt.subplots(2,3,figsize=(15, 9))
        fig.canvas.manager.set_window_title(f"Experimento niveles: {name_case}")

        axes = axes.ravel()

        for i, niveles in enumerate(niveles_exp):
            (   img_fus, Gpyr_A_channels, Gpyr_B_channels, Gpyr_mask,
                Lpyr_A_channels, Lpyr_B_channels, Lpyr_fus_channels
            ) = run_fusion_rgb(imgA, imgB, mask, niveles)

            axes[i].imshow(img_fus)
            axes[i].set_title(f"Niveles = {niveles}")
            axes[i].axis("off")

        # Ocultar posibles subplots sobrantes
        for i in range(len(niveles_exp), len(axes)):
            axes[i].axis("off")

        fig.tight_layout()
        fig.savefig(f"experimento_niveles_{name_case}.png", dpi=300, bbox_inches="tight")

        plt.show()