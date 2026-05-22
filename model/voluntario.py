class Voluntario:
    def __init__(self, idVoluntario: str, nombre: str, telefono:str, edad:int, correo:str, organizacion:str):
        self.idVoluntario = idVoluntario
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        self.correo = correo
        self.organizacion = organizacion


    def to_dict(self) -> dict:
        return {
            "idVoluntario": self.idVoluntario,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "edad": self.edad,
            "correo":self.correo,
            "organizacion":self.organizacion
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["idVoluntario"], data["nombre"], data["telefono"], data["edad"], data["correo"], data["organizacion"])

    def __str__(self) -> str:
        return f"ID: {self.idVoluntario} - Nombre: {self.nombre} - Telefono: {self.telefono} - Edad: {self.edad} - Correo: {self.correo} - Organizacion: {self.organizacion}"
