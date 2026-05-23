class Usuario:
    def __init__(self, idUsuario: str, nombre: str, correo: str, tipo: str):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.tipo = tipo

    def to_dict(self) -> dict:
        return {
            "idUsuario": self.idUsuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "tipo": self.tipo
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["idUsuario"], data["nombre"], data["correo"], data["tipo"])

    def __str__(self) -> str:
        return f"ID: {self.idUsuario} - Nombre: {self.nombre} - Correo: {self.correo} - Tipo: {self.tipo}"