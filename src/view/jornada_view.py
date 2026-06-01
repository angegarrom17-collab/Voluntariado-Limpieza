import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


class JornadaVistaModerna(tk.Frame):
    def __init__(self, parent, controller=None):
        # Se añade bg="#BEEED9" para asegurar que el frame tenga color desde el inicio
        super().__init__(parent, bg="#BEEED9")
        self.controller = controller
        # IMPORTANTE: Esto fuerza al frame a ocupar el espacio en el contenedor padre
        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        # Usamos el tamaño del contenedor actual en lugar de fijo para mayor flexibilidad
        self.update_idletasks()
        ancho = self.winfo_width() if self.winfo_width() > 1 else 1000
        alto = self.winfo_height() if self.winfo_height() > 1 else 650

        imagen_fondo = Image.new("RGBA", (ancho, alto), "#BEEED9")
        draw = ImageDraw.Draw(imagen_fondo)

        # Lógica de dibujo (simplificada para asegurar carga)
        try:
            alga_original = Image.open("view/alga.png")
        except FileNotFoundError:
            alga_original = None

        if alga_original:
            alga_borde = alga_original.resize((80, 100))
            for y in range(0, alto, 90):
                imagen_fondo.paste(alga_borde, (10, y), alga_borde)
                imagen_fondo.paste(alga_borde, (910, y), alga_borde)
        else:
            # Dibujo de respaldo
            for y in range(30, alto, 120):
                draw.chord([(-20, y), (60, y + 100)], 270, 90, fill="#5F7A61")
                draw.chord([(940, y), (1020, y + 100)], 90, 270, fill="#5F7A61")

        self.foto_fondo = ImageTk.PhotoImage(imagen_fondo)
        # Usamos un Label que se expanda para que el fondo sea siempre visible
        lbl_fondo = tk.Label(self, image=self.foto_fondo, bg="#BEEED9")
        lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        lbl_fondo.lower()  # Enviamos al fondo para que no tape los botones

        # Interfaz de usuario
        tk.Label(self, text="Registrar Nueva Jornada", font=("Comic Sans MS", 22, "bold"), bg="#BEEED9",
                 fg="#1b4f72").place(x=250, y=25)

        frame_campos = tk.Frame(self, bg="#BEEED9")
        frame_campos.place(x=200, y=110)

        labels_texto = ["ID Jornada:", "Fecha:", "Descripcion:", "Basura (kg):", "Observaciones:", "ID Zona:"]
        self.entries = {}
        for i, texto in enumerate(labels_texto):
            tk.Label(frame_campos, text=texto, font=("Comic Sans MS", 12, "bold"), bg="#BEEED9", fg="#1b4f72").grid(
                row=i, column=0, padx=15, pady=8, sticky="e")
            entry = tk.Entry(frame_campos, font=("Arial", 11), width=42, bd=1, relief="solid")
            entry.grid(row=i, column=1, padx=15, pady=8, sticky="w")
            self.entries[texto] = entry

        frame_botones = tk.Frame(self, bg="#BEEED9")
        frame_botones.place(x=380, y=490)

        self.btn_registrar = tk.Button(frame_botones, text="Registrar Jornada", font=("Comic Sans MS", 12, "bold"),
                                       bg="#5F7A61", fg="#FFFFFF", width=22, command=self.registrar_jornada)
        self.btn_registrar.pack(pady=5)

        self.btn_reporte = tk.Button(frame_botones, text="Ver Reporte", font=("Comic Sans MS", 12), bg="#7F8C8D",
                                     fg="#FFFFFF", width=22, command=self.ver_reporte)
        self.btn_reporte.pack(pady=5)

        self.btn_volver = tk.Button(self, text="Volver al Menu", font=("Comic Sans MS", 10, "bold"), bg="white",
                                    fg="#0b3c5d",
                                    command=lambda: self.controller.mostrar_menu_principal() if self.controller else None)
        self.btn_volver.place(x=20, y=20)

    def registrar_jornada(self):
        id_j = self.entries["ID Jornada:"].get().strip()
        fecha = self.entries["Fecha:"].get().strip()
        desc = self.entries["Descripcion:"].get().strip()
        basura = self.entries["Basura (kg):"].get().strip()
        obs = self.entries["Observaciones:"].get().strip()
        zona = self.entries["ID Zona:"].get().strip()

        if not all([id_j, fecha, desc, basura, zona]):
            messagebox.showwarning("Atención", "Complete los campos obligatorios.")
            return

        # Dejamos que el controlador maneje TODO. Si sale bien o mal, él avisará.
        if self.controller:
            self.controller.registrar_nueva_jornada(id_j, fecha, desc, basura, obs, zona)

    def ver_reporte(self):
        if self.controller and hasattr(self.controller, 'ver_reporte_jornadas'):
            self.controller.ver_reporte_jornadas()

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)