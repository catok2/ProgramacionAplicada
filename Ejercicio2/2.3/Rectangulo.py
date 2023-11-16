from Forma import Forma

class Rectangulo(Forma):
    def __init__(self, color:str  , dimension:int , ancho , alto):   
        super().__init__(color,dimension)
        self._ancho = ancho
        self._alto = alto

        

    def calcular_area(self):
        return (self._ancho * self._alto)

    def calcular_perimetro(self):
        return  2*(self._ancho * self._alto)  