import json
import os

class VoluntarioRepositorio:
    def __init__(self, filename="voluntarios.json"):
        self.filename = filename
        self._voluntarios = []

        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            self._voluntarios = []
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            self._voluntarios = json.load(f)

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._voluntarios, f, indent=4)

    def obtener_todos(self):
        self._load()
        return self._voluntarios

    def agregar(self, voluntario):
        self._voluntarios.append(voluntario.to_dict())
        self._save()

    def eliminar(self, voluntario):
        # 1. Buscamos el voluntario en la lista y lo eliminamos
        if voluntario in self._voluntarios:
            self._voluntarios.remove(voluntario)
            # 2. Guardamos los cambios en el archivo JSON
            self._save()