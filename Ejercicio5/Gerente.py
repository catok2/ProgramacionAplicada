from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, edad , dni, departamento):
        super().__init__(nombre ,edad , dni, self.__class__.__name__)
        self.departamento = departamento





g = Gerente('alan', 12 , 123124, 'Finanzas')

print(g.salario)