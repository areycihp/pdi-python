##Interfaz GUI
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
import time

Config.set('graphics', 'resizable', True)


class prototipo_gui(App):
    def build(self):
        self.window = GridLayout()
        #Widgets
        self.window.cols = 1 #División por grid
        #Margénes
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        #Imagen
        self.window.add_widget(Image(
            source = 'Images/logo.jpg',
            size_hint = (2.0, 2.0)
            ))

        #Etiqueta
        self.greeting = Label(
            text = "Bienvenido",
            font_size = 18 
            )
        self.window.add_widget(self.greeting)
        #Botón
        self.button = Button(
            text = "Iniciar",
            size_hint = (0.5, 0.5),
            bold = True,
            background_color = '#2979FF',
            background_normal = ""  #Color en escala normal
            )
        #Llamada a la función para el botón
        self.button.bind(on_press=self.Camara)
        self.window.add_widget(self.button)
        

        return self.window

    def Camara(self, instance):
        #self.greeting.text = "Iniciando..."
        camara = self.ids['camara']
        timestr = time.strftime("%d%m%Y_%H%M%S")
        camara.export_to_png("IMG_{}.png".format(timestr))
        print("Captura lista")


if __name__=='__main__':
    prototipo_gui().run()
