import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


class JornadaVistaModerna(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, bg="#BEEED9")
        self.controller = controller
        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        self.update_idletasks()
        ancho = self.winfo_width() if self.winfo_width() > 1 else 1000
        alto = self.winfo_height() if self.winfo_height() > 1 else 650

        imagen_fondo = Image.new("RGBA", (ancho, alto), "#BEEED9")
        draw = ImageDraw.Draw(imagen_fondo)

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
            # Siluetas en un tono gris-verde oscuro muy sobrio
            for y in range(30, alto, 120):
                draw.chord([(-20, y), (60, y + 100)], 270, 90, fill="#4A6550")
                draw.chord([(940, y), (1020, y + 100)], 90, 270, fill="#4A6550")

        self.foto_fondo = ImageTk.PhotoImage(imagen_fondo)
        lbl_fondo = tk.Label(self, image=self.foto_fondo, bg="#BEEED9")
        lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        lbl_fondo.lower()

        # Título principal en Azul Ejecutivo Profundo
        tk.Label(self, text="Registrar Nueva Jornada", font=("Arial", 22, "bold"), bg="#BEEED9",
                 fg="#1F3A52").place(x=250, y=25)

        frame_campos = tk.Frame(self, bg="#BEEED9")
        frame_campos.place(x=200, y=110)

        labels_texto = ["ID Jornada:", "Fecha:", "Descripcion:", "Basura (kg):", "Observaciones:", "ID Zona:"]
        self.entries = {}
        for i, texto in enumerate(labels_texto):
            # Textos de los campos en gris oscuro corporativo
            tk.Label(frame_campos, text=texto, font=("Arial", 11, "bold"), bg="#BEEED9", fg="#2C3E50").grid(
                row=i, column=0, padx=15, pady=8, sticky="e")
            entry = tk.Entry(frame_campos, font=("Arial", 11), width=42, bd=1, relief="solid", highlightthickness=0)
            entry.grid(row=i, column=1, padx=15, pady=8, sticky="w")
            self.entries[texto] = entry

        # --- PANEL DE BOTONES: GAMA UNIFICADA AZUL MARINO / GRIS CORPORATIVO ---
        frame_botones = tk.Frame(self, bg="#BEEED9")
        frame_botones.place(x=240, y=490)

        # Configuración común para toda la botonera
        estilo_botones = {
            "font": ("Arial", 11, "bold"),
            "bg": "#2C3E50",  # Azul Marino Corporativo uniforme para todos
            "fg": "#FFFFFF",  # Texto blanco limpio
            "activebackground": "#1A252F",  # Cambio sutil al presionar
            "activeforeground": "#FFFFFF",
            "width": 20,
            "bd": 0,  # Quitamos bordes toscos de Tkinter para un diseño plano (Flat)
            "cursor": "hand2",  # Cambia el cursor a mano al pasar por encima
            "pady": 6
        }

        # Botón 1: Registrar
        self.btn_registrar = tk.Button(frame_botones, text="Registrar Jornada", command=self.registrar_jornada,
                                       **estilo_botones)
        self.btn_registrar.grid(row=0, column=0, padx=10, pady=6)

        # Botón 2: Eliminar por ID (Mismo color base para mantener la seriedad)
        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar por ID", command=self.eliminar_jornada,
                                      **estilo_botones)
        self.btn_eliminar.grid(row=0, column=1, padx=10, pady=6)

        # Botón 3: Limpiar Campos
        self.btn_limpiar = tk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos,
                                     **estilo_botones)
        self.btn_limpiar.grid(row=1, column=0, padx=10, pady=6)

        # Botón 4: Ver Reporte
        self.btn_reporte = tk.Button(frame_botones, text="Ver Reporte", command=self.ver_reporte, **estilo_botones)
        self.btn_reporte.grid(row=1, column=1, padx=10, pady=6)

        # Botón Volver al Menú: Minimalista integrado a la esquina
        self.btn_volver = tk.Button(self, text="Salir", font=("Arial", 10, "bold"),
                                    bg="#2C3E50", fg="#FFFFFF", activebackground="#1A252F", activeforeground="#FFFFFF",
                                    bd=0, cursor="hand2", padx=12, pady=4,
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

        if self.controller:
            self.controller.registrar_nueva_jornada(id_j, fecha, desc, basura, obs, zona)

    def eliminar_jornada(self):
        id_j = self.entries["ID Jornada:"].get().strip()
        if not id_j:
            messagebox.showwarning("Atención",
                                   "Escriba el ID de la jornada que desea eliminar en el campo 'ID Jornada:'.")
            return

        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de que desea eliminar la jornada con ID '{id_j}'?")
        if confirmar:
            if self.controller and hasattr(self.controller, 'eliminar_jornada_por_id'):
                self.controller.eliminar_jornada_por_id(id_j)
            else:
                messagebox.showerror("Error", "El controlador no está conectado o no tiene la función de eliminar.")

    def ver_reporte(self):
        if self.controller and hasattr(self.controller, 'ver_reporte_jornadas'):
            self.controller.ver_reporte_jornadas()

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)