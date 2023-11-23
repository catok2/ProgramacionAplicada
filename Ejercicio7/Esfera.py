from .Figuras3D import Figura3D
import math

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def calcular_area_superficial(self):
        return 4 * math.pi * (self.radio ** 2)