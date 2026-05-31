import tkinter as tk
from view.principal_view import PrincipalView
from view.usuario_view import UsuarioVista
from view.voluntario_view import VoluntarioVistaModerna
from view.jornada_view import JornadaVistaModerna

# Importamos tu controlador real de negocio
from controller.usuario_controller import ControladorUsuario


class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto OFC Desarrollo - Protección del Mar")
        self.root.geometry("1000x650")

        # Contenedor dinámico para intercambiar los Frames en la misma ventana
        self.contenedor = tk.Frame(self.root)
        self.contenedor.pack(fill="both", expand=True)

        # 🚨 Instanciamos tu controlador de negocio real aquí
        self.negocio_usuario = ControladorUsuario()

        # Le configuramos su callback de salida apuntando a nuestro menú principal
        self.negocio_usuario.set_volver_callback(self.mostrar_menu_principal)

        self.vista_actual = None
        self.mostrar_menu_principal()

    def limpiar_contenedor(self):
        """Elimina la vista activa para dar paso a la siguiente."""
        if self.vista_actual is not None:
            self.vista_actual.destroy()

    def mostrar_menu_principal(self):
        self.limpiar_contenedor()
        # Inicializa la vista del menú pasando 'self' para la navegación por botones
        self.vista_actual = PrincipalView(self.contenedor, controller=self)

    # -------------------------------------------------------------
    # PASARELAS DEL MÓDULO DE USUARIOS
    # -------------------------------------------------------------
    def mostrar_registro_usuarios(self):
        self.limpiar_contenedor()
        # Levantamos la vista pasándole 'self' como su controlador de interfaz
        self.vista_actual = UsuarioVista(self.contenedor, controller=self)

    def registrar_usuario(self, id_, nombre, correo, contrasena, tipo):
        # El main NO procesa datos; se los transfiere directo a tu lógica de servicios
        self.negocio_usuario.registrar_usuario(id_, nombre, correo, contrasena, tipo)

    def get_all_usuarios(self):
        # El main le solicita los objetos a tu controlador persistido en JSON
        return self.negocio_usuario.get_all_usuarios()

    def volver_inicio(self):
        # Cuando el botón '← Salir' ejecute volver_inicio, llamamos al callback de negocio
        self.negocio_usuario.volver_inicio()

    # -------------------------------------------------------------
    # PASARELAS DE OTROS MÓDULOS (Voluntarios, Jornadas, etc.)
    # -------------------------------------------------------------
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