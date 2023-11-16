from abc import ABC, abstractclassmethod


class VehiculoAbstracto(ABC):
    
    @abstractclassmethod
    def arrancar(self):
        pass
    @abstractclassmethod
    def detener_vehiculo(self):
        pass
    @abstractclassmethod
    def bocinar(self):
        pass 

 