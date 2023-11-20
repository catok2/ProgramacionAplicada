from Animal import Animal
class Pajaro(Animal):
    def __init__(self , nombre , edad , patas):
        super().__init__(nombre = nombre , edad = edad)
        self._patas = patas

    def caminar(self):
      print(f'El pajaro {self._nombre} camina en dos patas')    

    def emitir_sonido(self):
         print("El Pajaro emite sonido de Pajaro")   

