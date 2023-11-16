class Estudiante:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad= edad
        self._calificaciones = []

    
    @property
    def calificaciones(self):
        return self._calificaciones

    def set_Calificacion(self, Calificacion):
        self._calificaciones.append(Calificacion)
     

e = Estudiante("pepito", 20)

e.set_Calificacion(2)
e.set_Calificacion(8)

print(f' el alumno {e.nombre}  tiene estas calificaciones {e.calificaciones}')