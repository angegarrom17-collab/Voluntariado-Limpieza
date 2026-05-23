import tkinter as tk
from tkinter import ttk, messagebox


class UsuarioVista(tk.Frame):

    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self._build()

    def _build(self):
        tk.Label(
            self,
            text="Registrar Usuario",
            font=("Arial", 13, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="ID:", font=("Arial", 11)).grid(
            row=1, column=0, padx=10, pady=6, sticky="e")
        self.entry_id = tk.Entry(self, width=30)
        self.entry_id.grid(row=1, column=1, padx=10, pady=6)

        tk.Label(self, text="Nombre:", font=("Arial", 11)).grid(
            row=2, column=0, padx=10, pady=6, sticky="e")
        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=6)

        tk.Label(self, text="Correo:", font=("Arial", 11)).grid(
            row=3, column=0, padx=10, pady=6, sticky="e")
        self.entry_correo = tk.Entry(self, width=30)
        self.entry_correo.grid(row=3, column=1, padx=10, pady=6)

        tk.Label(self, text="Contraseña:", font=("Arial", 11)).grid(
            row=4, column=0, padx=10, pady=6, sticky="e")
        self.entry_contrasena = tk.Entry(self, width=30, show="*")
        self.entry_contrasena.grid(row=4, column=1, padx=10, pady=6)

        tk.Label(self, text="Tipo (encargado):", font=("Arial", 11)).grid(
            row=5, column=0, padx=10, pady=6, sticky="e")
        self.entry_tipo = tk.Entry(self, width=30)
        self.entry_tipo.grid(row=5, column=1, padx=10, pady=6)

        tk.Button(
            self,
            text="Registrar",
            font=("Arial", 11, "bold"),
            command=self._registrar
        ).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(
            self,
            text="Lista de Usuarios",
            font=("Arial", 12, "bold")
        ).grid(row=7, column=0, columnspan=2, pady=(15, 5))

        nombres_columnas = ("ID", "Nombre", "Correo", "Tipo")
        self.tabla_usuarios = ttk.Treeview(
            self,
            columns=nombres_columnas,
            show="headings",
            height=6
        )
        for nombre_columna in nombres_columnas:
            self.tabla_usuarios.heading(nombre_columna, text=nombre_columna)
            self.tabla_usuarios.column(nombre_columna, width=120)
        self.tabla_usuarios.grid(row=8, column=0, columnspan=2, padx=10)

        tk.Button(
            self,
            text="Actualizar lista",
            command=self._cargar_tabla
        ).grid(row=9, column=0, columnspan=2, pady=8)

        self._cargar_tabla()

    def _registrar(self):
        try:
            id_usuario = self.entry_id.get()
            nombre = self.entry_nombre.get()
            correo = self.entry_correo.get()
            contrasena = self.entry_contrasena.get()
            tipo = self.entry_tipo.get()

            self.controller.registrar_usuario(
                int(id_usuario), nombre, correo, contrasena, tipo
            )
            messagebox.showinfo("Éxito", "Usuario registrado.")
            self._limpiar_campos()
            self._cargar_tabla()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def _limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_contrasena.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(fila)
        for usuario in self.controller.get_all_usuarios():
            self.tabla_usuarios.insert(
                "", "end",
                values=(usuario.id_usuario, usuario.nombre,
                        usuario.correo, usuario.tipo)
            )