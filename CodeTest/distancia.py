# Abrir pantalla de cámara
# Librerías principales
import math
import sys
import os
from os import scandir, getcwd
# Librería cámara
import cv2 as cv
import time
import numpy as np

# distancias = [][]

def distancia(imagen, imagenComp):
#imagen para comparar
    im1 = cv.imread("Images/PreImages/"+ imagenComp, cv.IMREAD_UNCHANGED)
    # im2 = cv.imread("Images/PreImages/"+ "B_2" +
    #                     ".jpg", cv.IMREAD_UNCHANGED)
    # im3 = cv.imread("Images/PreImages/"+ "B_3" +
    #                     ".jpg", cv.IMREAD_UNCHANGED)
    # im4 = cv.imread("Images/PreImages/"+ "B_4" +
    #                     ".jpg", cv.IMREAD_UNCHANGED)
    # im5 = cv.imread("Images/PreImages/"+ "B_5" +
    #                     ".jpg", cv.IMREAD_UNCHANGED)

    m1 = cv.matchShapes(imagen,im1,cv.CONTOURS_MATCH_I2,0)
    # m2 = cv.matchShapes(imagen,im2,cv.CONTOURS_MATCH_I2,0)
    # m3 = cv.matchShapes(imagen,im3,cv.CONTOURS_MATCH_I2,0)
    # m4 = cv.matchShapes(imagen,im4,cv.CONTOURS_MATCH_I2,0)
    # m5 = cv.matchShapes(imagen,im5,cv.CONTOURS_MATCH_I2,0)
    
    # distancias = [imagenComp][]
    # print("Distancia entre:")

    # print("{}".format(m1) + ",")
    print((m1),end=',')
    # print("\nImagen con imagen 2: {}".format(m2))
    # print("\nImagen con imagen 3: {}".format(m3))
    # print("\nImagen con imagen 4: {}".format(m4))
    # print("\nImagen con imagen 5: {}".format(m5))
 
 # Adquisición de imagen (1)
# imagen = cv.imread("Images/PreImages/"+ "A_1" +
#                         ".jpg", cv.IMREAD_UNCHANGED)

def ls(ruta='Images/PreImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# Distancias
img = "O_3"
imagen = cv.imread("Images/PreImages/"+ img +
                        ".jpg", cv.IMREAD_UNCHANGED)

print(img)
for original in ls():
        imagen = cv.imread("Images/PreImages/"+ img +
                        ".jpg", cv.IMREAD_UNCHANGED)
        x = original.split(".")
        nombre = x[0]
        formato = x[1]
        # if(nombre.endswith("_5")):
        imagenComp = nombre + "." + formato
        #print(imagenComp)
        distancia(imagen, imagenComp)