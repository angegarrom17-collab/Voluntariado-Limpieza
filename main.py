import tkinter as tk
from view.principal_view import PrincipalView
from view.usuario_view import UsuarioVista
from view.voluntario_view import VoluntarioVistaModerna
from view.jornada_view import JornadaVistaModerna
from view.zona_view import ZonaVista

# 1. IMPORTA LOS COMPONENTES REALES DE VOLUNTARIOS, JORNADAS Y ZONAS
from repository.voluntario_repository import VoluntarioRepositorio
# 💡 Importamos los repositorios que te hacían falta para quitar los 'None'
from repository.jornada_repository import JornadaRepositorio
from repository.zona_repository import ZonaRepository

from services.voluntario_service import VoluntarioServicio

# Importamos tus controladores reales de negocio
from controller.usuario_controller import ControladorUsuario
from controller.zona_controller import ControladorZona
from controller.voluntario_controller import ControladorVoluntario
from controller.jornadas_controller import JornadaController # 💡 Corregido el nombre si era 'jornada_controller'

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto OFC Desarrollo - Protección del Mar")
        self.root.geometry("1000x650")

        # Contenedor dinámico para intercambiar los Frames en la misma ventana
        self.contenedor = tk.Frame(self.root)
        self.contenedor.pack(fill="both", expand=True)

        # 👤 Instancia del negocio de usuarios
        self.negocio_usuario = ControladorUsuario()
        self.negocio_usuario.set_volver_callback(self.mostrar_menu_principal)

        # 📍 Instancia del negocio de zonas
        self.negocio_zona = ControladorZona()
        self.negocio_zona.set_volver_callback(self.mostrar_menu_principal)

        # 🤝 INICIALIZACIÓN DEL NEGOCIO DE VOLUNTARIOS, ZONAS Y JORNADAS
        # 💡 Inicializamos los tres repositorios con sus respectivos archivos JSON
        self.voluntario_repo = VoluntarioRepositorio("voluntarios.json")
        self.zona_repo = ZonaRepository("zonas.json")
        self.jornada_repo = JornadaRepositorio("jornadas.json")

        # 💡 Le pasamos los repositorios reales al servicio para que pueda guardar datos de verdad
        self.voluntario_servicio = VoluntarioServicio(
            self.voluntario_repo,
            self.zona_repo,
            self.jornada_repo
        )

        self.vista_actual = None
        self.mostrar_menu_principal()

    def limpiar_contenedor(self):
        """Elimina la vista activa para dar paso a la siguiente."""
        if self.vista_actual is not None:
            self.vista_actual.destroy()

    def mostrar_menu_principal(self):
        self.limpiar_contenedor()
        self.vista_actual = PrincipalView(self.contenedor, controller=self)

    def volver_inicio(self):
        """Método que llama ZonaVista y UsuarioVista para salir"""
        self.mostrar_menu_principal()

    # -------------------------------------------------------------
    # PASARELAS DEL MÓDULO DE ZONAS
    # -------------------------------------------------------------
    def mostrar_registro_zonas(self):
        self.limpiar_contenedor()
        self.vista_actual = ZonaVista(self.contenedor, controller=self)

    def registrar_zona(self, id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion):
        self.negocio_zona.registrar_zona(id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion)

    def get_all_zonas(self):
        return self.negocio_zona.get_all_zonas()

    # -------------------------------------------------------------
    # PASARELAS DE USUARIOS
    # -------------------------------------------------------------
    def mostrar_registro_usuarios(self):
        self.limpiar_contenedor()
        self.vista_actual = UsuarioVista(self.contenedor, controller=self)

    def registrar_usuario(self, id_, nombre, correo, contrasena, tipo):
        self.negocio_usuario.registrar_usuario(id_, nombre, correo, contrasena, tipo)

    def get_all_usuarios(self):
        return self.negocio_usuario.get_all_usuarios()

    # -------------------------------------------------------------
    # PASARELAS DE VOLUNTARIOS (CONECTADO AL CONTROLADOR REAL)
    # -------------------------------------------------------------
    def mostrar_registro_voluntarios(self):
        self.limpiar_contenedor()
        # El controlador se encarga de todo de manera interna
        controlador_vol = ControladorVoluntario(
            root=self.contenedor,
            servicio=self.voluntario_servicio,
            app_controller=self
        )
        # Guardamos la vista en el contenedor principal de la app
        self.vista_actual = controlador_vol.vista

    def registrar_voluntario(self, id_v, nom, tel, edad, corr, org):
        pass

    # -------------------------------------------------------------
    # PASARELAS DE JORNADAS
    # -------------------------------------------------------------
    def mostrar_registro_jornadas(self):
        self.limpiar_contenedor()

        # Instanciamos el controlador de jornadas pasándole el servicio ya conectado
        controlador_jornada = JornadaController(
            root=self.contenedor,
            servicio=self.voluntario_servicio,
            app_controller=self
        )
        # Asignamos la vista del controlador a la pantalla activa
        self.vista_actual = controlador_jornada.vista


if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()