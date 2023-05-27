# Abrir pantalla de cámara
# Librerías principales
import math
import sys
import os
from os import scandir, getcwd
# Librerías para GUI
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from subprocess import Popen, PIPE
from kivy.clock import Clock
# Librería cámara
import cv2
import time
import numpy as np
# Preprocesamiento de imágenes
from Imagenes import Imagen

Config.set('graphics', 'resizable', True)
letraFinal = ""

# ----------- Elementos de cámara -----------

# Id de cámara a abrirse, al ser 0, se toma la cámara principal
captura = 0

# Definición de elementos en la ventana
layout_camara = '''
GridLayout:
    cols: 1
    size_hint: 0.6,0.7
      
<Camara>:
    camera_display: img
    camera_button: btn
    camera_lbl: btn_label
    orientation: 'vertical'
    Image:
        id: img
        opacity: 1 if self.texture else 0
        size_hint: 1, 0.7

    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1.0, 0.1
        Button:
            id: btn
            text: "Iniciar"
            on_press: root.init_camera()
        Button:
            id: btn_label
            text: ""
        Button:
            text: 'Salir'
            on_release: app.stop()
'''


# app.stop()
# Clase que manipula o trabaja los elementos en la ventana
class Camara(BoxLayout):
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
                # Se llama a la función cada cierto tiempo
                # 30 frames por segundo ~ tiempo real
                Clock.schedule_interval(self.update, 1.0 / 30.0)
                self.camera_button.disabled = False

        else:

            Clock.unschedule(self.update)
            self.camera_display.texture = None
            self._btn_restart()

    def _btn_restart(self, *args):
        self.camera_button.text = "Iniciar"
        self.camera_button.disabled = False
        # Para cerrar completamente la aplicación
        self._cap.release()
        # Window.close()

        ruta = 'Images/NewImages/'
        for real in lsReal():
            try:
                os.remove(ruta + real)
                print('Elementos eliminados exitosamente')
            except OSError as error:
                print(error)
                print("Eliminado incorrecto")

        ruta2 = 'Images/RTImages/'
        for new in lsRealFrames():
            try:
                os.remove(ruta2 + new)
                print('Elementos eliminados exitosamente')
            except OSError as error:
                print(error)
                print("Eliminado incorrecto")

    def update(self, dt):
        # Aquí corre la captura en tiempo real
        # Leer el frame
        ret, img = self._cap.read()
        img = cv2.flip(img, 0)
        texture1 = Texture.create(
            size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(img.tobytes(), colorfmt='bgr', bufferfmt='ubyte')

        self.camera_display.texture = texture1

        # Crear una carpeta para las nuevas imágenes si no existe aún
        try:
            # Se crea la carpeta
            if not os.path.exists('Images/RTImages'):
                os.makedirs('Images/RTImages')

        # Si no se puede crear, muestra un error
        except OSError:
            print('Error: No se ha podido crear la carpeta nueva :(')

        # El frame se va tomando a la par de la imagen vista en vivo en la cámara
        frame_actual = dt

        # Leer el frame
        # ret, frame = self._cap.read()

        nombre = 'Images/RTImages/frame' + str(frame_actual) + '.jpg'
        # print ('Creando...' + nombre)

        # Voltea la imagen para "escribirla" / guardarla correctamente
        img = cv2.flip(img, 0)
        # Escribe en la carpeta las nuevas imágenes
        cv2.imwrite(nombre, img)
        print('Guardando...' + nombre)

        # Llamar preprocesamiento

        nombreRT = 'frame' + str(frame_actual)
        ImagenReal = Imagen(nombreRT, 'jpg')
        # Se realiza el preprocesamiento y se guarda como nueva imagen para utilizarse en la función de distancia
        imagen1 = ImagenReal.preprocesamiento()

        calculoDistancia(nombreRT)

        # Escribe letra en pantalla
        self.camera_lbl.text = "LETRA: \n" + \
            calculoDistancia(nombreRT)  # letraFinal

        #frame_actual += 1


# Se leen las nuevas imágenes para calcular la distancia a partir de los momentos de Hu
def calculoDistancia(imagenReal):
    m2 = 0
    m3 = 0
    letraF = ""
    umbral = 0.9
    bandera1 = False
    bandera2 = False

    imReal = cv2.imread("Images/NewImages/"+imagenReal +
                        ".jpg", cv2.IMREAD_GRAYSCALE)
    
    for pre in ls():
        ##Para comparación por letra (imagen de cada miembro del equipo)
        x = pre.split(".")
        

        # Imágenes Yara
        if len(x[0]) == 2:
            ImagenYara = pre
            im3 = cv2.imread("Images/PreImages/"+ImagenYara,
                             cv2.IMREAD_UNCHANGED)
            ret, thresh = cv2.threshold(im3, 127, 255, 0)
            ret, thresh2 = cv2.threshold(imReal, 127, 255, 0)
            contours, hierarchy = cv2.findContours(
                thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cnt1 = contours[0]
            contours2, hierarchy = cv2.findContours(
                thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cnt2 = contours2[0]

            m3 = cv2.matchShapes(cnt1, cnt2, cv2.CONTOURS_MATCH_I2, 0)
            
            
            # print("------------------")
            # if (math.isclose(m3,umbral) or m3 < umbral): #Función recomendada por mayor alernativa (mejor resultado para flotates)
            #     bandera1 = True
            #     print(ImagenYara + ": {}".format(m3))
        # Imágenes Are
        else:
            ImagenAre = pre
            im2 = cv2.imread("Images/PreImages/"+ImagenAre,
                             cv2.IMREAD_UNCHANGED)
            ret, thresh = cv2.threshold(im2, 127, 255, 0)
            ret, thresh2 = cv2.threshold(imReal, 127, 255, 0)
            contours, hierarchy = cv2.findContours(
                thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cnt1 = contours[0]
            contours2, hierarchy = cv2.findContours(
                thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cnt2 = contours2[0]

            m2 = cv2.matchShapes(cnt1, cnt2, cv2.CONTOURS_MATCH_I2, 0)
            
        
        # Condición para encontrar relación con la letra definida, el umbral establecido es menor a 0.9 y, obviamente, cercano a cero para mayor coincidencia
        prom = (m2+m3)/2
        print("Prom" + ": {}".format(m2))
        
        umbral = 0.9

        if (math.isclose(prom,umbral) or prom < umbral):  #Función recomendada por mayor alernativa (mejor resultado para flotates)
            print(prom)
            if len(x[0]) == 2:
                y = pre.split('y')
                letraF = str(y[0])
            else:
                letraF = str(x[0])
            print("Letra:" + letraF)    

    return letraF


# Listar archivos de la carpeta de imágenes preprocesadas
def ls(ruta='Images/PreImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# Listar archivos de la carpeta de frames de cámara en tiempo real preprocesadas


def lsReal(ruta='Images/NewImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


# Listar archivos de la carpeta de frames de cámara en tiempo real
def lsRealFrames(ruta='Images/RTImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# Para ejecutar la ventana
class OCVCamara(App):
    def build(self):
        Builder.load_string(layout_camara)
        return Camara()


if __name__ == '__main__':
    OCVCamara().run()
    # principal().run()
