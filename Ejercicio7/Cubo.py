from .Figuras3D import Figura3D

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_area_superficial(self):
        return 6 * (self.lado ** 2)