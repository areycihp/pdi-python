#Instalación pip install python-firebase

#Conexión
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("clave.json") #clave privada
firebase_admin.initialize_app(cred)

#Inicializamos firestore 
#Crear colección de pruebas


#db = firestore.client()
#def agregarDatos(email, password):
#    data = {"Email":email, "Contraseña":password}
#    doc_ref = db.collection("users").add(data)
#agregarDatos("yara.rivas@gmail.com","1234")  


db = firestore.client()
def agregarDatos(letra, distancia1, distancia2):
    data = {"Letra":letra, "Distancia1":distancia1, "Distancia2":distancia2}
    

    doc_ref = db.collection("distancias").add(data)
agregarDatos("A","0.240375859068142", "0.0133819743612972")  
agregarDatos("B","0.185261201152894", "0.017158075644287") 
agregarDatos("C","0.21303733251823","0.0525689610107154")
agregarDatos("D","0.260482447838035","0.0512389458133486")
agregarDatos("E","0.263171560544547","0.0219845959882314")
agregarDatos("F","0.197576152230508","0.0462206645919973")
agregarDatos("G","0.138029424125396","0.083065953536483")
agregarDatos("H","0.0967750879101987","0.1152140710033")
agregarDatos("I","0.228177429498365","0.0345905428572801")
agregarDatos("L","0.193837686343986","0.0554688645438909")
agregarDatos("M","0.183689856682689","0.0415346270519183")
agregarDatos("N","0.110149087115746","0.0741167483654314")
agregarDatos("O","0.244969636707356","0.035078853974193")
agregarDatos("P","0.191344809496144","0.0582042839770107")
agregarDatos("R","0.150313061127248","0.0748236081640998")
agregarDatos("S","0.280204591786346","0.000803758902320872")
agregarDatos("T","0.245701501577761","0.0288816059394179")
agregarDatos("U","0.170862223704777","0.0464784737250862")
agregarDatos("V","0.120980647939644","0.0685426368616379")
agregarDatos("W","0.134500212900406","0.0193965956138044")
agregarDatos("Y","0.373758507702646","0.0327405081829499")