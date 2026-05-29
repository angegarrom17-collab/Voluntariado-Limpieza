import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# --- CONFIGURACIÓN DE RUTAS ---
RUTA_BASE = os.path.dirname(__file__)
RUTA_BANNER = os.path.join(RUTA_BASE, "imagenes proyecto", "Lonely Whale.jpg")

# --- CONFIGURACIÓN VISUAL ---
COLOR_FONDO_CELESTE = "#96D4D6"
COLOR_TARJETA = "#FFFFFF"
COLOR_TEXTO_TITULO = "#1C2833"
COLOR_TEXTO_MUTED = "#566573"
COLOR_ENTRADA_TEXTO = "#2C3E50"

# Botones Eco-Premium
COLOR_BTN_REGISTRAR = "#2E52A3"
COLOR_BTN_REGISTRAR_HOVER = "#4A604C"
COLOR_BTN_VER = "#7F8C8D"
COLOR_BTN_VER_HOVER = "#626D6E"
COLOR_BOTON_TEXTO = "#FFFFFF"


class VoluntarioVistaModerna(tk.Frame):
    def __init__(self, root, controller=None):
        super().__init__(root, bg=COLOR_FONDO_CELESTE)
        self.controller = controller
        self.root = root

        self.root.configure(bg=COLOR_FONDO_CELESTE)

        # Fuentes
        self.font_title_large = ("Segoe UI", 16, "bold")
        self.font_title_medium = ("Segoe UI", 11, "bold")
        self.font_label = ("Segoe UI", 9, "bold")
        self.font_entry = ("Segoe UI", 10)
        self.font_button = ("Segoe UI", 10, "bold")

        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        # 1. --- BANNER SUPERIOR (BALLENA) ---
        self.frame_banner = tk.Frame(self, bg=COLOR_FONDO_CELESTE)
        self.frame_banner.pack(fill="x", side="top", padx=20, pady=(15, 5))

        try:
            imagen_original = Image.open(RUTA_BANNER)
            ancho_deseado = 910
            alto_deseado = 130

            proporcion_ancho = ancho_deseado / imagen_original.width
            proporcion_alto = alto_deseado / imagen_original.height
            proporcion_escala = max(proporcion_ancho, proporcion_alto)

            nuevo_ancho = int(imagen_original.width * proporcion_escala)
            nuevo_alto = int(imagen_original.height * proporcion_escala)

            imagen_escalada = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

            izquierda = (nuevo_ancho - ancho_deseado) / 2
            superior = (nuevo_alto - alto_deseado) / 2
            derecha = izquierda + ancho_deseado
            inferior = superior + alto_deseado

            imagen_recortada = imagen_escalada.crop((izquierda, superior, derecha, inferior))
            self.imagen_banner = ImageTk.PhotoImage(imagen_recortada)

            self.lbl_banner = tk.Label(self.frame_banner, image=self.imagen_banner, bd=0, bg=COLOR_FONDO_CELESTE)
            self.lbl_banner.pack(fill="x", expand=True)

        except Exception as e:
            self.lbl_banner = tk.Label(
                self.frame_banner, text="🐋 SISTEMA DE GESTIÓN DE VOLUNTARIOS 🐋",
                font=self.font_title_large, bg="#1A252F", fg="white", pady=25
            )
            self.lbl_banner.pack(fill="x", expand=True)

        # 2. --- CONTENEDOR CENTRAL (3 COLUMNAS) ---
        self.contenedor_principal = tk.Frame(self, bg=COLOR_FONDO_CELESTE)
        self.contenedor_principal.pack(fill="both", expand=True, padx=20, pady=(5, 20))

        self.contenedor_principal.columnconfigure(0, weight=1)
        self.contenedor_principal.columnconfigure(1, weight=2)
        self.contenedor_principal.columnconfigure(2, weight=1)
        self.contenedor_principal.rowconfigure(0, weight=1)

        self._build_col_left()
        self._build_col_center()
        self._build_col_right()

    def _build_col_left(self):
        frame_causa = tk.Frame(self.contenedor_principal, bg=COLOR_TARJETA, bd=0, relief="flat")
        frame_causa.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        tk.Label(frame_causa, text="Nuestra Causa:", font=self.font_title_medium, bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_MUTED).pack(pady=(20, 2))
        tk.Label(frame_causa, text="Vida Marina", font=("Segoe UI", 18, "bold"), bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_TITULO).pack(pady=(0, 15))

        try:
            ruta_causa = os.path.join(RUTA_BASE, "imagenes proyecto", "voluntariado.jpg")
            imagen_original = Image.open(ruta_causa)

            ancho_deseado = 220
            alto_deseado = 230

            proporcion_ancho = ancho_deseado / imagen_original.width
            proporcion_alto = alto_deseado / imagen_original.height
            proporcion_escala = max(proporcion_ancho, proporcion_alto)

            nuevo_ancho = int(imagen_original.width * proporcion_escala)
            nuevo_alto = int(imagen_original.height * proporcion_escala)

            imagen_escalada = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

            izquierda = (nuevo_ancho - ancho_deseado) / 2
            superior = (nuevo_alto - alto_deseado) / 2
            derecha = izquierda + ancho_deseado
            inferior = superior + alto_deseado

            imagen_recortada = imagen_escalada.crop((izquierda, superior, derecha, inferior))
            self.photo_causa = ImageTk.PhotoImage(imagen_recortada)

            self.lbl_imagen_causa = tk.Label(frame_causa, image=self.photo_causa, bg=COLOR_TARJETA, bd=0)
            self.lbl_imagen_causa.pack(fill="x", side="bottom", expand=True)

        except Exception as e:
            self.lbl_imagen_causa = tk.Label(frame_causa, text="[voluntariado.jpg]", bg="#F2F4F4", fg=COLOR_TEXTO_MUTED)
            self.lbl_imagen_causa.pack(pady=(10, 20))

    def _build_col_center(self):
        self.frame_registro = tk.Frame(self.contenedor_principal, bg=COLOR_TARJETA, bd=0, relief="flat")
        self.frame_registro.grid(row=0, column=1, sticky="nsew", padx=10)

        tk.Label(self.frame_registro, text="Apoya la Conservación:", font=self.font_title_medium, bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_MUTED).pack(pady=(15, 2))
        tk.Label(self.frame_registro, text="Registra tu Interés", font=("Segoe UI", 16, "bold"), bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_TITULO).pack(pady=(0, 15))

        frame_grid_campos = tk.Frame(self.frame_registro, bg=COLOR_TARJETA)
        frame_grid_campos.pack(fill="x", padx=30)
        frame_grid_campos.columnconfigure(1, weight=1)

        campos = [
            ("Identificador (ID):", "entry_id"),
            ("Nombre:", "entry_nombre"),
            ("Teléfono:", "entry_telefono"),
            ("Edad:", "entry_edad"),
            ("Correo:", "entry_correo"),
            ("Organización:", "entry_organizacion")
        ]

        for i, (label_text, attr_name) in enumerate(campos):
            lbl = tk.Label(frame_grid_campos, text=label_text, font=self.font_label, bg=COLOR_TARJETA,
                           fg=COLOR_TEXTO_TITULO)
            lbl.grid(row=i, column=0, sticky="e", padx=(0, 10), pady=6)

            entry = tk.Entry(frame_grid_campos, font=self.font_entry, bg="#FFFFFF", fg=COLOR_ENTRADA_TEXTO, bd=1,
                             relief="solid")
            setattr(self, attr_name, entry)
            entry.grid(row=i, column=1, sticky="ew", pady=6, ipady=2)

        # --- CAMBIO AQUÍ: Contenedor de Botones con Grid uniforme ---
        frame_botones = tk.Frame(self.frame_registro, bg=COLOR_TARJETA)
        frame_botones.pack(fill="x", padx=30, pady=(20, 15))

        # Hacemos que la columna se expanda para ocupar todo el ancho disponible
        frame_botones.columnconfigure(0, weight=1)

        self.btn_registrar = tk.Button(
            frame_botones, text="Registrar Interés de Voluntario", font=self.font_button,
            bg=COLOR_BTN_REGISTRAR, fg=COLOR_BOTON_TEXTO, bd=0,
            activebackground=COLOR_BTN_REGISTRAR_HOVER, activeforeground="white",
            pady=10, cursor="hand2", relief="flat"
        )
        self.btn_registrar.configure(command=self._registrar)
        # sticky="ew" obliga al botón a estirarse a lo ancho de la columna
        self.btn_registrar.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.btn_ver_lista = tk.Button(
            frame_botones, text="Ver Voluntarios Registrados", font=self.font_button,
            bg=COLOR_BTN_VER, fg=COLOR_BOTON_TEXTO, bd=0,
            activebackground=COLOR_BTN_VER_HOVER, activeforeground="white",
            pady=10, cursor="hand2", relief="flat"
        )
        self.btn_ver_lista.configure(command=self._ir_a_lista)
        # sticky="ew" para que mida exactamente lo mismo que el de arriba
        self.btn_ver_lista.grid(row=1, column=0, sticky="ew")

    def _build_col_right(self):
        frame_enfoque = tk.Frame(self.contenedor_principal, bg=COLOR_TARJETA, bd=0, relief="flat")
        frame_enfoque.grid(row=0, column=2, sticky="nsew", padx=(10, 0))

        tk.Label(frame_enfoque, text="Nuestro Enfoque:", font=self.font_title_medium, bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_MUTED).pack(pady=(20, 2))
        tk.Label(frame_enfoque, text="Comunidad", font=("Segoe UI", 18, "bold"), bg=COLOR_TARJETA,
                 fg=COLOR_TEXTO_TITULO).pack(pady=(0, 15))

        try:
            ruta_enfoque = os.path.join(RUTA_BASE, "imagenes proyecto", "peces.jpg")
            imagen_original = Image.open(ruta_enfoque)

            ancho_deseado = 220
            alto_deseado = 230

            proporcion_ancho = ancho_deseado / imagen_original.width
            proporcion_alto = alto_deseado / imagen_original.height
            proporcion_escala = max(proporcion_ancho, proporcion_alto)

            nuevo_ancho = int(imagen_original.width * proporcion_escala)
            nuevo_alto = int(imagen_original.height * proporcion_escala)

            imagen_escalada = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

            izquierda = (nuevo_ancho - ancho_deseado) / 2
            superior = (nuevo_alto - alto_deseado) / 2
            derecha = izquierda + ancho_deseado
            inferior = superior + alto_deseado

            imagen_recortada = imagen_escalada.crop((izquierda, superior, derecha, inferior))
            self.photo_enfoque = ImageTk.PhotoImage(imagen_recortada)

            self.lbl_imagen_enfoque = tk.Label(frame_enfoque, image=self.photo_enfoque, bg=COLOR_TARJETA, bd=0)
            self.lbl_imagen_enfoque.pack(fill="x", side="bottom", expand=True)

        except Exception as e:
            self.lbl_imagen_enfoque = tk.Label(frame_enfoque, text="[peces.jpg]", bg="#F2F4F4", fg=COLOR_TEXTO_MUTED)
            self.lbl_imagen_enfoque.pack(pady=(10, 20))

    def _registrar(self):
        id_v = self.entry_id.get().strip()
        nom = self.entry_nombre.get().strip()
        tel = self.entry_telefono.get().strip()
        edad_str = self.entry_edad.get().strip()
        corr = self.entry_correo.get().strip()
        org = self.entry_organizacion.get().strip()

        if not (id_v and nom and tel and edad_str and corr and org):
            messagebox.showwarning("Campos Vacíos", "Por favor, rellene todos los campos del formulario.")
            return

        try:
            edad = int(edad_str)
            if self.controller:
                self.controller.registrar_voluntario(id_v, nom, tel, edad, corr, org)

            messagebox.showinfo("Éxito", f"¡Voluntario '{nom}' registrado correctamente!")
            self._limpiar_campos()
        except ValueError:
            messagebox.showerror("Error de Datos", "La edad debe ser un número entero válido.")

    def _limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_organizacion.delete(0, tk.END)

    def _ir_a_lista(self):
        datos_voluntarios = self.controller.obtener_todos_los_voluntarios()

        ventana_lista = tk.Toplevel(self.root)
        ventana_lista.title("Lista de Voluntarios")
        ventana_lista.geometry("750x400")

        tk.Label(ventana_lista, text="Voluntarios Registrados", font=("Segoe UI", 14, "bold")).pack(pady=10)

        from tkinter import ttk
        columnas = ("ID", "Nombre", "Teléfono", "Edad", "Correo", "Organización")
        tabla = ttk.Treeview(ventana_lista, columns=columnas, show="headings")

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=110, anchor="center")

        for vol in datos_voluntarios:
            tabla.insert("", tk.END, values=(
                vol["id_voluntario"],
                vol["nombre"],
                vol["telefono"],
                vol["edad"],
                vol["correo"],
                vol["organizacion"]
            ))

        tabla.pack(fill="both", expand=True, padx=20, pady=20)


