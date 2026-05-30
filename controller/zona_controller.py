from model.zona import Zona
from repository.zona_repository import ZonaRepository


class ControladorZona:

    def __init__(self):
        self.repositorio_zona = ZonaRepository("zonas.json")
        self.callback_volver = None

    def set_volver_callback(self, callback):
        self.callback_volver = callback

    def volver_inicio(self):
        if self.callback_volver:
            self.callback_volver()

    def registrar_zona(self, id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion):
        niveles_validos = ["bajo", "medio", "alto", "critico"]

        if not nombre_zona.strip():
            raise ValueError("El nombre de la zona no puede estar vacío.")
        if not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía.")
        if nivel_contaminacion.lower() not in niveles_validos:
            raise ValueError(
                f"Nivel de contaminación no válido. "
                f"Opciones: {', '.join(niveles_validos)}"
            )

        nueva_zona = Zona(
            id_zona,
            nombre_zona.strip(),
            ubicacion.strip(),
            nivel_contaminacion.lower(),
            descripcion.strip()
        )
        self.repositorio_zona.add(nueva_zona)

    def get_all_zonas(self):
        return self.repositorio_zona.get_all()

    def get_zona_by_id(self, id_zona):
        return self.repositorio_zona.get_by_id(id_zona)

    def existe_zona(self, id_zona):
        return self.repositorio_zona.exists(id_zona)

    def get_zonas_por_nivel(self, nivel):
        todas_las_zonas = self.repositorio_zona.get_all()
        zonas_filtradas = []
        for zona in todas_las_zonas:
            if zona.nivel_contaminacion.lower() == nivel.lower():
                zonas_filtradas.append(zona)
        return zonas_filtradas