import json
import os

class JornadaRepositorio:

    def __init__(self, filename="jornadas.json"):
        self.filename = filename
        self._jornadas = []
        self._load()

#--------------------------------------------------------------------
    def _load(self):

        if not os.path.exists(self.filename):
            self._jornadas = []
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            self._jornadas = json.load(f)

#--------------------------------------------------------------------
    def _save(self):

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._jornadas, f, indent=4)

#--------------------------------------------------------------------
    def obtener_todos(self):

        self._load()
        return self._jornadas

#--------------------------------------------------------------------
    def agregar(self, jornada):

        self._jornadas.append(jornada.to_dict())
        self._save()