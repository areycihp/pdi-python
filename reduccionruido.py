##Reducción de ruido 
from skimage import io
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

imagen = io.imread("Images/B.jpg")
img_gray = rgb2gray(imagen)

med = median(img_gray)

plt.imshow(med)
plt.show()