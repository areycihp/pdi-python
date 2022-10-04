import cv2 as cv
import numpy as np

# Tamaño de imagen
def tamanio_imagen(nombre_imagen):
    cv.namedWindow(nombre_imagen, cv.WINDOW_NORMAL)
    cv.resizeWindow(nombre_imagen, 500, 550)

image = cv.imread('Images/G.jpeg')
#imagen = cv.imread('Images/A.jpeg')
tamanio_imagen('Imagen original')
cv.imshow('Imagen original', image)

(h, w) = image.shape[:2]
center = (w / 2, h / 2)
angle = 15
scale = 1
angle2 = 35

#First rotation at 15 grades
M = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(image, M, (w, h))

tamanio_imagen('Primer rotacion')
cv.imshow('Primer rotacion', rotated)

#Second rotation at 25 grades
M2 = cv.getRotationMatrix2D(center, angle2, scale)
rotated2 = cv.warpAffine(image, M2, (w, h))

tamanio_imagen('Segunda rotacion')
cv.imshow('Segunda rotacion', rotated2)

cv.waitKey(0)
cv.destroyAllWindows()