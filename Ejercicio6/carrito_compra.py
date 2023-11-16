class CarritoCompra():
    def __init__(self, ):
        self._productos = []

    def agregar_producto(self, producto:object):
        if not isinstance(producto,object): 
            raise TypeError("Error agregando producto al Carrito")
        self._productos.append(producto)
        
    
    
    def remover_producto(self,producto:object):
        if not isinstance(producto,object): 
            raise TypeError("Error removiendo producto del Carrito")
        self._productos.remove(producto)

    @property    
    def productos(self):    
        return self._productos
        
        
            
            
              