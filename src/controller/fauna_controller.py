import tkinter as tk
from tkinter import messagebox
from src.repository.fauna_repository import FaunaRepository
from src.services.fauna_service import FaunaService
from src.view.fauna_view import FaunaVista


class FaunaController:
    def __init__(self, parent, app_controller):
        self.root = parent
        self.app_controller = app_controller
        self.repo = FaunaRepository("animales.json")
        self.service = FaunaService(self.repo)
        self.vista = FaunaVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_animal(self, id_animal, especie, estado, descripcion):
        try:
            self.service.registrar_animal(id_animal, especie, estado, descripcion)
            messagebox.showinfo("Éxito", f"Animal '{especie}' registrado correctamente.")
            if hasattr(self.vista, 'notificar_registro_exitoso'):
                self.vista.notificar_registro_exitoso()
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error del Sistema", f"No se pudo guardar: {str(e)}")

    def get_all_animales(self):
        try:
            return self.service.obtener_animales()
        except Exception:
            return []

    def buscar_animal(self, id_animal):
        for animal in self.service.obtener_animales():
            if str(getattr(animal, "idAnimal", "")).strip() == str(id_animal).strip():
                return animal
        return None

    def eliminar_animal(self, id_animal):
        self.repo.eliminar_animal(id_animal)

    def volver_inicio(self):
        self.app_controller.mostrar_principal()
