##Prototipo Prueba
##Pantalla principal
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

#Clase que manipula o trabaja los elementos en la ventana
class Principal(BoxLayout):
    logo_principal = ObjectProperty()
    etiqueta_principal = ObjectProperty()
    boton_principal = ObjectProperty()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cap = None

    def abrirCamara(self):
        print("Abriendo cámara")
        process = Popen(['python', 'camara.py'], stdout=PIPE, stderr=PIPE)
        output = process.communicate()[0]

#Para ejecutar la ventana
class Ventana(App):
    def build(self):
        Builder.load_string(layout_principal)
        return Principal()

if __name__ == '__main__':
    Ventana().run()