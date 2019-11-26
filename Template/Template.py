from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def __init__(self):
        self._cantidadDipositivos= None
    
class Celular(Dispositivo):
    def tipoDispositivo(self):
         print("Tiene un tamaño de 10 cm")
    def Precio(self):
         print("Tiene un tamaño de 10 mil pesos")

class Tablet (Dispositivo):
    def tipoDispositivo(self):
        print("Es una tablet")
    

class Laptop(Dispositivo):
    def tipoDispositivo(self):
        print("Es una latpto")
   
