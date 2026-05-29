import tkinter as tk
from tkinter import ttk, messagebox

# --- CONFIGURACIÓN VISUAL ---
COLOR_FONDO_CELESTE = "#96D4D6"
COLOR_TARJETA = "#FFFFFF"
COLOR_BTN_REGISTRAR = "#5F7A61"
COLOR_BTN_VER = "#7F8C8D"
COLOR_BOTON_TEXTO = "#FFFFFF"


class JornadaVistaModerna(tk.Frame):
    def __init__(self, root, controller=None):
        super().__init__(root, bg=COLOR_FONDO_CELESTE)
        self.controller = controller
        self.root = root
        self.root.configure(bg=COLOR_FONDO_CELESTE)
        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        # Contenedor principal
        self.contenedor = tk.Frame(self, bg=COLOR_FONDO_CELESTE)
        self.contenedor.pack(fill="both", expand=True, padx=40, pady=40)

        # Configurar 2 columnas:
        # Columna 0 (Formulario) más ancha (weight=3)
        # Columna 1 (Imagen) más estrecha (weight=2)
        self.contenedor.columnconfigure(0, weight=3)
        self.contenedor.columnconfigure(1, weight=2)

        # --- COLUMNA 0: FORMULARIO (IZQUIERDA) ---
        self.frame_izq = tk.Frame(self.contenedor, bg=COLOR_TARJETA, padx=30, pady=30)
        self.frame_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        tk.Label(self.frame_izq, text="Registrar Nueva Jornada", font=("Segoe UI", 16, "bold"),
                 bg=COLOR_TARJETA).pack(pady=(0, 20), anchor="w")

        self.entries = {}
        campos = [("ID Jornada:", "id"), ("Fecha:", "fecha"), ("Descripción:", "desc"),
                  ("Basura (kg):", "cant"), ("Observaciones:", "obs"), ("ID Zona:", "zona")]

        for label, key in campos:
            tk.Label(self.frame_izq, text=label, bg=COLOR_TARJETA, font=("Segoe UI", 9, "bold")).pack(anchor="w")
            e = tk.Entry(self.frame_izq, font=("Segoe UI", 10))
            e.pack(fill="x", pady=(0, 10), ipady=2)
            self.entries[key] = e

        tk.Button(self.frame_izq, text="Registrar Jornada", bg=COLOR_BTN_REGISTRAR, fg=COLOR_BOTON_TEXTO,
                  font=("Segoe UI", 10, "bold"), command=self._registrar).pack(fill="x", pady=10)
        tk.Button(self.frame_izq, text="Ver Reporte", bg=COLOR_BTN_VER, fg=COLOR_BOTON_TEXTO,
                  font=("Segoe UI", 10, "bold"), command=self._ir_a_lista).pack(fill="x")

        # --- COLUMNA 1: ESPACIO PARA IMAGEN (DERECHA) ---
        self.frame_der = tk.Frame(self.contenedor, bg=COLOR_TARJETA)
        self.frame_der.grid(row=0, column=1, sticky="nsew")

        # Etiqueta que actuará como contenedor de la imagen
        self.lbl_imagen = tk.Label(self.frame_der, text="Espacio para Imagen\n(Arrastra aquí tu foto)",
                                   bg="#E5E8E8", fg=COLOR_BTN_VER)
        self.lbl_imagen.pack(fill="both", expand=True, padx=10, pady=10)

    def _registrar(self):
        # (Tu lógica de registro aquí...)
        messagebox.showinfo("Éxito", "Registrado")

    def _ir_a_lista(self):
        # (Tu lógica de reporte aquí...)
        pass


# --- MAIN ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x600")
    app = JornadaVistaModerna(root)
    root.mainloop()