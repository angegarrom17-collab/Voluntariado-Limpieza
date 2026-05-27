import json
import os
from model.animal_afectado import AnimalAfectado
from model.basura_recolectada import BasuraRecolectada

class FaunaRepository:
    def __init__(self, filename_animales="animales.json", filename_basura="basura.json"):
        # Archivos separados para animales y residuos
        self.filename_animales = filename_animales
        self.filename_basura = filename_basura
        self._animales = []
        self._basura = []
        self._load()

    def _load(self):
        # Cargar datos existentes si los archivos ya existen
        if os.path.exists(self.filename_animales):
            with open(self.filename_animales, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._animales = [AnimalAfectado.from_dict(item) for item in data]

        if os.path.exists(self.filename_basura):
            with open(self.filename_basura, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._basura = [BasuraRecolectada.from_dict(item) for item in data]

    def _save_animales(self):
        # Guarda lista de animales
        data = [animal.to_dict() for animal in self._animales]
        with open(self.filename_animales, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def _save_basura(self):
        # Guarda registros de basura
        data = [b.to_dict() for b in self._basura]
        with open(self.filename_basura, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def agregar_animal(self, animal: AnimalAfectado):
        # Registra un nuevo animal afectado
        self._animales.append(animal)
        self._save_animales()

    def agregar_basura(self, basura: BasuraRecolectada):
        # Registra basura recolectada
        self._basura.append(basura)
        self._save_basura()

    def obtener_animales(self):
        return self._animales

    def obtener_basura(self):
        return self._basura