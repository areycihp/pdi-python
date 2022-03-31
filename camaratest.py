##Prueba de abrir cámara web

import cv2

cap = cv2.VideoCapture(0)

## Revisa si la cámara abre correctamente
if not cap.isOpened():
    raise IOError("No se puede abrir la cámara")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:  ## ESC = ANSI (27), detiene la ejecución de la cámara
        break

cap.release()
cv2.destroyAllWindows()
