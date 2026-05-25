class JornadaLimpieza:

    def __init__(self, idJornada: str, fecha: str,descripcion: str, cantidadBasuraTotal: int,observaciones: str):
        self.idJornada = idJornada
        self.fecha = fecha
        self.descripcion = descripcion
        self.cantidadBasuraTotal = cantidadBasuraTotal
        self.observaciones = observaciones


    def to_dict(self) -> dict:
        return {
            "idJornada": self.idJornada,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "cantidadBasuraTotal": self.cantidadBasuraTotal,
            "observaciones": self.observaciones
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["idJornada"],
            data["fecha"],
            data["descripcion"],
            data["cantidadBasuraTotal"],
            data["observaciones"]
        )

    def __str__(self) -> str:
        return (
            f"ID Jornada: {self.idJornada} - "
            f"Fecha: {self.fecha} - "
            f"Descripcion: {self.descripcion} - "
            f"Cantidad Basura Total: {self.cantidadBasuraTotal} kg - "
            f"Observaciones: {self.observaciones}"
        )