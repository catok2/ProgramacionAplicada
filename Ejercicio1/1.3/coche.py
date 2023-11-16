from vehiculo import vehiculo

class Coche(vehiculo):
    def __init__(self, marca , modelo , velocidad_maxima):
        if not (isinstance(marca, str) and isinstance(modelo, str) and isinstance(velocidad_maxima, (int, float))):
            raise TypeError(f'{self.__class___.__name__} : Error con el tipo de dato')
        super().__init__(marca= marca , modelo=modelo , velocidad_maxima=velocidad_maxima)
        
    def arrancar():
        pass
    
    def detener():
        pass
    
    def bocinar():
        pass 
    