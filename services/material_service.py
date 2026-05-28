from model.material import Material

class MaterialService:
    def __init__(self, material_repository):
        # Conexión con el repositorio
        self.material_repository = material_repository

    def registrar_material(self, idMaterial: str, nombre: str, unidadMedida: str, cantidadDisponible: int):

        # Validaciones básicas
        if not idMaterial.strip():
            raise ValueError("El ID no puede estar vacío")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not unidadMedida.strip():
            raise ValueError("La unidad de medida no puede estar vacía")

        if cantidadDisponible < 0:
            raise ValueError("La cantidad no puede ser negativa")

        material = Material(idMaterial, nombre, unidadMedida, cantidadDisponible)
        self.material_repository.add(material)

    def usar_material(self, idMaterial: str, cantidad: int):
        # Reduce el stock al usar materiales
        material = self.material_repository.get_by_id(idMaterial)

        if not material:
            raise ValueError("Material no encontrado")

        if material.cantidadDisponible < cantidad:
            raise ValueError("No hay suficiente stock")

        material.cantidadDisponible -= cantidad

    def obtener_materiales(self):
        return self.material_repository.get_all()

    