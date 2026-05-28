class Usuario:
    def __init__(self, id_usuario: str, nombre: str,
                 correo: str, contrasena: str, tipo: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipo = tipo

    def to_dict(self) -> dict:
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena,
            "tipo": self.tipo
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["id_usuario"], data["nombre"],
            data["correo"], data["contrasena"], data["tipo"]
        )

    def __str__(self) -> str:
        return f"ID: {self.id_usuario} - Nombre: {self.nombre} - Tipo: {self.tipo}"