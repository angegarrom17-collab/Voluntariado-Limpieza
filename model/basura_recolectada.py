class BasuraRecolectada:

    def __init__(self, tipoResiduo: str, pesoKilos: float, fecha: str):
        # Datos del residuo recolectado durante una jornada
        self.tipoResiduo = tipoResiduo
        self.pesoKilos = pesoKilos
        self.fecha = fecha

    def to_dict(self) -> dict:
        return {
            "tipoResiduo": self.tipoResiduo,
            "pesoKilos": self.pesoKilos,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Reconstruye el objeto desde un archivo
        return cls(
            data["tipoResiduo"],
            data["pesoKilos"],
            data["fecha"]
        )

    def __str__(self) -> str:
        # Muestra información resumida del registro
        return f"Tipo: {self.tipoResiduo} - Peso: {self.pesoKilos} kg - Fecha: {self.fecha}"