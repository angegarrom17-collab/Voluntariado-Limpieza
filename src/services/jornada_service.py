from src.model.jornada_limpieza import JornadaLimpieza


class JornadaService:
    def __init__(self, jornada_repository, zona_repository, voluntario_repository=None):
        self.jornada_repository = jornada_repository
        self.zona_repository = zona_repository
        self.voluntario_repository = voluntario_repository

    def registrar_jornada(self, id_jornada, fecha, descripcion, cantidad_basura_total, observaciones, id_zona):
        if not id_jornada.strip():
            raise ValueError("El ID no puede estar vacio")
        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacia")
        if not descripcion.strip():
            raise ValueError("La descripcion no puede estar vacia")
        if cantidad_basura_total <= 0:
            raise ValueError("La basura debe ser mayor a cero")
        if not observaciones.strip():
            raise ValueError("Las observaciones no pueden estar vacias")
        if not id_zona.strip():
            raise ValueError("El ID de zona no puede estar vacio")

        todas = self.jornada_repository.obtener_todos()
        for j in todas:
            if str(j.get("id_jornada")).strip() == id_jornada.strip():
                raise ValueError(f"Ya existe jornada con ID {id_jornada}")

        zona_encontrada = None
        id_zona_input = str(id_zona).strip()

        for z in self.zona_repository.obtener_todos():
            if str(z.get("id_zona")).strip() == id_zona_input:
                zona_encontrada = z
                break

        if not zona_encontrada:
            raise ValueError(f"La zona con ID '{id_zona}' no existe en el sistema.")

        jornada = JornadaLimpieza(id_jornada, fecha, descripcion, cantidad_basura_total, observaciones)

        self.jornada_repository.agregar(jornada)

    def obtener_todas_las_jornadas(self):
        return self.jornada_repository.obtener_todos()

    def buscar_jornada_por_id(self, id_jornada):
        for j in self.jornada_repository.obtener_todos():
            if str(j.get("id_jornada")) == str(id_jornada):
                return j
        return None

    def asignar_voluntario_a_jornada(self, id_jornada, id_voluntario):
        jornada_dict = self.buscar_jornada_por_id(id_jornada)
        if not jornada_dict:
            raise ValueError("La jornada no existe")

        jornada = JornadaLimpieza.from_dict(jornada_dict)

        if self.voluntario_repository:
            voluntarios = self.voluntario_repository.obtener_todos()
            existe = any(str(v.get("id_voluntario")) == str(id_voluntario) for v in voluntarios)
            if not existe:
                raise ValueError("El voluntario no esta registrado")

        if len(jornada.voluntarios) >= 20:
            raise ValueError("Limite de 20 voluntarios alcanzado")
        if id_voluntario in jornada.voluntarios:
            raise ValueError("El voluntario ya esta asignado")

        jornada.voluntarios.append(id_voluntario)

        self.jornada_repository.actualizar(jornada)

    def obtener_reporte_jornadas(self):
        jornadas = self.obtener_todas_las_jornadas()
        reporte = []
        for j in jornadas:
            reporte.append({
                "ID": j.get("id_jornada"),
                "Fecha": j.get("fecha"),
                "Descripcion": j.get("descripcion"),
                "Basura (kg)": j.get("cantidad_basura_total"),
                "Voluntarios": len(j.get("voluntarios", []))
            })
        return reporte