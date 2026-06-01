from src.repository.material_repository import MaterialRepository
from src.services.material_service import MaterialService
from src.view.material_view import MaterialVista


class MaterialController:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = MaterialRepository("src/materiales.json")
        self.service = MaterialService(self.repo)
        self.vista = MaterialVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_material(self, id_m, nom, uni, cant):
        self.service.registrar_material(id_m, nom, uni, int(cant))

    def get_all_materiales(self):
        return self.service.obtener_materiales()

    def buscar_material(self, id_m):
        return self.repo.get_by_id(id_m)

    def usar_material(self, id_m, cant):
        self.service.usar_material(id_m, int(cant))

    def eliminar_material(self, id_m):
        self.repo.delete(id_m)

    def volver_inicio(self):
        self.app_controller.mostrar_principal()