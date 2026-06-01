from src.repository.fauna_repository import FaunaRepository
from src.services.reporte_service import ReporteService
from src.view.reporte_view import ReporteVista

class ReporteController:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = FaunaRepository()
        self.service = ReporteService()
        self.vista = ReporteVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def obtener_total_basura(self):
        return self.service.calcular_total_basura(self.repo.obtener_basura())

    def obtener_promedio_basura(self):
        return self.service.calcular_promedio_basura(self.repo.obtener_basura())

    def obtener_total_animales(self):
        return self.service.contar_animales(self.repo.obtener_animales())

    def obtener_residuos_por_tipo(self):
        return self.service.obtener_residuos_por_tipo(self.repo.obtener_basura())

    def volver_inicio(self):
        self.app_controller.mostrar_principal()