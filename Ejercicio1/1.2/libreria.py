from abstractlibreria import Abtractlibreria

class Libreria(Abtractlibreria):
    
        
    def calcular_precio(self,libros):
        lnPrecioTot = 0
        for li in libros:
            lnPrecioTot += li.precio 
        
        return lnPrecioTot