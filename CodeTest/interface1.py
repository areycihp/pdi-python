##Interfaces gráficas Kivy
## 01/07/2021

##Modulo de la aplicación Kivy
from kivy.app import App

##Importación de elementos
from kivy.uix.label import Label
from kivy.uix.button import Button


##Programa principal
##class FirstKivy(App):

    ##def build(self):

        ## return Label(text="Hello Kivy!") ##Label
        ## return Button(text="Welcome to LikeGeeks!")  ##Botón por default
        ##return Button(text="Welcome Ing. Areyci", background_color=(155,0,51,53))

##FirstKivy().run()

##Deshabilitar botón después de presionarlo
from kivy.app import App

from functools import partial

class KivyButton(App):

    def disable(self, instance, *args):

        instance.disabled = True

    def update(self, instance, *args):

        instance.text = "I am Disabled!"

    def build(self):

        mybtn = Button(text="Click me to disable", pos=(300,350), size_hint = (.25, .18))

        mybtn.bind(on_press=partial(self.disable, mybtn))

        mybtn.bind(on_press=partial(self.update, mybtn))

        ## return Button(text="Welcome to LikeGeeks!", pos=(300,350), size_hint = (.25, .18))

        return mybtn

KivyButton().run()
