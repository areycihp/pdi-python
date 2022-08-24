#By Yara Rivas
# Librerias
import cv2 as cv
import numpy as np



# Comienza algoritmo
def algoritmo_region_bordes(imagen):    
    # Filtro de conservación de bordes y eliminación de ruido 
    im_ruido = cv.pyrMeanShiftFiltering(imagen,sp=30,sr=50)
    cv.imshow('Imagen sin ruido', im_ruido)
    
    # Escala de grises
    im_gris = cv.cvtColor(im_ruido, cv.COLOR_BGR2GRAY)
    
    # Binarización | Binarización de Otsu
    ret, im_binaria = cv.threshold(im_gris, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('Imagen binarizada', im_binaria)
    
    # Operaciones morfologicas
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    apertura = cv.morphologyEx(im_binaria, cv.MORPH_OPEN, kernel=kernel, iterations=2)    
    dilatacion = cv.dilate(apertura, kernel, iterations=3)
    

    # Umbralización técnica de segmentación     
    th, im_umbral = cv.threshold(apertura, 80, 150, cv.THRESH_BINARY_INV);
    cv.imshow("Imagen umbralizada", im_umbral)
    
    # Copia de la imagen umbralizada
    im_umbral_copia = im_umbral.copy()
    cv.imshow("Imagen segmentada inundada", im_umbral_copia)

    # Mascara para rellenar con 2 pixeles mayores a la imagen    
    a, l = im_umbral.shape[:2]
    mascara = np.zeros((a+2, l+2), np.uint8)

    # Rellenando desde el punto (0, 0) al 255
    cv.floodFill(im_umbral_copia, mascara, (0,0), 255);
     
    # Invertido del relleno de la imagen
    im_seg_inv = cv.bitwise_not(im_umbral_copia)    
    cv.imshow("Imagen segmentada invertida", im_seg_inv)

    # Combinación de imagenes para obtener imagen rellenada
    im_combinada = im_umbral | im_seg_inv
    cv.imshow("Imagen combinada rellena", im_combinada)

    # Binarización de otsu
    ret, im_binaria2 = cv.threshold(im_combinada, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('Imagen binaria rellena', im_binaria2)
    
    #Proceso de etiquetado de la imagen ---
    distancia = cv.distanceTransform(im_binaria2, cv.DIST_L2, 3)
    distancia_salida = cv.normalize(distancia, 0, 1.0, cv.NORM_MINMAX) 
    # cv.imshow('distance-', dist_out * 50)--0.6,255
    ret, superficie = cv.threshold(distancia_salida, distancia_salida.max() * 0.3, 255, cv.THRESH_BINARY)

    # Marcadores de superficie a 8 bits
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
    cv.imshow('Imagen etiquetada', imagen)
    #Fin etiquetado ---

    #Proceso de realzado de contorno
    contorno,ret = cv.findContours(im_binaria2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #Dibuja el contorno color lila
    cv.drawContours (imagen, contorno, -1,(128, 0, 128),3)
    cv.imshow('Imagen contorneada', imagen)
   



# Cargamos imagen
imagen = cv.imread('Images/B_dark_v2.jpg')
cv.imshow('Imagen inicial', imagen)
algoritmo_region_bordes(imagen)
cv.waitKey(0)
cv.destroyAllWindows()
