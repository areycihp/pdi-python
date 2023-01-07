## Tratamiento básico de imágenes
from skimage import io,color

## Plots para mostrar imágenes
import matplotlib.pyplot as plt

## Lee imagen
img = io.imread('ar2.jpg')

## Convierte imagen RGB de entrada a matriz de intensidades en escala de grises
img_gris = color.rgb2gray(img) 

## Muestra imagen
#io.imshow(img_gris)
#io.show()

## Mostrar ambas imágenes (original, tratada - escala de grises)
plt.subplot(211)
io.imshow(img)
plt.subplot(212)
io.imshow(img_gris)
io.show()

## Muestra forma y cantidad de elementos en el array img
print (img.shape)
