class libro():
    def __init__(self, titulo, autor, precio):
        self._titulo = titulo
        self._autor = autor 
        self._precio  = precio
    @property 
    def precio(self):
        return self._precio    
            
            
class Comics(libro):
    def __init__(self, titulo , autor , precio):
        if not (isinstance(titulo, str) and isinstance(autor, str) and isinstance(precio, (int, float))):
            raise TypeError (f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        super().__init__(titulo = titulo, autor = autor, precio= precio)  
        
class Historia(libro):   
     def __init__(self, titulo , autor , precio):
        if not (isinstance(titulo, str) and isinstance(autor, str) and isinstance(precio, (int, float))):
            raise TypeError (f"{self.__class__.__name__}: Error con el tipo de dato ingresado")
        super().__init__(titulo = titulo, autor = autor, precio= precio)                