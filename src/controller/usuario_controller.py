from src.repository.usuario_repository import UsuarioRepository
from src.services.usuario_service import UsuarioService
from src.view.usuario_view import UsuarioVista

class ControladorUsuario:
    def __init__(self, parent, app_controller):
        self.app_controller = app_controller
        self.repo = UsuarioRepository("usuarios.json")
        self.service = UsuarioService(self.repo)
        self.vista = UsuarioVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_usuario(self, id_usuario, nombre, correo, contrasena, tipo):
        self.service.registrar_usuario(id_usuario, nombre, correo, contrasena, tipo)

    def get_all_usuarios(self):
        return self.service.get_all_usuarios()

    def eliminar_usuario(self, id_usuario):
        self.repo.delete(id_usuario)

    def volver_inicio(self):
        self.app_controller.mostrar_principal()
