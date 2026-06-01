from src.model.zona import Zona
from src.repository.zona_repository import ZonaRepository
from src.view.zona_view import ZonaVista

class ControladorZona:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = ZonaRepository("zonas.json")
        self.vista = ZonaVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_zona(self, id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion):
        niveles = ["bajo", "medio", "alto", "critico"]
        if not nombre_zona.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia.")
        if nivel_contaminacion.lower() not in niveles:
            raise ValueError(f"Nivel invalido. Opciones: {', '.join(niveles)}")
        z = Zona(int(id_zona), nombre_zona.strip(), ubicacion.strip(), nivel_contaminacion.lower(), descripcion.strip())
        self.repo.add(z)

    def get_all_zonas(self):
        return self.repo.get_all()

    def volver_inicio(self):
        self.app_controller.mostrar_principal()