#Imagen y prepocesamiento

# Librerias
import cv2 as cv
import numpy as np
from skimage import io
from skimage import filters

from math import copysign, log10

class Imagen(object):

    def __init__(self, nombre, formato):
        self.nombre = nombre
        self.formato = formato

    def getNombre(self):
        return self.nombre
    
    def getFormato(self):
        return self.formato

    def __str__(self):
        return "%s es un %s" % (self.nombre, self.formato)

    # Pre-procesamiento de imagen
    def preprocesamiento(self):
        #Adquisición de imagen
        imagen = cv.imread("Images/"+self.nombre+"."+self.formato)    

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

        Nueva = cv.imwrite("Images/NewImages/"+self.nombre+"."+self.formato,im_binaria2)

        # Etiquetado - Técnicas y funciones de python (13)
        distancia = cv.distanceTransform(im_binaria2, cv.DIST_L2, 3)
        distancia_salida = cv.normalize(distancia, 0, 1.0, cv.NORM_MINMAX) 
        ret, superficie = cv.threshold(distancia_salida, distancia_salida.max() * 0.3, 255, cv.THRESH_BINARY)

        # Marcadores de superficie a 8 bits - Técnicas y funciones de python (14)
        superficie_8 = np.uint8(superficie)    
        superficie_desconocida = cv.subtract(dilatacion, superficie_8)      #dilatacion   
        # Etiquetado
        ret, etiquetado = cv.connectedComponents(superficie_8)  
        print("Total de regiones:",ret)
        
        # Agregamos 1 
        etiquetado = etiquetado + 1
        # Región desconocida como 0
        etiquetado[superficie_desconocida == 255] = 0
        
        etiquetado = cv.watershed(imagen, markers=etiquetado)
        imagen[etiquetado == -1] = [0, 0, 255]
        #Fin etiquetado

        #Proceso de realzado de contorno - Técnicas y funciones de python (15)
        contorno,ret = cv.findContours(im_binaria2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #Dibuja el contorno color lila
        cv.drawContours (imagen, contorno, -1,(128, 0, 128),3)

            