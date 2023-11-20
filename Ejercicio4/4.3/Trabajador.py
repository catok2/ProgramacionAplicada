from Empleado import Empleado
class Gerente(Empleado):
        def __init__(self, nombre, salario , departamento, codigoAcceso):
                super().__init__(nombre , salario , departamento)
                self._codigoAcceso = codigoAcceso


        @property
        def codigoAcceso(self):
               return  self._codigoAcceso

        def set_codigoAcceso(self, codigo):
                self._codigoAcceso = codigo

        def calcular_salario(self):
            return self._salario + (self._salario * 0.10)       
