class Cliente:
    def __init__(self, nombre, apellido , dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._carrito = None

    def add_carrito(self, carrito:object):
        self._carrito = carrito  

    @property
    def carrito(self):
        return self._carrito     
        
        