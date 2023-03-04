#Abrir pantalla de cámara
#Librerías principales
import sys
import os
from os import scandir, getcwd
#Librerías para GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.config import Config
from subprocess import Popen, PIPE
from kivy.clock import Clock
#Librería cámara
import cv2
import time
import numpy as np

#Permisos android
from android.permissions import request_permissions, Permission
request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])

#Cambiar ek código en archivo buildozer.spec
#android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

from math import copysign, log10

class Imagen(object):
    def __init__(self, nombre, formato):
        self.nombre = nombre
        self.formato = formato

    def getNombre(self):
        return self.nombre
    
    def getFormato(self):
        return self.formato

    def __str__(self):
        return "%s es un %s" % (self.nombre, self.formato)

    # Pre-procesamiento de imagen
    def preprocesamiento(self):
    # Librerias preprocesamiento
        import cv2 as cv
        import numpy as np 
        from skimage import io	
        from skimage import filters
        #Adquisición de imagen

        #Imágenes para obtener distancias
        # imagen = cv.imread("Images/"+self.nombre+"."+self.formato)    

        #Imágenes en tiempo real
        imagen = cv.imread("Images/RTImages/"+self.nombre+"."+self.formato)    

        # Eliminación de ruido - Preprocesamiento (2)
        im_ruido = cv.pyrMeanShiftFiltering(imagen,sp=30,sr=50)
        
        # Escala de grises - Preprocesamiento (3)
        im_gris = cv.cvtColor(im_ruido, cv.COLOR_BGR2GRAY)
        
        # Binarización | Binarización de Otsu - Segmentación (4)
        ret, im_binaria = cv.threshold(im_gris, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

        # Detección de bordes - Segmentación (5)
        img_filtro1 = filters.sobel(im_binaria)
        
        # Operaciones morfologicas - Segmentación (6)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        apertura = cv.morphologyEx(im_binaria, cv.MORPH_OPEN, kernel=kernel, iterations=2)    
        dilatacion = cv.dilate(apertura, kernel, iterations=3)
        
        # Umbralización - Segmentación (7)
        th, im_umbral = cv.threshold(apertura, 80, 150, cv.THRESH_BINARY_INV)
        
        # Copia de la imagen umbralizada - Segmentación (8)
        im_umbral_copia = im_umbral.copy()

        # Mascara para rellenar con 2 pixeles mayores a la imagen - Segmentación (9)  [Relleno]
        a, l = im_umbral.shape[:2]
        mascara = np.zeros((a+2, l+2), np.uint8)

        # Rellenando desde el punto (0, 0) al 255
        cv.floodFill(im_umbral_copia, mascara, (0,0), 255);
        
        # Invertido del relleno de la imagen - Segmentación (10) [Relleno invertido]
        im_seg_inv = cv.bitwise_not(im_umbral_copia)

        # Combinación de imagenes para obtener imagen rellenada - Segmentación (11)
        im_combinada = im_umbral | im_seg_inv

        # Binarización de otsu - Segmentación (12)
        ret, im_binaria2 = cv.threshold(im_combinada, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        #--- se usará para momentos ---
        #tamanio_imagen('Imagen binaria rellena')
         
        #momentos(im_binaria2)
        #distance(im_binaria2)

        #Crear una carpeta para las nuevas imágenes si no existe aún
        try:
            # Se crea la carpeta
            if not os.path.exists('Images/NewImages'):
                os.makedirs('Images/NewImages')
        
        # Si no se puede crear, muestra un error
        except OSError:
            print ('Error: No se ha podido crear la carpeta nueva :(')

        Nueva = cv.imwrite("Images/NewImages/"+self.nombre+"."+self.formato,im_binaria2)

        # Etiquetado - Técnicas y funciones de python (13)
        distancia = cv.distanceTransform(im_binaria2, cv.DIST_L2, 3)
        distancia_salida = cv.normalize(distancia, 0, 1.0, cv.NORM_MINMAX) 
        ret, superficie = cv.threshold(distancia_salida, distancia_salida.max() * 0.3, 255, cv.THRESH_BINARY)

        # Marcadores de superficie a 8 bits - Técnicas y funciones de python (14)
        superficie_8 = np.uint8(superficie)    
        superficie_desconocida = cv.subtract(dilatacion, superficie_8)      #dilatacion   
        # Etiquetado
        ret, etiquetado = cv.connectedComponents(superficie_8)  
        #print("Total de regiones:",ret)
        
        # Agregamos 1 
        etiquetado = etiquetado + 1
        # Región desconocida como 0
        etiquetado[superficie_desconocida == 255] = 0
        
        etiquetado = cv.watershed(imagen, markers=etiquetado)
        imagen[etiquetado == -1] = [0, 0, 255]
        #Fin etiquetado

        #Proceso de realzado de contorno - Técnicas y funciones de python (15)
        #contorno,ret = cv.findContours(im_binaria2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #Dibuja el contorno color lila
        #cv.drawContours (imagen, contorno, -1,(128, 0, 128),3)





Config.set('graphics', 'resizable', True)
letraFinal = ""

#----------- Elementos de cámara -----------

#Id de cámara a abrirse, al ser 0, se toma la cámara principal
captura = 0

#Definir las pantallas o ventanas a utilizar
class Principal(Screen):
    pass

class Camara(Screen):
    camera_display = ObjectProperty()
    camera_button: ObjectProperty()
    camera_lbl: ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cap = None

    def init_camera(self): 
        self.camera_button.disabled = True
        if not self.camera_display.texture:
            self.camera_button.text = "Iniciando cámara"
            
            if self._cap is None:
                
                self._cap = cv2.VideoCapture(captura)

            if self._cap is None or not self._cap.isOpened():
                
                self.camera_button.text = "Cámara no disponible"
                Clock.schedule_once(self._btn_restart, 2)
            else:
                
                self.camera_button.text = "Detener"
                #Se llama a la función cada cierto tiempo
                Clock.schedule_interval(self.update, 1.0 / 30.0)
                self.camera_button.disabled = False    
                
        else:
            # print("cuarto if")
            Clock.unschedule(self.update)
            self.camera_display.texture = None
            self._btn_restart()

    def _btn_restart(self, *args):
        self.camera_button.text = "Iniciar"
        self.camera_button.disabled = False
        #Para cerrar completamente la aplicación
        self._cap.release()
        #Window.close()
        
        ruta = 'Images/NewImages/'
        for real in lsReal():
            try:
                os.remove(ruta + real)
                #print('Elementos eliminados exitosamente')
            except OSError as error:
                print(error)
                #print("Eliminado incorrecto")


        ruta2 = 'Images/RTImages/'
        for new in lsRealFrames():
            try:
                os.remove(ruta2 + new)
                #print('Elementos eliminados exitosamente')
            except OSError as error:
                print(error)
                #print("Eliminado incorrecto")


    def update(self, dt):
        # Aquí corre la captura en tiempo real
        
        #Crear una carpeta para las nuevas imágenes si no existe aún
        try:
            # Se crea la carpeta
            if not os.path.exists('Images/RTImages'):
                os.makedirs('Images/RTImages')
        
        # Si no se puede crear, muestra un error
        except OSError:
            print ('Error: No se ha podido crear la carpeta nueva :(')

        
        ret, img = self._cap.read()
        img = cv2.flip(img, 0)
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(img.tobytes(), colorfmt='bgr', bufferfmt='ubyte')

        self.camera_display.texture = texture1

        # El frame se va tomando a la par de la imagen vista en vivo en la cámara
        frame_actual = dt
        
        # Leer el frame 
        ret,frame = self._cap.read()
        
        nombre = 'Images/RTImages/frame' + str(frame_actual) + '.jpg'
        #print ('Creando...' + nombre)

        # Voltea la imagen para "escribirla" / guardarla correctamente 
        img = cv2.flip(img, 0)
        # Escribe en la carpeta las nuevas imágenes
        cv2.imwrite(nombre, img)
        #print ('Guardando...' + nombre)
        

        # Llamar preprocesamiento

        nombreRT = 'frame' + str(frame_actual)
        ImagenReal = Imagen(nombreRT,'jpg')
        #Se realiza el preprocesamiento y se guarda como nueva imagen para utilizarse en la función de distancia
        imagen1 = ImagenReal.preprocesamiento()
        
        calculoDistancia(nombreRT)

        # Escribe letra en pantalla
        self.camera_lbl.text = "LETRA: \n" + calculoDistancia(nombreRT) #letraFinal

        frame_actual += 1;



#Se leen las nuevas imágenes para calcular la distancia a partir de los momentos de Hu
def calculoDistancia(imagenReal):
    m2 = 0
    m3 = 0
    letraF = ""

    imReal = cv2.imread("Images/NewImages/"+imagenReal+".jpg",cv2.IMREAD_GRAYSCALE)
    #print("Imagen: "+ imagenReal + "\n")
    for pre in ls():
        x = pre.split(".")
        # for real in lsReal():
             
        #Imágenes Yara
        if len(x[0]) == 2:
            ImagenYara = str(x[0]) + ".jpg"
            im3 = cv2.imread("Images/PreImages/"+ImagenYara,cv2.IMREAD_GRAYSCALE)
            m3 = cv2.matchShapes(imReal,im3,cv2.CONTOURS_MATCH_I2,0)
            print(ImagenYara + ": {}".format(m3))
        #Imágenes Are
        else:
            ImagenAre = str(x[0]) + ".jpg"
            im2 = cv2.imread("Images/PreImages/"+ImagenAre,cv2.IMREAD_GRAYSCALE)
            m2 = cv2.matchShapes(imReal,im2,cv2.CONTOURS_MATCH_I2,0)
            print(ImagenAre + ": {}".format(m2))

        # Condición para encontrar relación con la letra definida, entre menor sea la distancia, más se parece la letra
        if (m2<= 0.002 and m3<= 0.007):
            if len(x[0]) == 2:
                y = pre.split('y')
                letraF = str(y[0])
            else:
                letraF = str(x[0])
        print(letraF)
    return letraF
        

#Listar archivos de la carpeta de imágenes preprocesadas
def ls(ruta = 'Images/PreImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

#Listar archivos de la carpeta de frames de cámara en tiempo real preprocesadas
def lsReal(ruta = 'Images/NewImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


#Listar archivos de la carpeta de frames de cámara en tiempo real
def lsRealFrames(ruta = 'Images/RTImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

class Manager(ScreenManager):
    pass    


kv = Builder.load_file('nueva_ventana.kv')

class Ventana(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Ventana().run()


