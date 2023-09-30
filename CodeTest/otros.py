# # Compara con el conjunto de imágenes #1
#         if (numero == 1):
#             im1 = cv2.imread("Images/PreImages/" + letra + "_" + numero + ".jpg",
#                                 cv2.IMREAD_UNCHANGED)
#             m1 = cv2.matchShapes(imReal, im1, cv2.CONTOURS_MATCH_I2, 0)
#             break
#         # Compara con el conjunto de imágenes #2
#         if (numero == 2):
#             im2 = cv2.imread("Images/PreImages/" + letra + "_" + numero + ".jpg",
#                                 cv2.IMREAD_UNCHANGED)
#             m2 = cv2.matchShapes(imReal, im2, cv2.CONTOURS_MATCH_I2, 0)
#             break
#         # Compara con el conjunto de imágenes #3
#         if (numero == 3):
#             im3 = cv2.imread("Images/PreImages/" + letra + "_" + numero + ".jpg",
#                                 cv2.IMREAD_UNCHANGED)
#             m3 = cv2.matchShapes(imReal, im3, cv2.CONTOURS_MATCH_I2, 0)
#             break
#         # Compara con el conjunto de imágenes #4
#         if (numero == 4):
#             im4 = cv2.imread("Images/PreImages/" + letra + "_" + numero + ".jpg",
#                                 cv2.IMREAD_UNCHANGED)
#             m4 = cv2.matchShapes(imReal, im4, cv2.CONTOURS_MATCH_I2, 0)
#             break
#         # Compara con el conjunto de imágenes #5
#         if (numero == 5):
#             im5 = cv2.imread("Images/PreImages/" + letra + "_" + numero + ".jpg",
#                                 cv2.IMREAD_UNCHANGED)
#             m5 = cv2.matchShapes(imReal, im5, cv2.CONTOURS_MATCH_I2, 0)
#             break
        
#         prom = (m1+m2+m3+m4+m5)/5
# import cv2
# import numpy as np
# import matplotlib.pyplot as plot

# IMG = cv2.imread('Images/KBImages/F_5.jpg')
# IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB)

# K = np.ones((5, 5), np.float32)/25
# HMG = cv2.filter2D(IMG, -1, K)
# BL = cv2.blur(IMG, (5, 5))
# GB = cv2.GaussianBlur(IMG, (5, 5), 0)

# T = ['Original IMG', '2D Convolution','Blur','GaussianBlur']
# IMGS = [IMG, HMG,BL,GB]

# for j in range(4):
#     plot.subplot(2, 2, j+1), plot.imshow(IMGS[j], 'gray')
#     plot.title(T[j])
#     plot.xticks([]),plot.yticks([])

# plot.show()

# import cv2
# import numpy as np

# img = cv2.imread('Images/KBImages/F_5.jpg')
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# bound_lower = np.array([36, 25, 25])
# bound_upper = np.array([70, 255,255 ])

# mask_green = cv2.inRange(hsv_img, bound_lower, bound_upper)
# kernel = np.ones((7,7),np.uint8)

# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

# seg_img = cv2.bitwise_and(img, img, mask=mask_green)
# contours, hier = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

# cv2.imshow("Result", seg_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import os
 
# #ROOT_DIR = os.path.abspath("../")
# img_path = "Images/PreImages/"
# imglist = os.listdir(img_path)
# #print(filelist)
# i = 0
# for img in imglist:
#     i+=1
#     if img.endswith('.jpg'):
#         #print(i)
#         src = os.path.join (os.path.abspath (img_path), img) #El nombre original de la imagen
#         #print(img)
#         x = img.split(".")
#         y = x[0]
#         z = x[1]
#         #print(x[0])
#         if(len(y) == 1):
#             #print(y)
#             #a = y.split("y")

#             #print(a[0])
#             dst = os.path.join (os.path.abspath (img_path), y + "_1.jpg") # Renombrar de acuerdo a sus necesidades, puede cambiar 'E_' + img al nombre que desee
#             print(dst)
#             os.rename (src, dst) #Rename, sobrescribe el nombre original
#             print("Hecho") 