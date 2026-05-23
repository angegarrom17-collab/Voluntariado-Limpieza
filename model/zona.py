class Zona:
    def __init__(self, id_zona: int, nombre_zona: str,
                 ubicacion: str, nivel_contaminacion: str, descripcion: str):
        self.id_zona = id_zona
        self.nombre_zona = nombre_zona
        self.ubicacion = ubicacion
        self.nivel_contaminacion = nivel_contaminacion
        self.descripcion = descripcion

    def to_dict(self) -> dict:
        return {
            "id_zona": self.id_zona,
            "nombre_zona": self.nombre_zona,
            "ubicacion": self.ubicacion,
            "nivel_contaminacion": self.nivel_contaminacion,
            "descripcion": self.descripcion
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["id_zona"], data["nombre_zona"], data["ubicacion"],
            data["nivel_contaminacion"], data["descripcion"]
        )

    def __str__(self) -> str:
        return f"Zona {self.id_zona}: {self.nombre_zona} - Contaminación: {self.nivel_contaminacion}"