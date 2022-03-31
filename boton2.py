##Botón con imagen
## 01/07/2021
from kivy.app import App

## Coloca los widgets de modo que se puedan colocar juntos
##de manera organizada
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

Builder.load_string("""

<KivyButton>:

    Button:

        text: "Hello Button!"

        size_hint: .12, .12

        Image:

            source: 'images.jpg'

            center_x: self.parent.center_x

            center_y: self.parent.center_y  
    
""")


class KivyButton(App, BoxLayout):
    
    def build(self):
        
        return self
    
KivyButton().run()
