import tkinter as tk
from view.principal_view import PrincipalView
from view.usuario_view import UsuarioVista
from view.voluntario_view import VoluntarioVistaModerna
from view.jornada_view import JornadaVistaModerna
from view.zona_view import ZonaVista

# Importamos tus controladores reales de negocio
from controller.usuario_controller import ControladorUsuario
from controller.zona_controller import ControladorZona  # 🚨 Sincronizado con tu nombre exacto


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

        # 📍 Instancia del negocio de zonas (Sincronizado con ControladorZona)
        self.negocio_zona = ControladorZona()
        self.negocio_zona.set_volver_callback(self.mostrar_menu_principal)

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
        # Transfiere los parámetros directamente a tu validador del ControladorZona
        self.negocio_zona.registrar_zona(id_zona, nombre_zona, ubicacion, nivel_contaminacion, descripcion)

    def get_all_zonas(self):
        # Solicita la colección real de objetos Zona guardados en zonas.json
        return self.negocio_zona.get_all_zonas()

    # -------------------------------------------------------------
    # PASARELAS DE OTROS MÓDULOS
    # -------------------------------------------------------------
    def mostrar_registro_usuarios(self):
        self.limpiar_contenedor()
        self.vista_actual = UsuarioVista(self.contenedor, controller=self)

    def registrar_usuario(self, id_, nombre, correo, contrasena, tipo):
        self.negocio_usuario.registrar_usuario(id_, nombre, correo, contrasena, tipo)

    def get_all_usuarios(self):
        return self.negocio_usuario.get_all_usuarios()

    def mostrar_registro_voluntarios(self):
        self.limpiar_contenedor()
        self.vista_actual = VoluntarioVistaModerna(self.contenedor, controller=self)
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_registro_jornadas(self):
        self.limpiar_contenedor()
        self.vista_actual = JornadaVistaModerna(self.contenedor, controller=self)
        self.vista_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()