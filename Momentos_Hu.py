# MOMENTOS DE HU
import numpy as np
import cv2 as cv
import numpy as np
from skimage import io
from skimage import filters
from math import copysign, log10

# Leer imagen
imagen = cv.imread('Images/B.jpg')
# Eliminación de ruido - Preprocesamiento (2)
im_ruido = cv.pyrMeanShiftFiltering(imagen,sp=30,sr=50)

# Escala de grises - Preprocesamiento (3)
im_gris = cv.cvtColor(im_ruido, cv.COLOR_BGR2GRAY)


# Binarización | Binarización de Otsu - Segmentación (4)
ret, im_binaria = cv.threshold(im_gris, 0, 255, cv.THRESH_BINARY)


#Calculo de momentos
moments = cv.moments(im_binaria)
#Calculo de momentos de Hu
huMoments = cv.HuMoments(moments)

# Log scale hu moments 
for i in range(0,7):
   huMoments[i] = -1* copysign(1.0, huMoments[i]) * log10(abs(huMoments[i]))


