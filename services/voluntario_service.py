from model.voluntario import Voluntario
from model.jornada_limpieza import import JornadaLimpieza
class VoluntarioServicio:

    def __init__(self, voluntario_repository,  zona_repository,jornada_repository):
        self.voluntario_repository = voluntario_repository
        self.zona_repository = zona_repository
        self.jornada_repository = jornada_repository

#------------------------------------------------------------------------------------------------------------------------------------
    def registrar_voluntario(self, idVoluntario: str, nombre: str, telefono: str, edad: int, correo: str, organizacion:str):
        if not idVoluntario.strip():
            raise ValueError("El id del Voluntario no puede estar vacío")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not telefono.strip():
            raise ValueError("El telefono no puede estar vacío")
        if not edad.strip():
            raise ValueError("La carrera no puede estar vacía")
        if edad < 20:
            raise ValueError("El voluntario tiene que ser mayor de 20 años")
        if not correo.strip():
            raise ValueError("El correo no puede estar vacío")
        if not organizacion.strip():
            raise ValueError("La organizacion no puede estar vacío")


        voluntario = Voluntario(idVoluntario, nombre, telefono, edad, correo, organizacion)
        self.voluntario_repository.add(voluntario)
#-------------------------------------------------------------------------------------------------------------

    def obtener_todos_los_voluntarios(self):
        return self.voluntario_repository.obtener_todos()
#--------------------------------------------------------------------------------------------------------

    def registrar_jornada(self, id_jornada: str, nombre_jornada: str, fecha_jornada: str, id_zona: str):
        if not id_jornada.strip():
            raise ValueError("El código no puede estar vacío")
        if not nombre_jornada.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not fecha_jornada:
            raise ValueError("La fecha no pueden estar vacía")
        zona = self.zona_repository.obtener_por_id(id_zona)
        if not zona:
            raise ValueError("La zona geográfica especificada no existe")

        jornada = JornadaLimpieza(id_jornada, nombre_jornada, fecha_jornada, id_zona)
        self.jornada_repository.add(jornada)


    def asignar_voluntario_a_jornada(self, id_jornada: str, id_voluntario: str):

        jornada = self.jornada_repository.obtener_por_id(id_jornada)
        if not jornada:
            raise ValueError("La jornada de limpieza no existe")

        voluntario = self.voluntario_repository.obtener_por_id(id_voluntario)
        if not voluntario:
            raise ValueError("El voluntario no está registrado en el sistema")

        if len(jornada.voluntarios) >= 20:
            raise ValueError("Esta jornada ya alcanzó el límite máximo de 20 voluntarios para esta zona")

        if id_voluntario in jornada.voluntarios:
            raise ValueError("Este voluntario ya está asignado a esta jornada")

        jornada.voluntarios.append(id_voluntario)
        self.jornada_repository.actualizar(jornada)


    def obtener_todas_las_jornadas(self):
        return self.jornada_repository.obtener_todos()