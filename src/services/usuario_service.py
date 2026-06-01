import hashlib
from src.model.usuario import Usuario

class UsuarioService:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def _cifrar_contrasena(self, contrasena: str) -> str:
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar_usuario(self, id_usuario: str, nombre: str,
                          correo: str, contrasena: str, tipo: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if "@" not in correo:
            raise ValueError("El correo no tiene formato válido")
        if len(contrasena) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        if tipo not in ["encargado"]:
            raise ValueError("Tipo de usuario no válido. Solo se acepta: encargado")

        contrasena_cifrada = self._cifrar_contrasena(contrasena)
        usuario = Usuario(id_usuario, nombre, correo, contrasena_cifrada, tipo)
        self.usuario_repository.add(usuario)

    def iniciar_sesion(self, correo: str, contrasena: str) -> Usuario:
        usuario = self.usuario_repository.get_by_correo(correo)
        if usuario is None:
            raise ValueError("Usuario no encontrado")
        if usuario.contrasena != self._cifrar_contrasena(contrasena):
            raise ValueError("Contraseña incorrecta")
        return usuario

    def es_encargado(self, usuario: Usuario) -> bool:
        return usuario.tipo == "encargado"

    def get_all_usuarios(self):
        return self.usuario_repository.get_all()