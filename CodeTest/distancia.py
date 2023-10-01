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

    
    # m2 = cv.matchShapes(imagen,im2,cv.CONTOURS_MATCH_I2,0)
    # m3 = cv.matchShapes(imagen,im3,cv.CONTOURS_MATCH_I2,0)
    # m4 = cv.matchShapes(imagen,im4,cv.CONTOURS_MATCH_I2,0)
    # m5 = cv.matchShapes(imagen,im5,cv.CONTOURS_MATCH_I2,0)
    
    # distancias = [imagenComp][]
    # print("Distancia entre:")
    ret, thresh = cv.threshold(im1, 127, 255, 0)
    ret, thresh2 = cv.threshold(imagen, 127, 255, 0)
    contours, hierarchy = cv.findContours(
        thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]
    contours2, hierarchy = cv.findContours(
        thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt2 = contours2[0]

    m1 = cv.matchShapes(cnt1, cnt2, cv.CONTOURS_MATCH_I2, 0)
    #cv.matchShapes(imagen,im1,cv.CONTOURS_MATCH_I2,0)
    # print("{}".format(m1) + ",")
    print(imagenComp +":")
    print((m1),end='\n')
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
img = "frame3"
imagen = cv.imread("Images/NewImages/"+ img +
                        ".jpg", cv.IMREAD_UNCHANGED)

#print(img)
for original in ls():
        # imagen = cv.imread("Images/PreImages/"+ img +
        #                 ".jpg", cv.IMREAD_UNCHANGED)
        x = original.split(".")
        nombre = x[0]
        formato = x[1]
        # if(nombre.endswith("_5")):
        imagenComp = nombre + "." + formato
        #print(imagenComp)
        distancia(imagen, imagenComp)