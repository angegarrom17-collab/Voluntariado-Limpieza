class AnimalAfectado:

    def __init__(self, especie: str, estado: str, descripcion: str):
        # Información básica de la fauna encontrada
        self.especie = especie
        self.estado = estado
        self.descripcion = descripcion

    def to_dict(self) -> dict:
        # Convierte el objeto para almacenamiento en JSON
        return {
            "especie": self.especie,
            "estado": self.estado,
            "descripcion": self.descripcion
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Crea objeto desde archivo JSON
        return cls(
            data["especie"],
            data["estado"],
            data["descripcion"]
        )

    def __str__(self) -> str:
        # Representación simple del animal
        return f"Especie: {self.especie} - Estado: {self.estado}"