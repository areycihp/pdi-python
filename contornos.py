## Suavizar y resaltar contornos
from skimage import io
from skimage import feature
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

imagen = io.imread("ar2.jpg")
img = rgb2gray(imagen)
edge = feature.canny(img)
plt.imshow(edge)
plt.show()


##plt.subplot(211)
##io.imshow(imagen)
##plt.subplot(212)
##io.imshow(edge)
##io.show()
