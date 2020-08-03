from dao import *
class TimeManager():
    tiempo_espera = 10
    hora_envio= time.time() + tiempo_espera
    @staticmethod
    def esTiempoDeEnviar():
        # Funcion booleana que devuelve verdadero cuando la hora actual 
        # ha superado la hora de envio.
        if time.time() > TimeManager.hora_envio:
            return True
        else:
            return False
    @staticmethod
    def medirTiempo():
        if TimeManager.esTiempoDeEnviar():
            Dao.sendData()
            TimeManager.hora_envio = time.time() + TimeManager.tiempo_espera