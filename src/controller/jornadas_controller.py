import tkinter as tk
from tkinter import messagebox, ttk
from src.view.jornada_view import JornadaVistaModerna


class JornadaController:
    def __init__(self, parent, servicio, app_controller):
        self.root = parent
        self.servicio = servicio
        self.app_controller = app_controller
        self.vista = JornadaVistaModerna(self.root, controller=self)
        self.vista.pack(fill="both", expand=True)

    def registrar_nueva_jornada(self, id_j, fecha, desc, basura_str, obs, id_zona):
        # 1. Validar el formato numérico antes de enviarlo al servicio
        try:
            cantidad = int(basura_str)
        except ValueError:
            messagebox.showerror("Error de Formato", "La cantidad de basura (kg) debe ser un número entero.")
            return

        # 2. Intentar guardar en las capas internas
        try:
            # Llamamos al servicio. Si lanza un ValueError (ID duplicado, zona inválida),
            # la ejecución se detendrá inmediatamente AQUÍ y saltará al bloque 'except ValueError'
            self.servicio.registrar_jornada(id_j, fecha, desc, cantidad, obs, id_zona)

            # ESTE CÓDIGO SOLO SE EJECUTA SI EL SERVICIO SE COMPLETÓ SIN ERRORES
            messagebox.showinfo("Éxito Total", f"Jornada '{id_j}' registrada y guardada exitosamente en el JSON.")
            self.vista.limpiar_campos()

        except ValueError as err:
            # Aquí caen TODOS los errores controlados que programamos en tu Service
            messagebox.showerror("Error de Validación", str(err))
        except Exception as err:
            # Aquí caen problemas del sistema, archivos JSON corruptos, etc.
            messagebox.showerror("Error Crítico de Sistema", f"No se pudo escribir en el archivo:\n{str(err)}")
            print(f"--- TRACEBACK ERROR SISTEMA ---\n{err}\n-------------------------------")

    def mostrar_menu_principal(self):
        self.app_controller.mostrar_principal()

    def ver_reporte_jornadas(self):
        try:
            lista = self.servicio.obtener_reporte_jornadas()
        except Exception:
            lista = []

        win = tk.Toplevel(self.root)
        win.title("Reporte Jornadas")
        win.geometry("850x400")
        win.configure(bg="#BEEED9")
        win.grab_set()

        tk.Label(win, text="REPORTE DE JORNADAS", font=("Segoe UI", 14, "bold"), fg="#1b4f72", bg="#BEEED9").pack(
            pady=15)

        frm = tk.Frame(win)
        frm.pack(expand=True, fill="both", padx=20, pady=10)

        sc = tk.Scrollbar(frm)
        sc.pack(side="right", fill="y")

        cols = ("id", "fecha", "descripcion", "basura", "voluntarios")
        tb = ttk.Treeview(frm, columns=cols, show="headings", yscrollcommand=sc.set, height=12)
        sc.config(command=tb.yview)

        tb.heading("id", text="ID");
        tb.column("id", width=100, anchor="center")
        tb.heading("fecha", text="Fecha");
        tb.column("fecha", width=120, anchor="center")
        tb.heading("descripcion", text="Descripción");
        tb.column("descripcion", width=280, anchor="w")
        tb.heading("basura", text="Basura (kg)");
        tb.column("basura", width=120, anchor="center")
        tb.heading("voluntarios", text="Voluntarios");
        tb.column("voluntarios", width=130, anchor="center")
        tb.pack(expand=True, fill="both")

        for j in lista:
            tb.insert("", tk.END, values=(
                j.get("ID", j.get("id_jornada", "")),
                j.get("Fecha", j.get("fecha", "")),
                j.get("Descripcion", j.get("descripcion", "")),
                j.get("Basura (kg)", j.get("cantidad_basura_total", 0)),
                j.get("Voluntarios", 0)
            ))

        tk.Button(win, text="Cerrar", command=win.destroy).pack(pady=15)