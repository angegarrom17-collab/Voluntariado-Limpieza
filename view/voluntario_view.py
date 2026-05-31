import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class VoluntarioVistaModerna(tk.Frame):
    def __init__(self, root, controller=None):
        # Usamos el color celeste/turquesa claro de fondo de tu aplicación
        super().__init__(root, bg="#BEEED9")
        self.controller = controller
        self.fuente_label = ("Segoe UI", 10, "bold")
        self.fuente_titulo = ("Segoe UI", 16, "bold")

        self._build_interface()

    def _build_interface(self):
        # ---------------- 1. BANNER DE LA BALLENA (CON PROPORCIÓN CORRECTA) ----------------
        try:
            # Buscamos tu imagen "Lonely Whale" en la carpeta del proyecto
            img_banner = Image.open("view/imagenes proyecto/Lonely Whale.jpg")
        except FileNotFoundError:
            try:
                img_banner = Image.open("view/Lonely Whale.jpg")
            except FileNotFoundError:
                try:
                    # Intento por si guardaste la imagen con otra extensión (.jpeg o .png)
                    img_banner = Image.open("view/imagenes proyecto/Lonely Whale.jpeg")
                except FileNotFoundError:
                    img_banner = None

        if img_banner:
            # --- CÁLCULO PARA EVITAR QUE SE VEA JALADA ---
            ancho_deseado = 960
            ancho_original, alto_original = img_banner.size

            # Calculamos el alto proporcional para que mantenga su forma original
            proporcion = ancho_deseado / ancho_original
            alto_proporcional = int(alto_original * proporcion)

            # Limitamos el alto máximo para que no se coma espacio del formulario
            if alto_proporcional > 140:
                alto_proporcional = 140

            # Redimensionamos con filtro de alta calidad para que se vea nítida
            img_banner = img_banner.resize((ancho_deseado, alto_proporcional), Image.Resampling.LANCZOS)

            self.banner_photo = ImageTk.PhotoImage(img_banner)
            lbl_banner = tk.Label(self, image=self.banner_photo, bg="#BEEED9")
            lbl_banner.pack(fill="x", padx=20, pady=(15, 5))

        # ---------------- 2. BOTÓN VOLVER (FLOTANTE SOBRE EL BANNER) ----------------
        self.btn_volver = tk.Button(
            self, text="⬅ Volver", font=("Segoe UI", 9, "bold"),
            bg="#ffffff", fg="#0b3c5d", bd=1, relief="solid", cursor="hand2",
            padx=10, command=self._volver
        )
        self.btn_volver.place(x=30, y=25)

        # ---------------- 3. TÍTULO SIMPLIFICADO ----------------
        tk.Label(
            self, text="REGISTRO DE VOLUNTARIOS",
            font=self.fuente_titulo, fg="#1b4f72", bg="#BEEED9"
        ).pack(pady=10)

        # ---------------- 4. FORMULARIO EN CAPA ÚNICA (Limpio y Centrado) ----------------
        # Agrupamos los campos en un frame central del mismo color del fondo
        frame_form = tk.Frame(self, bg="#BEEED9")
        frame_form.pack(pady=10)

        campos = [
            ("Identificador (ID):", "entry_id"),
            ("Nombre Completo:", "entry_nombre"),
            ("Teléfono de Contacto:", "entry_telefono"),
            ("Edad:", "entry_edad"),
            ("Correo Electrónico:", "entry_correo"),
            ("Organización / Institución:", "entry_organizacion")
        ]

        # Colocamos las etiquetas y cajas de texto una debajo de otra de manera uniforme
        for idx, (label_text, attr_name) in enumerate(campos):
            lbl = tk.Label(frame_form, text=label_text, font=self.fuente_label, fg="#1b4f72", bg="#BEEED9")
            lbl.grid(row=idx, column=0, sticky="e", padx=15, pady=6)

            entry = tk.Entry(frame_form, font=("Segoe UI", 11), width=35, bd=1, relief="solid")
            entry.grid(row=idx, column=1, sticky="w", padx=15, pady=6)

            setattr(self, attr_name, entry)

        # ---------------- 5. BOTONES DE ACCIÓN PRINCIPALES ----------------
        frame_btns = tk.Frame(self, bg="#BEEED9")
        frame_btns.pack(pady=15)

        tk.Button(
            frame_btns, text="Registrar Interés de Voluntario", font=("Segoe UI", 11, "bold"),
            bg="#259EFF", fg="white", bd=0, width=28, height=2, cursor="hand2",
            command=self._registrar
        ).pack(side="left", padx=10)

        tk.Button(
            frame_btns, text="Ver Voluntarios Registrados", font=("Segoe UI", 11, "bold"),
            bg="#78909c", fg="white", bd=0, width=25, height=2, cursor="hand2",
            command=self._ver_tabla
        ).pack(side="left", padx=10)

    # -------------------------------------------------------------
    # LÓGICA DE INTERACCIÓN Y ENLACE
    # -------------------------------------------------------------
    def _registrar(self):
        id_v = self.entry_id.get().strip()
        nom = self.entry_nombre.get().strip()
        tel = self.entry_telefono.get().strip()
        edad = self.entry_edad.get().strip()
        corr = self.entry_correo.get().strip()
        org = self.entry_organizacion.get().strip()

        if not (id_v and nom and tel and edad and corr and org):
            messagebox.showwarning("Campos Incompletos", "Por favor, llene todos los espacios solicitados.")
            return

        # Llama de forma segura al método registrar_voluntario de tu ControladorPrincipal
        if self.controller and hasattr(self.controller, 'registrar_voluntario'):
            self.controller.registrar_voluntario(id_v, nom, tel, edad, corr, org)
            messagebox.showinfo("Éxito", f"¡Gracias {nom}! Interés registrado correctamente.")
            self._limpiar_campos()
        else:
            print(f"[Simulación] Registrando en memoria local a: {nom}")

    def _ver_tabla(self):
        print("Abriendo lista de voluntarios registrados...")

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_nombre", "entry_telefono", "entry_edad", "entry_correo", "entry_organizacion"):
            getattr(self, attr).delete(0, tk.END)

    def _volver(self):
        # Regresa fluidamente al menú principal usando el AppController
        if self.controller and hasattr(self.controller, 'mostrar_menu_principal'):
            self.controller.mostrar_menu_principal()
        else:
            print("Regresando al inicio...")