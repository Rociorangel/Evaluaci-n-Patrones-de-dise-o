from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def __init__(self):
        self.Pequeño = DispositivosMoviles()
        self._ligero= None
        self._Samsung = None
     
    
    
class Celular(Dispositivo):
    def Ligero(self):
        print("Es un celular")
    def Samsung():
         print("Tiene un tamaño de 10 cm")

class Tablet (Dispositivo):
    def Ligero(self):
        print("Es una tablet")
    

class DispositivosMoviles:
    def __init__(self):
        self.TipoDispositivos = None
