from figura_geometrica import FiguraGeometrica

PI = 3.14159

class Circulo(FiguraGeometrica):
    
    def __init__(self, diametro:float):
        if not isinstance(diametro, (int, float)):
            raise TypeError(f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        self._diametro = diametro
            
             

    def calcular_area(self):
        return PI * (self._diametro/2)**2
        
    def calcular_perimetro(self):
        return 2 * PI *  (self._diametro/2)
    
