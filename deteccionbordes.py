## Detección de bordes
# Librerias necesarias
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Abrimos la imagen
imagen = io.imread("Images/A_2.jpg")
imagen_g = rgb2gray(imagen)

# Filtros: sobel, roberts, prewitt
filtros = [filters.sobel, filters.roberts, filters.prewitt]

for filtro in filtros:
    # Aplicamos cada uno de los filtros
    img_fil = filtro(imagen_g)
    
    # Mostramos los resultados 
    #plt.imshow(img_fil)
    #plt.show()

    plt.subplot(211)
    io.imshow(imagen)
    plt.subplot(212)
    io.imshow(img_fil)
    io.show()
