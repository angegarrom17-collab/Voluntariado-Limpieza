import json
import os
from src.model.animal_afectado import AnimalAfectado
from src.model.basura_recolectada import BasuraRecolectada

class FaunaRepository:
    def __init__(self, filename_animales="animales.json", filename_basura="basura.json"):
        self.filename_animales = filename_animales
        self.filename_basura = filename_basura
        self._animales = []
        self._basura = []
        self._load()

    def _load(self):
        # Carga segura de animales
        if os.path.exists(self.filename_animales):
            try:
                with open(self.filename_animales, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Si el archivo está vacío o no es una lista, asegurar una lista vacía
                    if isinstance(data, list):
                        self._animales = [AnimalAfectado.from_dict(item) for item in data]
                    else:
                        self._animales = []
            except (json.JSONDecodeError, ValueError):
                self._animales = []
        else:
            self._animales = []

        # Carga segura de basura
        if os.path.exists(self.filename_basura):
            try:
                with open(self.filename_basura, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self._basura = [BasuraRecolectada.from_dict(item) for item in data]
                    else:
                        self._basura = []
            except (json.JSONDecodeError, ValueError):
                self._basura = []
        else:
            self._basura = []

    def _save_animales(self):
        data = [animal.to_dict() for animal in self._animales]
        with open(self.filename_animales, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def _save_basura(self):
        data = [b.to_dict() for b in self._basura]
        with open(self.filename_basura, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def agregar_animal(self, animal: AnimalAfectado):
        self._load()  # Recargamos para asegurar consistencia con el disco
        self._animales.append(animal)
        self._save_animales()

    def agregar_basura(self, basura: BasuraRecolectada):
        self._load()  # Recargamos para asegurar consistencia con el disco
        self._basura.append(basura)
        self._save_basura()

    def obtener_animales(self):
        self._load()  # Forzamos la lectura fresca del JSON
        return self._animales

    def obtener_basura(self):
        self._load()  # Forzamos la lectura fresca del JSON
        return self._basura