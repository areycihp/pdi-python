#Abrir pantalla de cámara
#Librerías principales
import sys
import os
from os import scandir, getcwd
#Librerías para GUI
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from subprocess import Popen, PIPE
from kivy.clock import Clock
#Librería cámara
import cv2
import time
import numpy as np
#Preprocesamiento de imágenes
from Imagenes import Imagen

Config.set('graphics', 'resizable', True)
letraFinal = ""
#Id de cámara a abrirse, al ser 0, se toma la cámara principal
captura = 0

#Permisos android
# from android.permissions import request_permissions, Permission
# request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])

#Cambiar ek código en archivo buildozer.spec
#android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

#Definición de elementos en la ventana
Config.set('graphics', 'resizable', True)

layout_principal = '''
GridLayout:
    cols: 1
    size_hint: 0.6,0.7
      
<Principal>
    logo_principal: img_logo
    etiqueta_principal: lbl
    boton_principal: btn_comenzar
    orientation: 'vertical'
    spacing: 10
    Label:
        id: lbl1
        text: 'Reconocimiento de LSM'
        font_size: 28        
        color: 0,1,0,1
    Image:
        id: img_logo
        source: 'Images/logo.jpg'
        opacity: 1 if self.texture else 0
        size_hint: 1, 2
    Label:
        id: lbl
        text: 'Bienvenido'
        font_size: 26     
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, 0.5
        Button:
            id: btn_comenzar
            text: "Comenzar"
            on_release: root.abrirCamara()
        Button:
            id: btn_salir
            text: 'Salir'
            on_release: app.stop()
'''



#----------- Elementos de cámara -----------

#Definición de elementos en la ventana
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
        if (m2<= 0.007 and m3<= 0.01):
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

#Listar archivos de la carpeta de frames de cámara en tiempo real
def lsReal(ruta = 'Images/NewImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


#Clase que manipula o trabaja los elementos en la ventana secundaria
class Camara(BoxLayout):
    camera_display = ObjectProperty()
    camera_button: ObjectProperty()
    camera_lbl: ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cap = None
    
    def on_stop(self):
        #without this, app will not exit even if the window is closed
        #self._cap.release()
        ruta = 'Images/RTImages/'
        for real in lsReal():
            try:
                os.remove(ruta)
                print('Elementos eliminados exitosamente')
            except OSError as error:
                print(error)
                print("Eliminado incorrecto")


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
        print ('Creando...' + nombre)

        # Voltea la imagen para "escribirla" / guardarla correctamente 
        img = cv2.flip(img, 0)
        # Escribe en la carpeta las nuevas imágenes
        cv2.imwrite(nombre, img)
        print ('Guardando...' + nombre)
        

        # Llamar preprocesamiento

        nombreRT = 'frame' + str(frame_actual)
        ImagenReal = Imagen(nombreRT,'jpg')
        #Se realiza el preprocesamiento y se guarda como nueva imagen para utilizarse en la función de distancia
        imagen1 = ImagenReal.preprocesamiento()
        
        calculoDistancia(nombreRT)

        # Escribe letra en pantalla
        self.camera_lbl.text = "LETRA: \n" + calculoDistancia(nombreRT) #letraFinal

        frame_actual += 1;



#Para ejecutar la ventana secundaria
class OCVCamara(App):
    def build(self):
        Builder.load_string(layout_camara)
        return Camara()




#Clase que manipula o trabaja los elementos en la ventana principal
class Principal(BoxLayout):
    logo_principal = ObjectProperty()
    etiqueta_principal = ObjectProperty()
    boton_principal = ObjectProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cap = None
    
    def abrirCamara(self):
        #Builder.load_string(layout_camara)
        print("Abriendo cámara")        
        return OCVCamara()

      

#Para ejecutar la ventana principal
class Ventana(App):
    def build(self):
        Builder.load_string(layout_principal)
        return Principal()

if __name__ == '__main__':
    Ventana().run()