# Librerias
# OpenCV
import cv2 as cv
# import numpy as np
from skimage import io
from skimage import filters
# Operaciones de logaritmo
from math import copysign, log10
# Excel
# import pandas as pd
# from pandas import ExcelWriter
# Ruta
from os import scandir, getcwd


# Momentos de Hu (2.1)
def momentos(imagen, nombre):
    
    mostrarMomentos = True
    moments = cv.moments(imagen)
    huMoments = cv.HuMoments(moments)

    print("\n" + nombre + ":\n")
    for i in range(0, 7):
        if mostrarMomentos:
            # print("H"+i+":")
            print(-1*copysign(1.0,
                               huMoments[i])*log10(abs(huMoments[i])),
                  end=',')
            # print(huMoments[i])
        else:
            print("{:.5f}".format(huMoments[i]), end='\n')

def ls(ruta='Images/PreImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# Adquisición de imagen (1)
for nombre in ls():

    imagen = cv.imread("Images/PreImages/" + nombre, cv.IMREAD_UNCHANGED)

    momentos(imagen, nombre)

    # imagen = cv.imread("Images/PreImages/" + "A_1" +
    #                 ".jpg", cv.IMREAD_UNCHANGED)
    