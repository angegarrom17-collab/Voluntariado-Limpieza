from src.model.zona import Zona
from src.repository.zona_repository import ZonaRepository
from src.view.zona_view import ZonaVista


class ControladorZona:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = ZonaRepository("src/zonas.json")
        self.vista = ZonaVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_zona(self, id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion):
        nombre_zona = str(nombre_zona).strip()
        ubicacion = str(ubicacion).strip()

        try:
            id_int = int(id_zona)
        except (ValueError, TypeError):
            raise ValueError("El ID debe ser un número entero válido.")

        niveles = ["bajo", "medio", "alto", "critico"]
        nivel_limpio = nivel_contaminacion.strip().lower()

        if not nombre_zona:
            raise ValueError("El nombre no puede estar vacío.")
        if not ubicacion:
            raise ValueError("La ubicación no puede estar vacía.")
        if nivel_limpio not in niveles:
            raise ValueError(f"Nivel de contaminación inválido. Use: {', '.join(niveles)}")

        zona = Zona(id_int, nombre_zona, ubicacion, nivel_limpio, descripcion.strip())
        self.repo.add(zona)

    def get_all_zonas(self):
        return self.repo.get_all()

    def eliminar_zona(self, id_zona):
        self.repo.delete(int(id_zona))

    def volver_inicio(self):
        self.app_controller.mostrar_principal()