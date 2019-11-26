
'''
Patron state
'''

from abc import ABC, abstractmethod



class EstatusEscolar(ABC):
    @abstractmethod
    def __init__(self):
         self._estatusEscolar = None
    
class Estudiante(EstatusEscolar):
    def Yoaprobar(self):
        self._estatusescolar = EstatusEscolar()
        pass
    def Yoreprobar (self):
        pass

class aprobado(EstatusEscolar):
     def estudiarDuro(self):
        print("Estudiar diariemanete para mejorar")
        
class reprobado(EstatusEscolar):
    def estudiarDuro(self):
        print("Estudiar diariemanete para mejorar")

