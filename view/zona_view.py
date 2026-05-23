import tkinter as tk
from tkinter import ttk, messagebox


class ZonaVista(tk.Frame):

    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self._build()

    def _build(self):
        tk.Label(
            self,
            text="Registrar Zona",
            font=("Arial", 13, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="ID Zona:", font=("Arial", 11)).grid(
            row=1, column=0, padx=10, pady=6, sticky="e")
        self.entry_id_zona = tk.Entry(self, width=30)
        self.entry_id_zona.grid(row=1, column=1, padx=10, pady=6)

        tk.Label(self, text="Nombre:", font=("Arial", 11)).grid(
            row=2, column=0, padx=10, pady=6, sticky="e")
        self.entry_nombre_zona = tk.Entry(self, width=30)
        self.entry_nombre_zona.grid(row=2, column=1, padx=10, pady=6)

        tk.Label(self, text="Ubicación:", font=("Arial", 11)).grid(
            row=3, column=0, padx=10, pady=6, sticky="e")
        self.entry_ubicacion = tk.Entry(self, width=30)
        self.entry_ubicacion.grid(row=3, column=1, padx=10, pady=6)

        tk.Label(self, text="Nivel Contaminación:", font=("Arial", 11)).grid(
            row=4, column=0, padx=10, pady=6, sticky="e")
        self.entry_nivel_contaminacion = tk.Entry(self, width=30)
        self.entry_nivel_contaminacion.grid(row=4, column=1, padx=10, pady=6)

        tk.Label(self, text="Descripción:", font=("Arial", 11)).grid(
            row=5, column=0, padx=10, pady=6, sticky="e")
        self.entry_descripcion = tk.Entry(self, width=30)
        self.entry_descripcion.grid(row=5, column=1, padx=10, pady=6)

        tk.Button(
            self,
            text="Registrar Zona",
            font=("Arial", 11, "bold"),
            command=self._registrar
        ).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(
            self,
            text="Lista de Zonas",
            font=("Arial", 12, "bold")
        ).grid(row=7, column=0, columnspan=2, pady=(15, 5))

        nombres_columnas = ("ID", "Nombre", "Ubicación", "Contaminación")
        self.tabla_zonas = ttk.Treeview(
            self,
            columns=nombres_columnas,
            show="headings",
            height=6
        )
        for nombre_columna in nombres_columnas:
            self.tabla_zonas.heading(nombre_columna, text=nombre_columna)
            self.tabla_zonas.column(nombre_columna, width=130)
        self.tabla_zonas.grid(row=8, column=0, columnspan=2, padx=10)

        tk.Button(
            self,
            text="Actualizar lista",
            command=self._cargar_tabla
        ).grid(row=9, column=0, columnspan=2, pady=8)

        self._cargar_tabla()

    def _registrar(self):
        try:
            id_zona = self.entry_id_zona.get()
            nombre_zona = self.entry_nombre_zona.get()
            ubicacion = self.entry_ubicacion.get()
            nivel_contaminacion = self.entry_nivel_contaminacion.get()
            descripcion = self.entry_descripcion.get()

            self.controller.registrar_zona(
                int(id_zona), nombre_zona, ubicacion,
                nivel_contaminacion, descripcion
            )
            messagebox.showinfo("Éxito", "Zona registrada.")
            self._limpiar_campos()
            self._cargar_tabla()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def _limpiar_campos(self):
        self.entry_id_zona.delete(0, tk.END)
        self.entry_nombre_zona.delete(0, tk.END)
        self.entry_ubicacion.delete(0, tk.END)
        self.entry_nivel_contaminacion.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_zonas.get_children():
            self.tabla_zonas.delete(fila)
        for zona in self.controller.get_all_zonas():
            self.tabla_zonas.insert(
                "", "end",
                values=(zona.id_zona, zona.nombre_zona,
                        zona.ubicacion, zona.nivel_contaminacion)
            )