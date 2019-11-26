from abc import ABC, abstractmethod

class sistemaOperativo(ABC):
    @abstractmethod
    def __init__(self):
        self._CaracteristicasSistemaOperativo = None
        self._tipoSistemaOperativo = None
    
    
class Linux(sistemaOperativo):
    def ActualizacionPeriodica(self):
       print("sistema operativo es muy robusto en cuestion de seguridad")
       
class Windows(sistemaOperativo):
    def SeguridadPeriodica(self):
        print("es una sistema operativo que se actualiza constantemente")
        
class Mac (sistemaOperativo):
    def gamaAlta(self):
        print("es un sistema operativo de gama alta")


class Computer(sistemaOperativo):
    print("Software principal")
