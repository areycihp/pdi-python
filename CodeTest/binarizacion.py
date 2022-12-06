## Binarización con OpenCV
import numpy as np
import cv2
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Lectura de inagen original
image = cv2.imread('Images/B_dark.jpg')

# Da un nombre o titulo a la ventana
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
  
# Usa resizeWindow() para dar un tamaño determinado a la ventana
cv2.resizeWindow("Original", 300, 450)
  
# Muestra la imagen original
cv2.imshow("Original", image)

# Convierte imagen a Escala de grises
gray = cv2.imread('Images/B_dark.jpg', cv2.IMREAD_GRAYSCALE)

# Binariza imagen
t, dst = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Umbral", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Umbral", 300, 450)
cv2.imshow('Umbral', gray)
cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resultado", 300, 450)
cv2.imshow('Resultado', dst)

cv2.waitKey(0)
