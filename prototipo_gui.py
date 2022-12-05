##Interfaz GUI
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

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
            source = 'Images/logo.jpeg',
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
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        

        return self.window

    def callback(self, instance):
        self.greeting.text = "Iniciando..."

if __name__=='__main__':
    prototipo_gui().run()
