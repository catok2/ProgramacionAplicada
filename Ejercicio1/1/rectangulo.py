from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto:float , ancho:float):
           
        if not isinstance(alto, (int, float)) and  isinstance(ancho,(int ,float)):
            raise TypeError(f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        self._alto = alto
        self._ancho = ancho
        

    def calcular_area(self):
        return (self._ancho * self._alto)

    def calcular_perimetro(self):
        return  2*(self._ancho * self._alto)  