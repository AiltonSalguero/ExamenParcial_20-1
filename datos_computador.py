import socket
import getpass
import platform
import sys
import sysconfig
# Captura los datos computador: 
# arquitectura,
# id del sistema operativo,
# nombre del computador,
# IP,
# nombre del usuario.

class DatosComputador:
    @staticmethod
    def getArquitectura():
        return str(platform.architecture())
    @staticmethod
    def getIdSistemaOperativo():
        return str(platform.system())  + " " + str(platform.release())
    @staticmethod
    def getNompreComputador():
        return socket.gethostname()

    @staticmethod
    def getNombreUsuario():
        return getpass.getuser()

    @staticmethod
    def getIp():
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    
    
    @staticmethod
    def getDatosComputador():
        return ""