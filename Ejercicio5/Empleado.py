from Persona import Persona

class Empleado(Persona):

    sueldo_base: int = 300000

    def __init__(self, nombre, edad , dni, cargo):
        super().__init__(nombre ,edad , dni)
        self.cargo = cargo
        self._salario = self.calcular_salario()
   

    def calcular_salario(self):
        if self.cargo == "Gerente":
            return Empleado.sueldo_base * 1.2
        else:
            return Empleado.sueldo_base
    
    @property
    def salario(self):
        return self._salario