## Detección de bordes
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
#Librerías para reducción de ruido
from skimage.filters.rank import median
from skimage.morphology import disk
##Librería contraste
from skimage import exposure
import numpy as np
## Binarización
import cv2

imagen = io.imread("Images/B_dark.jpg")
img_gray = rgb2gray(imagen)

#Binarización 
ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)

io.imshow(thresh1)
io.imshow(thresh3)
io.show()
io.show()

# Reducción de ruido
#img_uint8 = img_gray.astype(np.uint8)  # Warning
imagen_r = median(img_gray)

# Estiramiento de contraste
p2, p98 = np.percentile(imagen_r, (2,98))
img_rescale = exposure.rescale_intensity(imagen_r, in_range=(p2,p98))

# Ecualización
img_eq = exposure.equalize_hist(imagen_r)

# Ecualización adaptiva
imagen_g = exposure.equalize_adapthist(imagen_r, clip_limit=0.03)

# Filtros: sobel, roberts, prewitt
filtros = [filters.sobel, filters.roberts, filters.prewitt]
# filtros = [filters.prewitt]

io.imshow(imagen)
io.show()
for filtro in filtros:
    # Aplicamos cada uno de los filtros
    img_fil = filtro(imagen_g)
    #img_fil2 = filtro(imagen_g)
    # Mostramos los resultados 
    plt.imshow(img_fil)
    plt.show()

    # plt.subplot(211)
    # io.imshow(imagen)
    # plt.subplot(212)
    # io.imshow(img_fil)
    # io.show()

# Aplicación de filtro Sobel
# img_fil = filtros[0](imagen_g)

# plt.imshow(img_fil)
# plt.show()