from model.voluntario import Voluntario
from model.jornada_limpieza import  JornadaLimpieza
class VoluntarioServicio:

    def __init__(self, voluntario_repository,  zona_repository,jornada_repository):
        self.voluntario_repository = voluntario_repository
        self.zona_repository = zona_repository
        self.jornada_repository = jornada_repository

#------------------------------------------------------------------------------------------------------------------------------------
    def registrar_voluntario(self, id_voluntario: str, nombre: str, telefono: str, edad: int, correo: str, organizacion:str):
        if not id_voluntario.strip():
            raise ValueError("El id del Voluntario no puede estar vacío")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not telefono.strip():
            raise ValueError("El telefono no puede estar vacío")
        if edad <= 0:
            raise ValueError("La edad debe ser mayor a cero")
        if edad < 20:
            raise ValueError("El voluntario tiene que ser mayor de 20 años")
        if not correo.strip():
            raise ValueError("El correo no puede estar vacío")
        if not organizacion.strip():
            raise ValueError("La organizacion no puede estar vacío")


        todos_voluntarios = self.voluntario_repository.obtener_todos()

        for volu in todos_voluntarios:
            if volu["id_voluntario"] == id_voluntario:
                raise ValueError(f"Ya existe un voluntario registrado con el ID {id_voluntario}")

        voluntario = Voluntario(id_voluntario, nombre, telefono, edad, correo, organizacion)
        self.voluntario_repository.agregar(voluntario)

#-------------------------------------------------------------------------------------------------------------

    def obtener_todos_los_voluntarios(self):
        return self.voluntario_repository.obtener_todos()
#--------------------------------------------------------------------------------------------------------

    def registrar_jornada(self, id_jornada: str, fecha_jornada: str, descripcion: str, cantidadBasuraTotal: int, observaciones: str,id_zona: str):
        if not id_jornada.strip():
            raise ValueError("El ID de la jornada no puede estar vacío")
        if not fecha_jornada:
            raise ValueError("La fecha no pueden estar vacía")
        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía")
        if not cantidadBasuraTotal:
            raise ValueError("La cantidad de basura no puede estar vacía")
        if cantidadBasuraTotal <= 0:
            raise ValueError("La cantidad de basura debe ser mayor a cero")
        if not observaciones.strip():
            raise ValueError("Las observaciones no puede estar vacía")

        todas_jornadas = self.jornada_repository.obtener_todos()
        for jorn in todas_jornadas:
            if jorn["id_jornada"] == id_jornada:
                raise ValueError(f"Ya existe una jornada registrada con el ID {id_jornada}")

        zona_encontrada = None
        for zon in self.zona_repository.obtener_todos():
            if zon["id_zona"] == id_zona:
                zona_encontrada = zon
                break

        if not zona_encontrada:
            raise ValueError("La zona geográfica especificada no existe")

        jornada = JornadaLimpieza(id_jornada, fecha_jornada, descripcion, cantidadBasuraTotal, observaciones)
        self.jornada_repository.agregar(jornada)

#--------------------------------------------------------------------------------------------------------

    def asignar_voluntario_a_jornada(self, id_jornada: str, id_voluntario: str):

        jornada_dict = None
        todas_jornadas = self.jornada_repository.obtener_todos()
        for jorn in todas_jornadas:
            if jorn["id_jornada"] == id_jornada:
                jornada_dict = jorn
                break

        if not jornada_dict:
            raise ValueError("La jornada de limpieza no existe")


        voluntario_existe = False
        todos_voluntarios = self.voluntario_repository.obtener_todos()
        for volu in todos_voluntarios:
            if volu["id_voluntario"] == id_voluntario:
                voluntario_existe = True
                break

        if not voluntario_existe:
            raise ValueError("El voluntario no está registrado en el sistema")

        if len(jornada_dict["voluntarios"]) >= 20:
            raise ValueError("Esta jornada ya alcanzó el límite máximo de 20 voluntarios")

        if id_voluntario in jornada_dict["voluntarios"]:
            raise ValueError("Este voluntario ya está asignado a esta jornada")

        jornada_dict["voluntarios"].append(id_voluntario)

        self.jornada_repository._save()

#------------------------------------------------------------------------------------------------------
    def obtener_todas_las_jornadas(self):
        return self.jornada_repository.obtener_todos()

    def obtener_reporte_jornadas(self):
        jornadas = self.jornada_repository.obtener_todos()
        reporte = []
        for j in jornadas:
            reporte.append({
                "ID": j["id_jornada"],
                "Fecha": j["fecha_jornada"],
                "Descripción": j["descripcion"],
                "Basura (kg)": j["cantidadBasuraTotal"],
                "Voluntarios": len(j["voluntarios"])  # Contamos cuántos hay
            })
        return reporte