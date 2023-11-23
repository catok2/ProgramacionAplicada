from figura_geometrica import FiguraGeometrica
import math

class Triangulo(FiguraGeometrica):
    def __init__(self, alto:float , ancho:float):
        if not isinstance(alto, (int, float)) and  isinstance(ancho,(int ,float)):
            raise TypeError(f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        self._alto = alto
        self._ancho = ancho
        

    def calcular_area(self):
        return (self._ancho * self._alto)/2
        
    def calcular_perimetro(self): 
        return self._alto + self._ancho + self.calcular_hipotenusa()
        
    def calcular_hipotenusa (self)->float:    
         return math.sqrt(self._alto**2 + self._ancho**2) 
    
    def informacion(self):
        print(f"Estas imprimiendo un Triangulo ")  