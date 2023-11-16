from abc import ABC, abstractmethod
from categoria import Categoria

    


class Producto():
        def __init__(self, nombre:str, precio:float, cantidad:int, categoria:object):
            self._nombre = nombre
            self._precio = precio
            self._cantidad = cantidad
            self._categoria = categoria
            
        def __str__(self) -> str:
             return f'''Producto:
                        Nombre:{self._nombre}
                        Precio:{self._precio}
                        Nombre:{self._cantidad}
                        categoria:{self._categoria}'''   
        
        

class ProductoAccesorios(Producto):
        def __init__(self, nombre, precio, cantidad, categoria):
            if not isinstance(nombre, str) and not not isinstance(precio, (int,float)) and not isinstance(nombre, int):
                raise TypeError(f"Error asignando el tipo de dato en {self.__class__.__name__}")
            super().__init__(nombre, precio, cantidad, categoria)     
        
        

class ProductoIndumentaria(Producto):
        def __init__(self, nombre, precio, cantidad , categoria):
            if not isinstance(nombre, str) and not not isinstance(precio, (int,float)) and not isinstance(nombre, int) :
              raise TypeError(f"Error asignando el tipo de dato en {self.__class__.__name__}")
            super().__init__(nombre, precio, cantidad, categoria)             
        

class ProductoElectronica(Producto):
        def __init__(self, nombre, precio, cantidad , categoria:object ):
            if not isinstance(nombre, str) and not not isinstance(precio, (int,float)) and not isinstance(nombre, int) and not isinstance(categoria,object):
                raise TypeError(f"Error asignando el tipo de dato en {self.__class__.__name__}")
            super().__init__(nombre, precio, cantidad , categoria)  
        

    

