class factura:
    gen_codFactura = 0

    @classmethod
    def gen_codfactura(cls):
        cls.gen_codFactura += 1
        return cls.gen_codFactura
    
    def __init__(self , cliente , carrito):
        self._idfactura = factura.gen_codfactura()
        self._carrito = carrito
        self._cliente = cliente
        
    def anula_factura(self):
        pass
    
    
    def genFactura(self):
        pass
    
        
        
