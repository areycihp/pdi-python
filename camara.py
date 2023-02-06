##Abrir pantalla de cámara
##Librerías para GUI
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from subprocess import Popen, PIPE
from kivy.clock import Clock
##Librería cámara
import cv2
import os
import time
import numpy as np

Config.set('graphics', 'resizable', True)

#----------- Elementos de cámara -----------

#Id de cámara a abrirse, al ser 0, se toma la cámara principal
captura = 0

#Definición de elementos en la ventana
layout_camara = '''
GridLayout:
    cols: 1
    size_hint: 0.6,0.7
      
<Camara>:
    camera_display: img
    camera_button: btn
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
            text: 'Salir'
            on_release: app.stop()
'''

#Clase que manipula o trabaja los elementos en la ventana
class Camara(BoxLayout):
    camera_display = ObjectProperty()
    camera_button: ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cap = None
    
    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self._cap.release()

    def init_camera(self): 
        self.camera_button.disabled = True
        if not self.camera_display.texture:
            self.camera_button.text = "Iniciando cámara"
            print("cero if")
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
        # Aquí corre la captura

        try:
            # Se crea la carpeta
            if not os.path.exists('Images/RTImages'):
                os.makedirs('Images/RTImages')
        
        # Si no se puede crear, muestra un error
        except OSError:
            print ('Error: No se ha podido crear la carpeta nueva :(')
        

        # Se trabaja con la captura en tiempo real
        # real = self._cap
        
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
        # texture1.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        self.camera_display.texture = texture1

        frame_actual = dt

        
        ## Condición para tomar capturas mientras la cámara está abierta
        # while(True):
        print("entró"+ str(frame_actual))
        
        ## Se usa el tiempo para tomar una captura del video cada cierto tiempo
        #start_time = time.time()

        ## Leer el frame 
        ret,frame = self._cap.read()
        
        nombre = 'Images/RTImages/frame' + str(frame_actual) + '.jpg'
        print ('Creando...' + nombre)

        ## Escribe en la carpeta las nuevas imágenes
        cv2.imwrite(nombre, img)
        print ('Guardando...' + nombre)
        #spent = time.time() - start_time # tiempo que se uso en las tareas de arriba

        #time.sleep(5 - spent)
        frame_actual += 1;


#Para ejecutar la ventana
class OCVCamara(App):
    def build(self):
        Builder.load_string(layout_camara)
        return Camara()
    

if __name__ == '__main__':
    OCVCamara().run()
    #principal().run()