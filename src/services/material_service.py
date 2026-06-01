from src.model.material import Material


class MaterialService:
    def __init__(self, material_repository):
        self.material_repository = material_repository

    def registrar_material(self, idMaterial, nombre, unidadMedida, cantidadDisponible):
        if not idMaterial.strip():
            raise ValueError("El ID no puede estar vacio")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        if not unidadMedida.strip():
            raise ValueError("La unidad de medida no puede estar vacia")
        if cantidadDisponible < 0:
            raise ValueError("La cantidad no puede ser negativa")
        material = Material(idMaterial, nombre, unidadMedida, cantidadDisponible)
        self.material_repository.add(material)

    def usar_material(self, idMaterial, cantidad):
        material = self.material_repository.get_by_id(idMaterial)
        if not material:
            raise ValueError("Material no encontrado")
        if material.cantidadDisponible < cantidad:
            raise ValueError("No hay suficiente stock")
        material.cantidadDisponible -= cantidad
        self.material_repository.save()

    def obtener_materiales(self):
        return self.material_repository.get_all()