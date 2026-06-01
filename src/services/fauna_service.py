from src.model.animal_afectado import AnimalAfectado
from src.model.basura_recolectada import BasuraRecolectada


class FaunaService:
    def __init__(self, fauna_repository):
        self.fauna_repository = fauna_repository

    def registrar_animal(self, id_animal: str, especie: str, estado: str, descripcion: str):
        if not id_animal.strip():
            raise ValueError("El ID no puede estar vacío")
        if not especie.strip():
            raise ValueError("La especie no puede estar vacía")

        estado_norm = estado.strip().lower()
        if estado_norm not in ["vivo", "herido", "muerto"]:
            raise ValueError("El estado debe ser: vivo, herido o muerto")

        for animal in self.obtener_animales():
            if str(getattr(animal, "idAnimal", "")).strip() == id_animal.strip():
                raise ValueError(f"Ya existe un animal registrado con el ID '{id_animal}'")

        animal = AnimalAfectado(id_animal, especie, estado_norm, descripcion)
        self.fauna_repository.agregar_animal(animal)

    def registrar_basura(self, id_basura: str, tipo_residuo: str, peso_kilos: float, fecha: str):
        if not id_basura.strip():
            raise ValueError("El ID no puede estar vacío")
        if not tipo_residuo.strip():
            raise ValueError("El tipo de residuo no puede estar vacío")
        if peso_kilos < 0:
            raise ValueError("El peso no puede ser negativo")
        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacía")

        for basur in self.obtener_basura():
            if str(getattr(basur, "idBasura", "")).strip() == id_basura.strip():
                raise ValueError(f"Ya existe un registro de basura con el ID '{id_basura}'")

        basura = BasuraRecolectada(id_basura, tipo_residuo, peso_kilos, fecha)
        self.fauna_repository.agregar_basura(basura)

    def obtener_animales(self):
        return self.fauna_repository.obtener_animales()

    def obtener_basura(self):
        return self.fauna_repository.obtener_basura()

    def obtener_resumen_fauna(self):
        animales = self.obtener_animales()
        basura = self.obtener_basura()

        total_animales = len(animales)

        animales_heridos = sum(1 for ani in animales if getattr(ani, "estado", "").strip().lower() == "herido")
        animales_muertos = sum(1 for ani in animales if getattr(ani, "estado", "").strip().lower() == "muerto")

        total_basura_kg = 0.0
        for b in basura:
            try:
                peso_texto = getattr(b, "pesoKilos", 0.0)
                total_basura_kg += float(peso_texto)
            except (ValueError, TypeError):
                continue

        return {
            "total_animales": total_animales,
            "animales_heridos": animales_heridos,
            "animales_muertos": animales_muertos,
            "total_basura_kg": total_basura_kg,
            "registros_basura": len(basura)
        }