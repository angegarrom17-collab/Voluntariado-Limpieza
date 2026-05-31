import tkinter as tk
from PIL import Image, ImageTk


# Convertimos toda la vista en una clase que hereda de tk.Frame
class PrincipalView(tk.Frame):
    def __init__(self, root, controller=None):
        # Inicializamos el Frame contenedor dentro de la ventana principal
        super().__init__(root)
        self.root = root
        self.controller = controller

        # Guardamos la referencia de la fuente
        self.fuente = ("Comic Sans MS", 12, "bold")

        # Desplegamos la interfaz ocupando toda la ventana
        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        # ---------------- IMAGEN DE FONDO ----------------
        try:
            # Buscamos la imagen marr.png (ajusta la ruta si está en otra carpeta, ej: "view/marr.png")
            imagen = Image.open("view/marr.png")
        except FileNotFoundError:
            imagen = Image.open("marr.png")

        imagen = imagen.resize((1000, 650))
        self.fondo = ImageTk.PhotoImage(imagen)

        # Usamos self para empaquetar los widgets dentro de este Frame
        self.labelFondo = tk.Label(self, image=self.fondo)
        self.labelFondo.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------------- TITULO ----------------
        self.titulo = tk.Label(
            self,
            text="🌊 PROTEJAMOS NUESTRO MAR 🌊",
            font=("Comic Sans MS", 24, "bold"),
            fg="#1b4f72",
            bg="#BEEED9"
        )
        self.titulo.place(x=210, y=25)

        # ---------------- SUBTITULO ----------------
        self.subtitulo = tk.Label(
            self,
            text="Pequeñas acciones, grandes cambios",
            font=("Comic Sans MS", 16, "bold"),
            fg="#1b4f72",
            bg="#BEEED9"
        )
        self.subtitulo.place(x=300, y=80)

        # ---------------- FRAME BOTONES ----------------
        self.frame_botones = tk.Frame(
            self,
            bg="#C0EEE4",
            bd=0
        )
        self.frame_botones.place(x=170, y=170)

        # ---------------- FILA 1 ----------------
        self.btnUsuarios = tk.Button(
            self.frame_botones, text="👤\nUsuarios", font=self.fuente,
            bg="#94D1EE", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_usuarios() if self.controller else print("Click Usuarios")
        )
        self.btnUsuarios.grid(row=0, column=0, padx=15, pady=15)

        self.btnJornadas = tk.Button(
            self.frame_botones, text="🌊\nJornadas", font=self.fuente,
            bg="#98EEA1", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_jornadas() if self.controller else print("Click Jornadas")
        )
        self.btnJornadas.grid(row=0, column=1, padx=15, pady=15)

        self.btnVoluntarios = tk.Button(
            self.frame_botones, text="🤝\nVoluntarios", font=self.fuente,
            bg="#FFD884", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_voluntarios() if self.controller else print("Click Voluntarios")
        )
        self.btnVoluntarios.grid(row=0, column=2, padx=15, pady=15)

        self.btnZonas = tk.Button(
            self.frame_botones, text="📍\nZonas", font=self.fuente,
            bg="#94EED1", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_zonas() if self.controller else print("Click Zonas")
        )
        self.btnZonas.grid(row=0, column=3, padx=15, pady=15)

        # ---------------- FILA 2 ----------------
        self.btnMaterial = tk.Button(
            self.frame_botones, text="♻️\nMaterial", font=self.fuente,
            bg="#FFC1BE", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_material() if self.controller else print("Click Material")
        )
        self.btnMaterial.grid(row=1, column=0, padx=15, pady=15)

        self.btnAnimal = tk.Button(
            self.frame_botones, text="🐢\nAnimal\nAfectado", font=self.fuente,
            bg="#68EEE1", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_fauna() if self.controller else print("Click Animal Afectado")
        )
        self.btnAnimal.grid(row=1, column=1, padx=15, pady=15)

        self.btnBasura = tk.Button(
            self.frame_botones, text="🗑️\nBasura\nRecolectada", font=self.fuente,
            bg="#e0ccff", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_registro_basura() if self.controller else print("Click Basura Recolectada")
        )
        self.btnBasura.grid(row=1, column=2, padx=15, pady=15)

        self.btnReporte = tk.Button(
            self.frame_botones, text="📊\nReporte", font=self.fuente,
            bg="#B7FF84", fg="#0b3c5d", width=15, height=5, bd=0, relief="flat", cursor="hand2",
            command=lambda: self.controller.mostrar_reporte() if self.controller else print("Click Reporte")
        )
        self.btnReporte.grid(row=1, column=3, padx=15, pady=15)

        # ---------------- MENSAJE Y SALIR ----------------
        self.mensaje = tk.Label(
            self, text="🌎 JUNTOS HACEMOS LA DIFERENCIA 🌎",
            font=("Comic Sans MS", 14, "bold"), fg="White", bg="#259EFF"
        )
        self.mensaje.place(x=330, y=600)

        self.btnSalir = tk.Button(
            self, text="✖", font=("Comic Sans MS", 10, "bold"),
            bg="white", fg="#0b3c5d", bd=0, relief="flat", width=5, cursor="hand2",
            command=self.root.destroy
        )
        self.btnSalir.place(x=950, y=610)