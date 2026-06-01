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
        try:
            img_banner = Image.open("view/imagenes proyecto/Lonely Whale.jpg")
        except FileNotFoundError:
            try:
                img_banner = Image.open("view/Lonely Whale.jpg")
            except FileNotFoundError:
                try:
                    img_banner = Image.open("view/imagenes proyecto/Lonely Whale.jpeg")
                except FileNotFoundError:
                    img_banner = None

        if img_banner:
            ancho_deseado = 960
            ancho_original, alto_original = img_banner.size
            proporcion = ancho_deseado / ancho_original
            alto_proporcional = int(alto_original * proporcion)
            if alto_proporcional > 140:
                alto_proporcional = 140
            img_banner = img_banner.resize((ancho_deseado, alto_proporcional), Image.Resampling.LANCZOS)
            self.banner_photo = ImageTk.PhotoImage(img_banner)
            tk.Label(self, image=self.banner_photo, bg="#BEEED9").pack(fill="x", padx=20, pady=(15, 5))

        self.btn_volver = tk.Button(self, text="Volver", font=("Segoe UI", 9, "bold"), bg="#ffffff", fg="#0b3c5d", bd=1, relief="solid", cursor="hand2", padx=10, command=self._volver)
        self.btn_volver.place(x=30, y=25)

        tk.Label(self, text="REGISTRO DE VOLUNTARIOS", font=self.fuente_titulo, fg="#1b4f72", bg="#BEEED9").pack(pady=10)

        frame_form = tk.Frame(self, bg="#BEEED9")
        frame_form.pack(pady=10)

        campos = [("Identificador (ID):", "entry_id"), ("Nombre Completo:", "entry_nombre"), ("Telefono de Contacto:", "entry_telefono"), ("Edad:", "entry_edad"), ("Correo Electronico:", "entry_correo"), ("Organizacion / Institucion:", "entry_organizacion")]
        for idx, (label_text, attr_name) in enumerate(campos):
            tk.Label(frame_form, text=label_text, font=self.fuente_label, fg="#1b4f72", bg="#BEEED9").grid(row=idx, column=0, sticky="e", padx=15, pady=6)
            entry = tk.Entry(frame_form, font=("Segoe UI", 11), width=35, bd=1, relief="solid")
            entry.grid(row=idx, column=1, sticky="w", padx=15, pady=6)
            setattr(self, attr_name, entry)

        frame_btns = tk.Frame(self, bg="#BEEED9")
        frame_btns.pack(pady=15)
        tk.Button(frame_btns, text="Registrar Interes de Voluntario", font=("Segoe UI", 11, "bold"), bg="#259EFF", fg="white", bd=0, width=28, height=2, cursor="hand2", command=self._registrar).pack(side="left", padx=10)
        tk.Button(frame_btns, text="Ver Voluntarios Registrados", font=("Segoe UI", 11, "bold"), bg="#78909c", fg="white", bd=0, width=25, height=2, cursor="hand2", command=self._ver_tabla).pack(side="left", padx=10)

    def _registrar(self):
        id_v = self.entry_id.get().strip()
        nom = self.entry_nombre.get().strip()
        tel = self.entry_telefono.get().strip()
        edad = self.entry_edad.get().strip()
        corr = self.entry_correo.get().strip()
        org = self.entry_organizacion.get().strip()
        if not all([id_v, nom, tel, edad, corr, org]):
            messagebox.showwarning("Campos Incompletos", "Por favor, llene todos los espacios.")
            return
        if self.controller and hasattr(self.controller, 'registrar_voluntario'):
            self.controller.registrar_voluntario(id_v, nom, tel, edad, corr, org)
        else:
            print(f"[Simulacion] Registrando: {nom}")

    def _ver_tabla(self):
        if self.controller and hasattr(self.controller, 'mostrar_tabla_voluntarios'):
            self.controller.mostrar_tabla_voluntarios()

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_nombre", "entry_telefono", "entry_edad", "entry_correo", "entry_organizacion"):
            getattr(self, attr).delete(0, tk.END)

    def _volver(self):
        if self.controller and hasattr(self.controller, 'mostrar_menu_principal'):
            self.controller.mostrar_menu_principal()