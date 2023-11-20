class Empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento


    def aumentar_salario(self):
        pass    

    def calcular_salario(self):
            return self._salario + (self._salario * 0.1)       