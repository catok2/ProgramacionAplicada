from Animal import Animal
class Gato(Animal):
        def __init__(self , nombre , edad , garras):
            super().__init__(nombre = nombre , edad = edad)
            self._garras = garras

        def caminar(self):
            print(f'El Gato {self._nombre} camina en 4 patas')     


