from model.usuario import Usuario
from repository.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService


class ControladorUsuario:

    def __init__(self):
        self.repositorio_usuario = UsuarioRepository("usuarios.json")
        self.servicio_usuario = UsuarioService(self.repositorio_usuario)
        self.callback_volver = None

    def set_volver_callback(self, callback):
        self.callback_volver = callback

    def volver_inicio(self):
        if self.callback_volver:
            self.callback_volver()

    def registrar_usuario(self, id_usuario, nombre, correo, contrasena, tipo):
        self.servicio_usuario.registrar_usuario(id_usuario, nombre, correo, contrasena, tipo)

    def get_all_usuarios(self):
        return self.servicio_usuario.get_all_usuarios()

    def iniciar_sesion(self, correo, contrasena):
        return self.servicio_usuario.iniciar_sesion(correo, contrasena)

    def es_encargado(self, usuario):
        return self.servicio_usuario.es_encargado(usuario)