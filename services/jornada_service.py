from model.jornada_limpieza import JornadaLimpieza

class JornadaServicio:

    def __init__(self, jornada_repository, zona_repository):
        self.jornada_repository = jornada_repository
        self.zona_repository = zona_repository

#------------------------------------------------------------------------------------------------------------------------------------
    def registrar_jornada(self, id_jornada: str, fecha_jornada: str, descripcion: str, cantidad_basura_total: int, observaciones: str, id_zona: str):
        if not id_jornada.strip():
            raise ValueError("El ID de la jornada no puede estar vacío")
        if not fecha_jornada.strip():
            raise ValueError("La fecha no puede estar vacía")
        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía")
        if cantidad_basura_total <= 0:
            raise ValueError("La cantidad de basura debe ser mayor a cero")
        if not observaciones.strip():
            raise ValueError("Las observaciones no pueden estar vacías")
        if not id_zona.strip():
            raise ValueError("El ID de la zona no puede estar vacío")

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

        jornada = JornadaLimpieza(id_jornada, fecha_jornada, descripcion, cantidad_basura_total, observaciones)
        self.jornada_repository.agregar(jornada)

#------------------------------------------------------------------------------------------------------------------------------------
    def obtener_todas_las_jornadas(self):
        return self.jornada_repository.obtener_todos()

#------------------------------------------------------------------------------------------------------------------------------------
    def buscar_jornada_por_id(self, id_jornada: str):
        todas_jornadas = self.jornada_repository.obtener_todos()
        for jorn in todas_jornadas:
            if jorn["id_jornada"] == id_jornada:
                return jorn
        return None