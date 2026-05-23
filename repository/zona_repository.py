import json
import os
from model.zona import Zona

class ZonaRepository:
    def __init__(self, filename="zonas.json"):
        self.filename = filename
        self._zonas = []
        self._zonas_by_id = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            zona = Zona.from_dict(item)
            self._zonas.append(zona)
            self._zonas_by_id[zona.id_zona] = zona

    def _save(self):
        data = [zona.to_dict() for zona in self._zonas]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add(self, zona: Zona):
        if zona.id_zona in self._zonas_by_id:
            raise ValueError("Ya existe una zona con ese ID")
        self._zonas.append(zona)
        self._zonas_by_id[zona.id_zona] = zona
        self._save()

    def get_by_id(self, id_zona: int):
        return self._zonas_by_id.get(id_zona)

    def get_all(self):
        return list(self._zonas)

    def exists(self, id_zona: int) -> bool:
        return id_zona in self._zonas_by_id