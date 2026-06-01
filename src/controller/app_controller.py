import tkinter as tk


class AppController:
    def __init__(self, root):
        self.root = root
        # Aseguramos que el contenedor sea el gestor de espacio principal
        self.contenedor = tk.Frame(root)
        self.contenedor.pack(fill="both", expand=True)
        self.vista_actual = None

    def _limpiar_contenedor(self):
        # Destruimos los widgets anteriores
        for widget in self.contenedor.winfo_children():
            widget.destroy()
        self.vista_actual = None

    def _mostrar_vista(self, controlador_clase, *args):
        self._limpiar_contenedor()
        #Creamos el controlador pasando el contenedor padre
        controlador = controlador_clase(self.contenedor, *args)

        if hasattr(controlador, 'vista'):
            controlador.vista.pack(fill="both", expand=True)

        self.contenedor.update()

    def mostrar_principal(self):
        from src.view.principal_view import PrincipalView
        self._limpiar_contenedor()
        self.principal = PrincipalView(self.contenedor, self)
        self.principal.pack(fill="both", expand=True)

    def mostrar_registro_jornadas(self):
        from src.repository.jornada_repository import JornadaRepositorio
        from src.repository.zona_repository import ZonaRepository
        from src.services.jornada_service import JornadaService
        from src.controller.jornadas_controller import JornadaController

        repo_j = JornadaRepositorio("src/jornadas.json")
        repo_z = ZonaRepository("src/zonas.json")
        service = JornadaService(repo_j, repo_z)

        self._mostrar_vista(JornadaController, service, self)

    def mostrar_registro_usuarios(self):
        from src.controller.usuario_controller import ControladorUsuario
        self._mostrar_vista(ControladorUsuario, self)

    def mostrar_registro_voluntarios(self):
        from src.controller.voluntario_controller import ControladorVoluntario
        self._mostrar_vista(ControladorVoluntario, self)

    def mostrar_registro_zonas(self):
        from src.controller.zona_controller import ControladorZona
        self._limpiar_contenedor()
        # Creamos el controlador y él mismo crea y guarda la vista en self.vista
        controlador = ControladorZona(self.contenedor, self)
        controlador.vista.pack(fill="both", expand=True)
        self.contenedor.update()

    def mostrar_registro_material(self):
        self._limpiar_contenedor()
        from src.controller.material_controller import MaterialController
        self._mostrar_vista(MaterialController, self)

    def mostrar_registro_materiales(self):
        self.mostrar_registro_material()

    def mostrar_registro_fauna(self):
        self._limpiar_contenedor()

        from src.repository.fauna_repository import FaunaRepository
        from src.services.fauna_service import FaunaService
        from src.controller.fauna_controller import FaunaController

        repo_fauna = FaunaRepository("src/animales.json")
        servicio_fauna = FaunaService(repo_fauna)

        FaunaController(self.contenedor, self)

        self.contenedor.update()

    def mostrar_registro_basura(self):
        self._limpiar_contenedor()

        from src.repository.fauna_repository import FaunaRepository
        from src.services.fauna_service import FaunaService
        from src.controller.basura_controller import BasuraController

        repo_fauna = FaunaRepository("src/animales.json")
        servicio_fauna = FaunaService(repo_fauna)

        BasuraController(self.contenedor, self)

        self.contenedor.update()

    def mostrar_reporte(self):
        self._limpiar_contenedor()
        from src.controller.reporte_controller import ReporteController
        from src.repository.jornada_repository import JornadaRepositorio
        from src.repository.fauna_repository import FaunaRepository

        repo_j = JornadaRepositorio("src/jornadas.json")
        repo_f = FaunaRepository("src/animales.json")

        self.controlador_reporte = ReporteController(self.contenedor, self, repo_j, repo_f)

        self.contenedor.update()
