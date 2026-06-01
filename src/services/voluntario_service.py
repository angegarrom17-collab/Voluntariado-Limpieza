from src.model.voluntario import Voluntario

CAMPOS_OBLIGATORIOS = ("id_voluntario", "nombre", "telefono", "correo", "organizacion")

class VoluntarioService:
    def __init__(self, voluntario_repository):
        self.voluntario_repository = voluntario_repository

        self._ids_registrados: set = set()
        self._inicializar_ids()

    def _inicializar_ids(self):
        for v in self.voluntario_repository.obtener_todos():
            self._ids_registrados.add(v.get("id_voluntario", ""))

    def registrar_voluntario(self, id_voluntario, nombre, telefono, edad, correo, organizacion):
        valores = (id_voluntario, nombre, telefono, correo, organizacion)
        for campo, valor in zip(CAMPOS_OBLIGATORIOS, valores):
            if not str(valor).strip():
                raise ValueError(f"El campo '{campo}' no puede estar vacío")

        if edad <= 0:
            raise ValueError("La edad debe ser mayor a cero")
        if edad < 18:
            raise ValueError("El voluntario debe ser mayor de 18 años")
        if "@" not in correo:
            raise ValueError("El correo no tiene formato válido")

        if id_voluntario in self._ids_registrados:
            raise ValueError(f"Ya existe un voluntario con ID {id_voluntario}")

        voluntario = Voluntario(id_voluntario, nombre, telefono, edad, correo, organizacion)
        self.voluntario_repository.agregar(voluntario)
        self._ids_registrados.add(id_voluntario)

    def obtener_todos_los_voluntarios(self):
        return self.voluntario_repository.obtener_todos()

    def buscar_por_organizacion(self, organizacion: str) -> list:
        todos = self.voluntario_repository.obtener_todos()
        return [v for v in todos if v.get("organizacion", "").lower() == organizacion.lower()]

    def obtener_organizaciones_unicas(self) -> set:
        todos = self.voluntario_repository.obtener_todos()
        return {v.get("organizacion", "") for v in todos if v.get("organizacion")}

    def eliminar_voluntario(self, id_voluntario):
        if not id_voluntario.strip():
            raise ValueError("El ID no puede estar vacío.")

        voluntarios = self.voluntario_repository.obtener_todos()
        voluntario_encontrado = None

        for v in voluntarios:
            if str(v.get("id_voluntario", "")).strip() == id_voluntario.strip():
                voluntario_encontrado = v
                break

        if not voluntario_encontrado:
            raise ValueError(f"No se encontró un voluntario con ID '{id_voluntario}'.")

        # Lo borramos del repositorio (si tu repo usa .eliminar())
        self.voluntario_repository.eliminar(voluntario_encontrado)