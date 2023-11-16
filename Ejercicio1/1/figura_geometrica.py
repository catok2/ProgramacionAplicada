from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass