# MOMENTOS DE HU
import numpy as np
import cv2
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Read image as grayscale image
im = cv2.imread('Images/A_2.jpg',cv2.IMREAD_GRAYSCALEt
                t, im = cv2.threshold(im, 110, 255, cv2.THRESH_BINARY)
                
#t,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

#Calculo de momentos
moments = cv2.moments(im)
#Calculo de momentos de Hu
huMoments = cv2.HuMoments(moments)

# Log scale hu moments 
for i in range(0,7):
   huMoments[i] = -1* copysign(1.0, huMoments[i]) * log10(abs(huMoments[i])))


