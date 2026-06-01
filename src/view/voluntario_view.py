import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class VoluntarioVistaModerna(tk.Frame):
    def __init__(self, root, controller=None):
        super().__init__(root, bg="#BEEED9")
        self.controller = controller
        self.fuente_label = ("Segoe UI", 10, "bold")
        self.fuente_titulo = ("Segoe UI", 16, "bold")
        self._build_interface()

    def _build_interface(self):
        # --- BANNER ---
        try:
            img_banner = Image.open("view/imagenes proyecto/Lonely Whale.jpg")
        except FileNotFoundError:
            try:
                img_banner = Image.open("view/Lonely Whale.jpg")
            except FileNotFoundError:
                img_banner = None

        if img_banner:
            ancho_deseado = 960
            ancho_original, alto_original = img_banner.size
            proporcion = ancho_deseado / ancho_original
            alto_proporcional = min(int(alto_original * proporcion), 140)
            img_banner = img_banner.resize((ancho_deseado, alto_proporcional), Image.Resampling.LANCZOS)
            self.banner_photo = ImageTk.PhotoImage(img_banner)
            tk.Label(self, image=self.banner_photo, bg="#BEEED9").pack(fill="x", padx=20, pady=(15, 5))

        # --- TÍTULO ---
        tk.Label(self, text="REGISTRO DE VOLUNTARIOS", font=self.fuente_titulo, fg="#1F3A52", bg="#BEEED9").pack(
            pady=10)

        # --- FORMULARIO ---
        frame_form = tk.Frame(self, bg="#BEEED9")
        frame_form.pack(pady=10)

        campos = [
            ("Identificador (ID):", "entry_id"),
            ("Nombre Completo:", "entry_nombre"),
            ("Telefono de Contacto:", "entry_telefono"),
            ("Edad:", "entry_edad"),
            ("Correo Electronico:", "entry_correo"),
            ("Organizacion / Institucion:", "entry_organizacion")
        ]

        for idx, (label_text, attr_name) in enumerate(campos):
            tk.Label(frame_form, text=label_text, font=self.fuente_label, fg="#2C3E50", bg="#BEEED9").grid(
                row=idx, column=0, sticky="e", padx=15, pady=6)
            entry = tk.Entry(frame_form, font=("Segoe UI", 11), width=35, bd=1, relief="solid")
            entry.grid(row=idx, column=1, sticky="w", padx=15, pady=6)
            setattr(self, attr_name, entry)

        # --- PANEL DE BOTONES (GAMA CORPORATIVA) ---
        frame_btns = tk.Frame(self, bg="#BEEED9")
        frame_btns.pack(pady=15)

        estilo = {
            "font": ("Segoe UI", 11, "bold"),
            "bg": "#2C3E50", "fg": "#FFFFFF",
            "activebackground": "#1A252F", "activeforeground": "#FFFFFF",
            "width": 25, "height": 2, "bd": 0, "cursor": "hand2"
        }

        tk.Button(frame_btns, text="Registrar Voluntario", command=self._registrar, **estilo).grid(row=0, column=0,
                                                                                                   padx=10, pady=5)
        tk.Button(frame_btns, text="Eliminar por ID", command=self._eliminar, **estilo).grid(row=0, column=1, padx=10,
                                                                                             pady=5)
        tk.Button(frame_btns, text="Limpiar Campos", command=self._limpiar_campos, **estilo).grid(row=1, column=0,
                                                                                                  padx=10, pady=5)
        tk.Button(frame_btns, text="Ver Voluntarios", command=self._ver_tabla, **estilo).grid(row=1, column=1, padx=10,
                                                                                              pady=5)

        # --- BOTÓN VOLVER ---
        tk.Button(self, text="← Volver", font=("Segoe UI", 9, "bold"), bg="#2C3E50", fg="#FFFFFF",
                  bd=0, cursor="hand2", padx=12, pady=4, command=self._volver).place(x=30, y=25)

    # --- LÓGICA DE EVENTOS ---
    def _registrar(self):
        datos = [getattr(self, attr).get().strip() for attr in
                 ["entry_id", "entry_nombre", "entry_telefono", "entry_edad", "entry_correo", "entry_organizacion"]]
        if not all(datos):
            messagebox.showwarning("Campos Incompletos", "Por favor, llene todos los espacios.")
            return
        if self.controller and hasattr(self.controller, 'registrar_voluntario'):
            self.controller.registrar_voluntario(*datos)

    def _eliminar(self):
        id_v = self.entry_id.get().strip()
        if not id_v:
            messagebox.showwarning("Atención", "Ingrese el ID del voluntario a eliminar.")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar al voluntario con ID '{id_v}'?"):
            if self.controller and hasattr(self.controller, 'eliminar_voluntario_por_id'):
                self.controller.eliminar_voluntario_por_id(id_v)

    def _ver_tabla(self):
        if self.controller and hasattr(self.controller, 'mostrar_tabla_voluntarios'):
            self.controller.mostrar_tabla_voluntarios()

    def _limpiar_campos(self):
        for attr in ["entry_id", "entry_nombre", "entry_telefono", "entry_edad", "entry_correo", "entry_organizacion"]:
            getattr(self, attr).delete(0, tk.END)

    def _volver(self):
        if self.controller and hasattr(self.controller, 'mostrar_menu_principal'):
            self.controller.mostrar_menu_principal()