from vehiculoabstract import VehiculoAbstracto

class vehiculo(VehiculoAbstracto):
    def __init__(self, marca , modelo , velocidad_maxima):
        self._marca = marca 
        self._modelo = modelo
        self._velocidadM = velocidad_maxima
        
        