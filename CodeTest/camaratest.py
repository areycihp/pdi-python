##Prueba de abrir cámara web
import cv2
import numpy as np
import imutils
import requests

#captura = 0
captura = 'http://192.168.100.70:8080/shot.jpg'

#cap = cv2.VideoCapture(captura)

## Revisa si la cámara abre correctamente
# if not cap.isOpened():
#     raise IOError("No se puede abrir la cámara")

while True:
    #ret, frame = cap.read()
    img_resp = requests.get(captura)
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)
    #cv2.imshow('Input', frame)

    if cv2.waitKey(1) == 27:
        break

#cap.release()
cv2.destroyAllWindows()
