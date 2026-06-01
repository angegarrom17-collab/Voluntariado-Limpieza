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
        for w in self.contenedor.winfo_children():
            w.destroy()
        self.vista_actual = None

    def _mostrar_vista(self, controlador_clase, *args):
        """Método auxiliar para centralizar la creación de vistas"""
        self._limpiar_contenedor()
        # Creamos el controlador pasando el contenedor padre
        controlador = controlador_clase(self.contenedor, *args)

        # FORZADO DE VISUALIZACIÓN:
        # Si el controlador tiene un atributo .vista, lo empaquetamos si no lo hizo
        if hasattr(controlador, 'vista'):
            controlador.vista.pack(fill="both", expand=True)

        self.contenedor.update()  # Forzamos a Tkinter a renderizar inmediatamente

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

        repo_j = JornadaRepositorio("jornadas.json")
        repo_z = ZonaRepository("zonas.json")
        service = JornadaService(repo_j, repo_z)

        # Usamos el ayudante
        self._mostrar_vista(JornadaController, service, self)

    # Aplica este mismo patrón para el resto de tus métodos:
    def mostrar_registro_usuarios(self):
        from src.controller.usuario_controller import ControladorUsuario
        self._mostrar_vista(ControladorUsuario, self)

    def mostrar_registro_voluntarios(self):
        from src.controller.voluntario_controller import ControladorVoluntario
        self._mostrar_vista(ControladorVoluntario, self)

    def mostrar_registro_zonas(self):
        from src.controller.zona_controller import ControladorZona
        self._mostrar_vista(ControladorZona, self)

    def mostrar_registro_material(self):
        self._limpiar_contenedor()
        from src.controller.material_controller import MaterialController
        self._mostrar_vista(MaterialController, self)

    # Agregamos esta línea exacta abajo para solucionar el desajuste con la vista:
    def mostrar_registro_materiales(self):
        self.mostrar_registro_material()

    def mostrar_registro_fauna(self):
        # 1. Limpiamos los widgets de la pantalla anterior
        self._limpiar_contenedor()

        # 2. Importamos los archivos necesarios
        from src.repository.fauna_repository import FaunaRepository
        from src.services.fauna_service import FaunaService
        from src.controller.fauna_controller import FaunaController

        # 3. Inicializamos las dependencias
        repo_fauna = FaunaRepository("animales.json")
        servicio_fauna = FaunaService(repo_fauna)

        # 4. Instanciamos el controlador pasándole el contenedor y el controlador de la app
        FaunaController(self.contenedor, self)

        # 5. Forzamos la actualización visual de Tkinter
        self.contenedor.update()

    def mostrar_registro_basura(self):
        # 1. Limpiamos los widgets de la pantalla anterior
        self._limpiar_contenedor()

        # 2. Importamos los archivos necesarios para la basura
        from src.repository.fauna_repository import FaunaRepository
        from src.services.fauna_service import FaunaService
        from src.controller.basura_controller import BasuraController

        # 3. Compartimos el repositorio y servicio de fauna (donde está la lógica de basura)
        repo_fauna = FaunaRepository("animales.json")
        servicio_fauna = FaunaService(repo_fauna)

        # 4. Instanciamos tu BasuraController tal y como está diseñado originalmente
        BasuraController(self.contenedor, self)

        # 5. Forzamos la actualización visual de Tkinter para que pinte los componentes
        self.contenedor.update()

    def mostrar_reporte(self):
        self._limpiar_contenedor()

        # Importación limpia coincidiendo con el nombre exacto
        from src.controller.reporte_controller import ReporteController

        # Instanciamos el controlador directamente
        ReporteController(self.contenedor, self)

        self.contenedor.update()