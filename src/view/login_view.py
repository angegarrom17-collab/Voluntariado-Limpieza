import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Frame):

    def __init__(self, parent, controlador):
        super().__init__(parent)

        self.controlador = controlador

        self.crear_componentes()

    def crear_componentes(self):

        ttk.Label(
            self,
            text="Sistema de Voluntariado y Limpieza",
            font=("Arial", 14, "bold")
        ).pack(pady=20)

        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Label(frame, text="Usuario:").grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_usuario = ttk.Entry(frame, width=25)
        self.txt_usuario.grid(row=0, column=1)

        ttk.Label(frame, text="Contraseña:").grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_password = ttk.Entry(
            frame,
            width=25,
            show="*"
        )
        self.txt_password.grid(row=1, column=1)

        ttk.Button(
            self,
            text="Iniciar Sesión",
            command=self.validar_login
        ).pack(pady=15)

    def validar_login(self):

        usuario = self.txt_usuario.get()
        password = self.txt_password.get()

        if self.controlador.iniciar_sesion(usuario, password):
            messagebox.showinfo(
                "Correcto",
                "Bienvenido"
            )
            self.controlador.mostrar_principal()

        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )