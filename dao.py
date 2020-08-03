import csv
import time, datetime
import requests

class Dao:
    apiUrl = "https://qm2skcyyr8.execute-api.sa-east-1.amazonaws.com/prueba/tecla"
    fecha_inicio_lectura = datetime.datetime.now()
    @staticmethod
    def sendData(valor):
        hora_presionada = now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        Dao.postData(hora_presionada, valor)
                                 
                
    @staticmethod
    def postData(hora_presionada, valor):
        try:
            requests.post(Dao.apiUrl, json={'hora_presionada': hora_presionada, 'valor': valor})
            print("enviado")
        except:
            print("error")
