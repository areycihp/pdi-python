## Segmentación

from skimage import io
from skimage import feature
from skimage.feature import canny
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

imagen = io.imread("Images/B_dark.jpg")
img = rgb2gray(imagen)
edge = canny(img)
##edges = canny(coins/255.)
plt.imshow(edge)
plt.show()

