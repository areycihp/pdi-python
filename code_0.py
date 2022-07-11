# Librerias
import cv2 as cv
import numpy as np
from skimage import io
from skimage import filters

#Pre-procesamiento de imagen
def algoritmo_region_bordes(imagen):    
    # Filtro de conservación de bordes y eliminación de ruido 
    im_ruido = cv.pyrMeanShiftFiltering(imagen,sp=30,sr=50)
    tamanio_imagen('Imagen sin ruido')
    cv.imshow('Imagen sin ruido', im_ruido)
    
    # Escala de grises
    im_gris = cv.cvtColor(im_ruido, cv.COLOR_BGR2GRAY)
    tamanio_imagen('Imagen a escala de grises')
    cv.imshow('Imagen a escala de grises', im_gris)
    
    # Binarización | Binarización de Otsu
    ret, im_binaria = cv.threshold(im_gris, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    tamanio_imagen('Imagen binarizada')
    cv.imshow('Imagen binarizada', im_binaria)

    #Aplicacion de filtros
    #filtros = [filters.sobel, filters.roberts, filters.prewitt]

    
    # Aplicación de filtros
    img_filtro1 = filters.sobel(im_binaria)
    tamanio_imagen('Imagen con filtro Sobel')
    cv.imshow('Imagen con filtro Sobel', img_filtro1)

    # img_filtro2 = filters.roberts(im_binaria)
    # tamanio_imagen('Imagen con filtro Roberts')
    # cv.imshow('Imagen con filtro Roberts', img_filtro2)

    # img_filtro3 = filters.prewitt(im_binaria)
    # tamanio_imagen('Imagen con filtro Prewitt')
    # cv.imshow('Imagen con filtro Prewitt', img_filtro3)
    
    # Operaciones morfologicas
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    kernel = np.ones((5,5),np.uint8)
    apertura = cv.morphologyEx(im_binaria, cv.MORPH_OPEN, kernel=kernel, iterations=2)    
    dilatacion = cv.dilate(apertura, kernel, iterations=6)
    tamanio_imagen('Imagen dilatada')
    cv.imshow("Imagen dilatada", dilatacion)
    
    #Binarización trunca
    ret,bin_trunca = cv.threshold(im_gris,127,255,cv.THRESH_TRUNC)

    im_combinada = dilatacion | bin_trunca
    tamanio_imagen('Imagen combinada rellena')
    cv.imshow("Imagen combinada rellena", im_combinada)


    # Umbralización técnica de segmentación     
    # th, im_umbral = cv.threshold(apertura, 80, 150, cv.THRESH_BINARY_INV);
    # tamanio_imagen('Imagen umbralizada')
    # cv.imshow("Imagen umbralizada", im_umbral)

    




#Tamaño de imagen
def tamanio_imagen(nombre_imagen):
    cv.namedWindow(nombre_imagen, cv.WINDOW_NORMAL)
    cv.resizeWindow(nombre_imagen, 500, 550)

# Carga de imagen
imagen = cv.imread('Images/B_dark.jpg')
tamanio_imagen('Imagen original')
cv.imshow('Imagen original', imagen)
algoritmo_region_bordes(imagen)
cv.waitKey(0)
cv.destroyAllWindows()