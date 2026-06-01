import tkinter as tk
from tkinter import messagebox, ttk
from src.repository.voluntario_repository import VoluntarioRepositorio
from src.services.voluntario_service import VoluntarioService
from src.view.voluntario_view import VoluntarioVistaModerna

class ControladorVoluntario:
    def __init__(self, parent, app_controller):
        self.root = parent
        self.app_controller = app_controller
        self.repo = VoluntarioRepositorio("src/voluntarios.json")
        self.service = VoluntarioService(self.repo)
        self.vista = VoluntarioVistaModerna(self.root, controller=self)
        self.vista.pack(fill="both", expand=True)

    def registrar_voluntario(self, id_v, nom, tel, edad_str, corr, org):
        try:
            edad = int(edad_str)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un numero entero.")
            return
        try:
            self.service.registrar_voluntario(id_v, nom, tel, edad, corr, org)
            messagebox.showinfo("Exito", f"Voluntario '{nom}' registrado.")
            self.vista._limpiar_campos()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_tabla_voluntarios(self):
        lista = self.service.obtener_todos_los_voluntarios()
        win = tk.Toplevel(self.root)
        win.title("Voluntarios Registrados")
        win.geometry("850x400")
        win.configure(bg="#BEEED9")
        win.grab_set()
        tk.Label(win, text="LISTADO DE VOLUNTARIOS", font=("Segoe UI", 14, "bold"), fg="#1b4f72", bg="#BEEED9").pack(pady=15)
        frm = tk.Frame(win)
        frm.pack(expand=True, fill="both", padx=20, pady=10)
        sc = tk.Scrollbar(frm)
        sc.pack(side="right", fill="y")
        cols = ("id", "nombre", "telefono", "edad", "correo", "organizacion")
        tb = ttk.Treeview(frm, columns=cols, show="headings", yscrollcommand=sc.set, height=12)
        sc.config(command=tb.yview)
        for c in cols:
            tb.heading(c, text=c.replace("_", " ").title())
            tb.column(c, width=130, anchor="center")
        tb.pack(expand=True, fill="both")
        for v in lista:
            tb.insert("", tk.END, values=(v.get("id_voluntario"), v.get("nombre"), v.get("telefono"), v.get("edad"), v.get("correo"), v.get("organizacion")))
        tk.Button(win, text="Cerrar", command=win.destroy).pack(pady=15)

    def mostrar_menu_principal(self):
        self.app_controller.mostrar_principal()

    def eliminar_voluntario_por_id(self, id_voluntario):
        try:
            self.service.eliminar_voluntario(id_voluntario)

            messagebox.showinfo("Éxito", f"El voluntario con ID '{id_voluntario}' fue eliminado.")
            self.vista._limpiar_campos()

        except ValueError as e:
            messagebox.showerror("Error", str(e))