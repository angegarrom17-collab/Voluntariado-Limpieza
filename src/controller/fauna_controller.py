import tkinter as tk
from tkinter import messagebox
from src.repository.fauna_repository import FaunaRepository
from src.services.fauna_service import FaunaService
from src.view.fauna_view import FaunaVista


class FaunaController:
    # Cambié el orden a (parent, app_controller) para que coincida con tu AppController
    def __init__(self, parent, app_controller):
        self.root = parent
        self.app_controller = app_controller
        self.repo = FaunaRepository("animales.json")
        self.service = FaunaService(self.repo)
        self.vista = FaunaVista(parent, self)
        self.vista.pack(fill="both", expand=True)

    def registrar_animal(self, id_a, esp, est, desc):
        try:
            # 1. Intentamos registrar en el Service (aquí saltará el ValueError si pones "mal")
            self.service.registrar_animal(id_a, esp, est, desc)

            # 2. SI LLEGA AQUÍ, ES UN ÉXITO REAL
            messagebox.showinfo("Éxito", f"Animal '{esp}' registrado correctamente.")

            # 3. Le avisamos a la vista que limpie los campos y actualice su tabla
            if hasattr(self.vista, 'notificar_registro_exitoso'):
                self.vista.notificar_registro_exitoso()

        except ValueError as e:
            # Aquí frena en seco los estados incorrectos o IDs duplicados
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            # Errores del sistema con el JSON
            messagebox.showerror("Error del Sistema", f"No se pudo guardar: {str(e)}")

    def get_all_animales(self):
        try:
            return self.service.obtener_animales()
        except Exception:
            return []

    def buscar_animal(self, id_a):
        for a in self.service.obtener_animales():
            # CAMBIO: Usar idAnimal en lugar de id_animal
            if str(getattr(a, "idAnimal", "")).strip() == str(id_a).strip():
                return a
        return None

    def volver_inicio(self):
        self.app_controller.mostrar_principal()