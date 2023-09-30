#Imagen y prepocesamiento
#Librerías principales
import sys
import os
from os import scandir, getcwd
# Librerias preprocesamiento
import cv2 as cv
import numpy as np
from skimage import io
from skimage import filters

from math import copysign, log10


# Pre-procesamiento de imagen
def preprocesamiento(nombre):
    #Adquisición de imagen
   
    imagen = cv.imread("Images/KBImages/" + nombre)   

    # Eliminación de ruido - Preprocesamiento (2)
    im_ruido = cv.pyrMeanShiftFiltering(imagen,sp=30,sr=50)
    
    # Escala de grises - Preprocesamiento (3)
    im_gris = cv.cvtColor(im_ruido, cv.COLOR_BGR2GRAY)
    
    # Binarización | Binarización de Otsu - Segmentación (4)
    ret, im_binaria = cv.threshold(im_gris, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # Detección de bordes - Segmentación (5)
    img_filtro1 = filters.sobel(im_binaria)
    
    # Operaciones morfologicas - Segmentación (6)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    apertura = cv.morphologyEx(im_binaria, cv.MORPH_OPEN, kernel=kernel, iterations=2)    
    dilatacion = cv.dilate(apertura, kernel, iterations=3)
    
    # Umbralización - Segmentación (7)
    th, im_umbral = cv.threshold(apertura, 80, 150, cv.THRESH_BINARY_INV)
    
    # Copia de la imagen umbralizada - Segmentación (8)
    im_umbral_copia = im_umbral.copy()

    # Mascara para rellenar con 2 pixeles mayores a la imagen - Segmentación (9)  [Relleno]
    a, l = im_umbral.shape[:2]
    mascara = np.zeros((a+2, l+2), np.uint8)

    # Rellenando desde el punto (0, 0) al 255
    cv.floodFill(im_umbral_copia, mascara, (0,0), 255);
    
    # Invertido del relleno de la imagen - Segmentación (10) [Relleno invertido]
    im_seg_inv = cv.bitwise_not(im_umbral_copia)

    # Combinación de imagenes para obtener imagen rellenada - Segmentación (11)
    im_combinada = im_umbral | im_seg_inv

    # Binarización de otsu - Segmentación (12)
    ret, im_binaria2 = cv.threshold(im_combinada, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #--- se usará para momentos ---
    #tamanio_imagen('Imagen binaria rellena')
        
    #momentos(im_binaria2)
    #distance(im_binaria2)

    #Crear una carpeta para las nuevas imágenes si no existe aún
    try:
        # Se crea la carpeta
        if not os.path.exists('Images/NewImages'):
            os.makedirs('Images/NewImages')
    
    # Si no se puede crear, muestra un error
    except OSError:
        print ('Error: No se ha podido crear la carpeta nueva :(')

    Nueva = cv.imwrite("Images/PreImages/" + nombre,im_binaria2)





def ls(ruta='Images/KBImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


for original in ls():
        x = original.split(".")
        nombre = x[0]
        formato = x[1]
        if(nombre.endswith("_3")):
            imagen = nombre + "." + formato
            preprocesamiento(imagen)