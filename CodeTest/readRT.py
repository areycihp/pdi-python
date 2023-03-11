##Abrir cámara en tiempo real
from matplotlib import pyplot as plt 
import numpy as np
import cv2

captura = cv2.VideoCapture(0)

while(True):
    # capturatura de frame a frame
    ret, frame = captura.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Muestra el frame trabajado
    cv2.imshow('Captura Tiempo real',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Muestra la imagen en tiempo real
captura.release()
cv2.destroyAllWindows()

#Prueba con video de YouTube
# import cv2 # opencv2 package for python.
# import pafy # pafy allows us to read videos from youtube.
# URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #URL to parse
# play = pafy.new(self._URL).streams[-1] #'-1' means read the lowest quality of video.
# assert play is not None # we want to make sure their is a input to read.
# stream = cv2.Videocapturature(play.url) #create a opencv video stream.