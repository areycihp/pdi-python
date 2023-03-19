# Principal

import cv2 as cv
from Imagenes import Imagen

# ImagenAre = Imagen("frame0.6874911000000008","jpg")
# ImagenYara = Imagen("A","jpg")

# Se realiza el preprocesamiento y se guarda como nueva imagen para utilizarse en la función de distancia
# imagen1 = ImagenAre.preprocesamiento()
# imagen2 = ImagenYara.preprocesamiento()

# Se leen las nuevas imágenes para calcular la distancia a partir de los momentos de Hu


def calculoDistancia():
    im2 = cv.imread("Images/PreImages/Ey.jpg", cv.IMREAD_UNCHANGED)
    im1 = cv.imread("Images/PreImages/E.jpg", cv.IMREAD_UNCHANGED)

    # m2 = cv.matchShapes(im1,im2,cv.CONTOURS_MATCH_I3,0)
    ret, thresh = cv.threshold(im1, 127, 255, 0)
    ret, thresh2 = cv.threshold(im2, 127, 255, 0)
    contours, hierarchy = cv.findContours(
        thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]
    contours2, hierarchy = cv.findContours(
        thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt2 = contours2[0]
    ret = cv.matchShapes(cnt1, cnt2, 2, 0.0)
    print("Distancia entre \n-------------------------")

    print("Imagen Are comp. Imagen Yara: {}".format(ret))
    # cv.drawContours (im1, contours, -1,(0, 255, 0),7)
    # for c in contours:
    #     for c2 in contours2:
    #         rets = cv.matchShapes(c, c2, 1, 0.0)
    #         if rets < 0.5:
    #             peri = cv.arcLength(c, True)
    #             approx = cv.approxPolyDP(c, 0.02 * peri, True)
    #             cv.drawContours(im1, [approx], -1, (0, 255, 0), 7)
    
    # cv.namedWindow('Contornos',cv.WINDOW_NORMAL)
    # cv.namedWindow('Tresh',cv.WINDOW_NORMAL)
    # cv.imshow('Contornos', im1)
    # cv.imshow('Tresh', thresh)
    # if cv.waitKey(0):
    #     cv.destroyAllWindows()

    # print("BC original and bt (trasera) : {}".format(m2))
    # print("BC original and B_dark : {}".format(m3))


calculoDistancia()
