#Principal

import cv2 as cv
from Imagenes import Imagen

ImagenAre = Imagen("Y","jpg")
ImagenYara = Imagen("Yy","jpg")

#Se realiza el preprocesamiento y se guarda como nueva imagen para utilizarse en la función de distancia
imagen1 = ImagenAre.preprocesamiento()
imagen2 = ImagenYara.preprocesamiento()

#Se leen las nuevas imágenes para calcular la distancia a partir de los momentos de Hu
def calculoDistancia():
    im1 = cv.imread("Images/NewImages/"+ImagenAre.getNombre()+"."+ImagenAre.getFormato(),cv.IMREAD_GRAYSCALE) 
    im2 = cv.imread("Images/NewImages/"+ImagenYara.getNombre()+"."+ImagenYara.getFormato(),cv.IMREAD_GRAYSCALE)
    

    m2 = cv.matchShapes(im1,im2,cv.CONTOURS_MATCH_I2,0)
 
    print("Distancia entre \n-------------------------")
 
    print("Imagen Are comp. Imagen Yara: {}".format(m2))
    # print("BC original and bt (trasera) : {}".format(m2))
    # print("BC original and B_dark : {}".format(m3))


calculoDistancia()



