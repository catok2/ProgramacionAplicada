from vehiculo import vehiculo

class Motocicleta(vehiculo):
    def __init__(self, marca , modelo , velocidad_maxima):
        if not (isinstance(marca, str) and isinstance(modelo, str) and isinstance(velocidad_maxima, (int, float))):
            raise TypeError(f'{self.__class___.__name__} : Error con el tipo de dato')
        super().__init__(marca= marca , modelo=modelo , velocidad_maxima=velocidad_maxima)
        
    def arrancar(self):
        return f'''Empezando el arranque de
                Motocicleta: {self._marca} {self._modelo}
                '''
    
    def detener_vehiculo(self):
                return f'''Detencion en proceso de
                Motocicleta: {self._marca} {self._modelo}
                '''
    
    def bocinar(self):
        return f'''Suena bocina de
                Motocicleta: {self._marca} {self._modelo}
                '''
    

m1 = Motocicleta("Mercedez", "A1" ,500)
print(m1.arrancar())
print(m1.detener_vehiculo())
print(m1.bocinar())


    