#Instalación pip install python-firebase

#Conexión
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("clave.json") #clave privada
firebase_admin.initialize_app(cred)

#Inicializamos firestore 
#Crear colección de prueba
db = firestore.client()
def agregarDatos(email, password):
    data = {"Email":email, "Contraseña":password}
    doc_ref = db.collection("users").add(data)
agregarDatos("yara.rivas@gmail.com","1234")  
