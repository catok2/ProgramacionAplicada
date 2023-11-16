from Forma import Forma

PI = 3.14159

class Circulo(Forma):
    
    def __init__(self, color, dimension, diametro:float):
        super().__init__(color,dimension)
        if not isinstance(diametro, (int, float)):
            raise TypeError(f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        self._diametro = diametro
            
             

    def calcular_area(self):
        return PI * (self._diametro/2)**2
        
    def calcular_perimetro(self):
        return 2 * PI *  (self._diametro/2)