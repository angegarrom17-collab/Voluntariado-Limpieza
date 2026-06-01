class Voluntario:
    def __init__(self, id_voluntario: str, nombre: str, telefono:str, edad:int, correo:str, organizacion:str):
        self.id_voluntario = id_voluntario
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        self.correo = correo
        self.organizacion = organizacion

    def to_dict(self) -> dict:
        return {
            "id_voluntario": self.id_voluntario,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "edad": self.edad,
            "correo":self.correo,
            "organizacion":self.organizacion
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id_voluntario"], data["nombre"], data["telefono"], data["edad"], data["correo"], data["organizacion"])

    def __str__(self) -> str:
        return f"ID: {self.id_voluntario} - Nombre: {self.nombre} - Telefono: {self.telefono} - Edad: {self.edad} - Correo: {self.correo} - Organizacion: {self.organizacion}"