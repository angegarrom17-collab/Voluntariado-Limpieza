import uuid
from src.repository.fauna_repository import FaunaRepository
from src.services.fauna_service import FaunaService
from src.view.basura_recolectada_view import BasuraRecolectadaVista

class BasuraController:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = FaunaRepository("src/animales.json", "src/basura.json")
        self.service = FaunaService(self.repo)
        self.vista = BasuraRecolectadaVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_basura(self, tipo, peso, fecha):
        id_b = str(uuid.uuid4())[:8]
        self.service.registrar_basura(id_b, tipo, float(peso), fecha)

    def get_all_basura(self):
        return self.service.obtener_basura()

    def volver_inicio(self):
        self.app_controller.mostrar_principal()