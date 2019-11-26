from abc import ABC, abstractmethod

class Computadoras(ABC):
    @abstractmethod
    def __init__(self):
        self.tipo = Tipo
        self.caracteristicas = None

class PC(Computadoras):
        print("Dipositivo de gama alta")

class Laptop(Computadoras):
        print("Modelo perteneciente a Apple")


class Tipo:
   print("Caracteristica/ tipo de maquina")
        

class CasaEscritorio(Tipo):
    def grande(self):
        print("Solo puede estar estatica")
    
class Portatil(Tipo):
        print("Facíl de traer a todos lados")

