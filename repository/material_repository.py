import json
import os
from model.material import Material

class MaterialRepository:

    def __init__(self, filename="materiales.json"):
        # Archivo donde se guardan los materiales
        self.filename = filename
        self._materiales = []
        self._materiales_by_id = {}
        self._load()

    def _load(self):
        # Carga los materiales desde el archivo JSON
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            material = Material.from_dict(item)
            self._materiales.append(material)
            self._materiales_by_id[material.idMaterial] = material

    def _save(self):
        # Guarda los materiales en el archivo
        data = [material.to_dict() for material in self._materiales]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, material: Material):
        # Agrega un nuevo material validando que no exista el ID
        if material.idMaterial in self._materiales_by_id:
            raise ValueError("Ya existe un material con ese ID")

        self._materiales.append(material)
        self._materiales_by_id[material.idMaterial] = material
        self._save()

    def get_by_id(self, idMaterial: str):
        # Busca un material por ID
        return self._materiales_by_id.get(idMaterial)

    def get_all(self):
        # Devuelve todos los materiales
        return list(self._materiales)