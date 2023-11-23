class Cose():
    def __init__(self , kilometraje):
        self.velocidad = 0
        self._kilometraje = kilometraje


    def acelerar(self):
       if self.velocidad < 150:
            self.velocidad = self.velocidad + 1
            print(f"esta acelerando")
            self._kilometraje = self._kilometraje + 0.1

    @property
    def kilometraje(self):
        return self._kilometraje