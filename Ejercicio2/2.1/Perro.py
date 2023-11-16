from Animal import Animal
class Perro(Animal):
        def __init__(self , nombre , edad , comillos):
            super().__init__(nombre = nombre , edad = edad)
            self._comillos = comillos

        def caminar(self):
            print(f'El Perro {self._nombre} camina en 4 patas')    

