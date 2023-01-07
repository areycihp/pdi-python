#Conexión
import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2 as cv

cred = credentials.Certificate("clave.json") #clave privada
firebase_admin.initialize_app(cred, {'storageBucket': 'reconocimiento-de-lsm.appspot.com'})

#Acceder al depósito
paquete = storage.bucket()
#Acceder a las imágenes de la bd
#sys.argv
blob = paquete.get_blob("A.jpg")
array = np.frombuffer(blob.download_as_string(), np.uint8)
img = cv.imdecode(array, cv.COLOR_BGR2BGR555)

cv.imshow('imagen A',img)
cv.waitKey(0)