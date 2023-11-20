from cliente import Cliente

class factura:
    gen_codFactura = 0

    @classmethod
    def gen_codfactura(cls):
        cls.gen_codFactura += 1
        return cls.gen_codFactura
    
    def __init__(self , cliente):
        self._idfactura = factura.gen_codfactura()
        self._cliente = cliente
        self.totFactura = self.genFactura()



    def anula_factura(self):
        pass
    
    
    def genFactura(self):
        total = 0
        for producto in self._cliente.carrito.productos:
            total += producto.precio
        return total    

    
        
        
