from Empleado import Empleado
class Gerente(Empleado):
        def __init__(self, nombre, salario , departamento , codigoFreeAlmuerzo ):
                super().__init__(nombre , salario , departamento)
                self._codigoFreeAlmuerzo = codigoFreeAlmuerzo

        @property
        def codigoFreeAlmuerzo(self):
               return self._codigoFreeAlmuerzo 

        def set_codigoFreeAlmuerzo(self, codigo):
               self._codigoFreeAlmuerzo = codigo

        def calcular_salario(self):
            return self._salario + (self._salario * 0.21)       

