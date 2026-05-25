class Material:

    def __init__(self, idMaterial: str, nombre: str, unidadMedida: str, cantidadDisponible: int):

        # Atributos básicos del material en inventario
        self.idMaterial = idMaterial
        self.nombre = nombre
        self.unidadMedida = unidadMedida
        self.cantidadDisponible = cantidadDisponible

    def to_dict(self) -> dict:
        return {
            "idMaterial": self.idMaterial,
            "nombre": self.nombre,
            "unidadMedida": self.unidadMedida,
            "cantidadDisponible": self.cantidadDisponible
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Crea un objeto Material a partir de un diccionario
        return cls(
            data["idMaterial"],
            data["nombre"],
            data["unidadMedida"],
            data["cantidadDisponible"]
        )

    def __str__(self) -> str:
        # Representación en texto del material
        return f"ID: {self.idMaterial} - Nombre: {self.nombre} - Cantidad: {self.cantidadDisponible} {self.unidadMedida}"
