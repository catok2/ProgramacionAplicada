from .Figuras3D import Figura3D
import math

class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_area_superficial(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)