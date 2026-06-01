import json
import os
from src.model.usuario import Usuario

class UsuarioRepository:
    def __init__(self, filename="usuarios.json"):
        self.filename = filename
        self._usuarios = []
        self._usuarios_by_id = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            usuario = Usuario.from_dict(item)
            self._usuarios.append(usuario)
            self._usuarios_by_id[usuario.id_usuario] = usuario

    def _save(self):
        data = [usuario.to_dict() for usuario in self._usuarios]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add(self, usuario: Usuario):
        if usuario.id_usuario in self._usuarios_by_id:
            raise ValueError("Ya existe un usuario con ese ID")
        self._usuarios.append(usuario)
        self._usuarios_by_id[usuario.id_usuario] = usuario
        self._save()

    def delete(self, id_usuario: str):
        usuario = self._usuarios_by_id.pop(id_usuario, None)
        if usuario is None:
            raise ValueError(f"No existe usuario con ID {id_usuario}")
        self._usuarios = [u for u in self._usuarios if u.id_usuario != id_usuario]
        self._save()

    def get_by_id(self, id_usuario: str):
        return self._usuarios_by_id.get(id_usuario)

    def get_by_correo(self, correo: str):
        for usuario in self._usuarios:
            if usuario.correo == correo:
                return usuario
        return None

    def get_all(self):
        return list(self._usuarios)

    def exists(self, id_usuario: str) -> bool:
        return id_usuario in self._usuarios_by_id
