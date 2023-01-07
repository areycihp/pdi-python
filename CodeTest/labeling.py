## @autor: Areyci Huerta Patiño
## @date: 04/25/2022

## Detección de bordes (Border detection)
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
## Reducción de ruido (Noise reduction)
from skimage.filters.rank import median
from skimage.morphology import disk
## Contraste (Contrast)
from skimage import exposure
import numpy as np
## Binarización (Binarization)
import cv2
## Erosión | Dilatación (Erosion | Dilaton)
from scipy import ndimage
## Bordes (Edges)
from skimage.feature import canny

#Lectura de imagen | Image reading
image = cv2.imread("Images/B_dark.png")

#Escala de grises | Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imread('Images/A_dark1.jpg', cv2.IMREAD_GRAYSCALE)
#Binarización 
t, binary_img = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

#Bordes | Edges
#edge = canny(binary_img)

#Relleno o eliminado de espacios | Fill dark dots or spaces with dilation
#Dilatación
kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(binary_img, kernel, iterations = 2)
dilation = cv2.dilate(binary_img, kernel, iterations = 15)

#Ventana | Show the results
cv2.namedWindow("Escala de Grises", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Escala de Grises", 300, 350)
cv2.imshow("Escala de Grises", gray)
cv2.namedWindow("Binarizada", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Binarizada", 300, 350)
cv2.imshow("Binarizada", binary_img)
# cv2.namedWindow("Erosion", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Erosion", 300, 350)
# cv2.imshow("Erosion", erosion)
cv2.namedWindow("Dilatacion", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Dilatacion", 300, 350)
cv2.imshow("Dilatacion", dilation)
# plt.imshow(dilation)
# plt.show()

cv2.waitKey(0)
