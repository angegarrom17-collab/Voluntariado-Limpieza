import tkinter as tk
from PIL import Image, ImageTk

class PrincipalView(tk.Frame):
    def __init__(self, root, controller=None):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.fuente = ("Comic Sans MS", 12, "bold")
        self._build_interface()

    def _build_interface(self):
        try:
            imagen = Image.open("view/marr.png")
        except FileNotFoundError:
            try:
                imagen = Image.open("marr.png")
            except FileNotFoundError:
                imagen = Image.new("RGB", (1000, 650), "#BEEED9")
        imagen = imagen.resize((1000, 650))
        self.fondo = ImageTk.PhotoImage(imagen)
        tk.Label(self, image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text="PROTEJAMOS NUESTRO MAR", font=("Comic Sans MS", 24, "bold"), fg="#1b4f72", bg="#BEEED9").place(x=210, y=25)
        tk.Label(self, text="Pequenas acciones, grandes cambios", font=("Comic Sans MS", 16, "bold"), fg="#1b4f72", bg="#BEEED9").place(x=300, y=80)

        frm = tk.Frame(self, bg="#C0EEE4", bd=0)
        frm.place(x=170, y=170)

        datos = [
            ("Usuarios", "#94D1EE", 0, 0, "mostrar_registro_usuarios"),
            ("Jornadas", "#98EEA1", 0, 1, "mostrar_registro_jornadas"),
            ("Voluntarios", "#FFD884", 0, 2, "mostrar_registro_voluntarios"),
            ("Zonas", "#94EED1", 0, 3, "mostrar_registro_zonas"),
            ("Material", "#FFC1BE", 1, 0, "mostrar_registro_material"),
            ("Animal\nAfectado", "#68EEE1", 1, 1, "mostrar_registro_fauna"),
            ("Basura\nRecolectada", "#e0ccff", 1, 2, "mostrar_registro_basura"),
            ("Reporte", "#B7FF84", 1, 3, "mostrar_reporte"),
        ]

        for texto, color, fila, col, metodo in datos:
            btn = tk.Button(frm, text=texto, font=self.fuente, bg=color, fg="#0b3c5d", width=15, height=5, bd=0, cursor="hand2",
                            command=lambda m=metodo: getattr(self.controller, m)() if self.controller else None)
            btn.grid(row=fila, column=col, padx=15, pady=15)

        tk.Label(self, text="JUNTOS HACEMOS LA DIFERENCIA", font=("Comic Sans MS", 14, "bold"), fg="White", bg="#259EFF").place(x=330, y=600)
        tk.Button(self, text="X", font=("Comic Sans MS", 10, "bold"), bg="white", fg="#0b3c5d", bd=0, width=5, cursor="hand2", command=self.root.destroy).place(x=950, y=610)