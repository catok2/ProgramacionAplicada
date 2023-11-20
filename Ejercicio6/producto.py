class Producto():
        def __init__(self, nombre:str, precio:float, cantidad:int):
            self._nombre = nombre
            self.precio = precio
            self._cantidad = cantidad
            
        def __str__(self) -> str:
             return f'''Producto:
                        Nombre:{self._nombre}
                        Precio:{self._precio}
                        Nombre:{self._cantidad}
                        '''   
        
        
        

    

