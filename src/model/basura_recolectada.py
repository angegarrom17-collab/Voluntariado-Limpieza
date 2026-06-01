class BasuraRecolectada:
    def __init__(self, idBasura: str, tipoResiduo: str, pesoKilos: float, fecha: str):
        self.idBasura = idBasura
        self.tipoResiduo = tipoResiduo
        self.pesoKilos = pesoKilos
        self.fecha = fecha

    def to_dict(self) -> dict:
        return {
            "idBasura": self.idBasura,
            "tipoResiduo": self.tipoResiduo,
            "pesoKilos": self.pesoKilos,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data: dict):
        # CORRECCIÓN DE SEGURIDAD: Convertimos obligatoriamente el peso a float
        try:
            peso = float(data.get("pesoKilos", 0.0))
        except (ValueError, TypeError):
            peso = 0.0

        return cls(
            data.get("idBasura", ""),
            data.get("tipoResiduo", ""),
            peso,
            data.get("fecha", "")
        )

    def __str__(self) -> str:
        return f"ID: {self.idBasura} - Tipo: {self.tipoResiduo} - Peso: {self.pesoKilos} kg - Fecha: {self.fecha}"