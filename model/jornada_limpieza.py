class JornadaLimpieza:

    def __init__(self, id_jornada: str, fecha: str,descripcion: str, cantidad_basura_total: int,observaciones: str):
        self.id_jornada = id_jornada
        self.fecha = fecha
        self.descripcion = descripcion
        self.cantidad_basura_total = cantidad_basura_total
        self.observaciones = observaciones

        self.voluntarios = []

#--------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "id_jornada": self.id_jornada,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "cantidad_basura_total": self.cantidad_basura_total,
            "observaciones": self.observaciones,
            "voluntarios": self.voluntarios
        }

#--------------------------------------------------------------------

    @classmethod
    def from_dict(cls, data: dict):
        jornada = cls(data["id_jornada"],
            data["fecha"],
            data["descripcion"],
            data["cantidad_basura_total"],
            data["observaciones"]
        )
        jornada.voluntarios = data.get("voluntarios", [])
        return jornada

#--------------------------------------------------------------------

    def __str__(self) -> str:
        return (
            f"ID Jornada: {self.id_jornada} - "
            f"Fecha: {self.fecha} - "
            f"Descripcion: {self.descripcion} - "
            f"Cantidad Basura Total: {self.cantidad_basura_total} kg - "
            f"Observaciones: {self.observaciones}"
        )