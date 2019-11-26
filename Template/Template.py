from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def __init__(self):
        self._cantidadDipositivos= Dispositivo()
    def tipoDispotivo(self):
        pass
    
class Celular(Dispositivo):
    def cantidadDispositivos(self):
         print("Tiene un tamaño de 10 cm")

class Tablet (Dispositivo):
    def tipoDispositivo(self):
        print("Es una tablet")
    

class Laptop(Dispositivo):
    def tipoDispositivo(self):
        print("Es una latpto")
   
