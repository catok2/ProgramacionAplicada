class Animal:
     def __init__(self, nombre , edad):
        self._nombre = nombre
        self._edad = edad

     @property
     def nombre(self):
         return self._nombre
     
     def set_nombre(self,nombre):
          self._nombre = nombre

     @property
     def edad(self):
         return self._edad
     
     def set_edad(self,edad):
          self._edad = edad   

     def caminar(self):
         pass     
     
     def emitir_sonido(self):
         print("El animal emite sonido")

