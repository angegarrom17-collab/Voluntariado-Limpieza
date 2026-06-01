class AnimalAfectado:
    def __init__(self, id_animal: str, especie: str, estado: str, descripcion: str):
        self.idAnimal = id_animal
        self.especie = especie
        self.estado = estado
        self.descripcion = descripcion

    def to_dict(self) -> dict:
        return {
            "idAnimal": self.idAnimal,
            "especie": self.especie,
            "estado": self.estado,
            "descripcion": self.descripcion
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("idAnimal", ""),
            data["especie"],
            data["estado"],
            data["descripcion"]
        )

    def __str__(self) -> str:
        return f"ID: {self.idAnimal} - Especie: {self.especie} - Estado: {self.estado}"