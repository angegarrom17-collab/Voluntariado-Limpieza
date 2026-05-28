import tkinter as tk
from tkinter import ttk, messagebox
import os  # Para manejar las rutas de carpetas de forma segura
from PIL import Image, ImageTk  # Para procesar la imagen JPG


class VoluntarioVista(tk.Frame):

    def __init__(self, root, controller):
        # Configuramos el fondo general gris claro moderno
        super().__init__(root, bg="#F4F6F7")
        self.controller = controller

        # Paleta de colores para el diseño limpio
        self.COLOR_FONDO = "#F4F6F7"
        self.COLOR_TARJETA = "#FFFFFF"
        self.COLOR_TEXTO = "#2C3E50"
        self.COLOR_BOTON_PRIMARIO = "#2ECC71"  # Verde
        self.COLOR_BOTON_SECUNDARIO = "#3498DB"  # Azul

        self._build()

    def _build(self):
        # 1. --- BANNER SUPERIOR (Permanente en la parte alta) ---
        self.frame_banner = tk.Frame(self, bg=self.COLOR_FONDO)
        self.frame_banner.pack(fill="x", side="top", pady=(0, 10))

        # ARREGLO DE RUTA: Buscamos dentro de 'view/imagenes proyecto/'
        carpeta_view = os.path.dirname(__file__)
        ruta_imagen = os.path.join(carpeta_view, "imagenes proyecto", "descarga (2).jpg")

        try:
            # Abrimos y redimensionamos la imagen JPG con Pillow
            imagen_original = Image.open(ruta_imagen)
            # 680 de ancho por 130 de alto le va genial al tamaño de la ventana
            imagen_redimensionada = imagen_original.resize((680, 130), Image.Resampling.LANCZOS)
            self.imagen_banner = ImageTk.PhotoImage(imagen_redimensionada)

            self.lbl_banner = tk.Label(self.frame_banner, image=self.imagen_banner, bg=self.COLOR_FONDO)
            self.lbl_banner.pack(fill="x", expand=True)
        except Exception as e:
            # Respaldo visual elegante si ocurre algún detalle imprevisto
            print(f"Aviso: Cargando respaldo de texto por detalle con la imagen: {e}")
            self.lbl_banner = tk.Label(
                self.frame_banner,
                text="🌿 GESTIÓN DE VOLUNTARIOS 🌿",
                font=("Arial", 16, "bold"),
                bg="#2C3E50",
                fg="white",
                pady=20
            )
            self.lbl_banner.pack(fill="x", expand=True)

        # 2. --- CONTENEDOR CENTRAL (Intercambiable) ---
        self.contenedor_principal = tk.Frame(self, bg=self.COLOR_FONDO)
        self.contenedor_principal.pack(fill="both", expand=True)

        # 3. --- VISTA: FORMULARIO DE REGISTRO ---
        self.frame_formulario = tk.Frame(self.contenedor_principal, bg=self.COLOR_TARJETA, bd=1, relief="solid")
        self.frame_formulario.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(
            self.frame_formulario,
            text="Registrar Nuevo Voluntario",
            font=("Arial", 14, "bold"),
            bg=self.COLOR_TARJETA,
            fg=self.COLOR_TEXTO
        ).grid(row=0, column=0, columnspan=2, pady=(15, 10))

        # Etiquetas fijas
        labels = ["Identificador (ID):", "Nombre:", "Teléfono:", "Edad:", "Correo:", "Organización:"]
        for i, text in enumerate(labels):
            tk.Label(
                self.frame_formulario,
                text=text,
                font=("Arial", 10, "bold"),
                bg=self.COLOR_TARJETA,
                fg=self.COLOR_TEXTO
            ).grid(row=i + 1, column=0, padx=(25, 10), pady=5, sticky="e")

        # Campos de entrada (Entries)
        self.entry_id = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")
        self.entry_nombre = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")
        self.entry_telefono = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")
        self.entry_edad = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")
        self.entry_correo = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")
        self.entry_organizacion = tk.Entry(self.frame_formulario, width=32, font=("Arial", 10), bd=1, relief="solid")

        self.entry_id.grid(row=1, column=1, padx=(10, 25), pady=5, sticky="w")
        self.entry_nombre.grid(row=2, column=1, padx=(10, 25), pady=5, sticky="w")
        self.entry_telefono.grid(row=3, column=1, padx=(10, 25), pady=5, sticky="w")
        self.entry_edad.grid(row=4, column=1, padx=(10, 25), pady=5, sticky="w")
        self.entry_correo.grid(row=5, column=1, padx=(10, 25), pady=5, sticky="w")
        self.entry_organizacion.grid(row=6, column=1, padx=(10, 25), pady=5, sticky="w")

        # Botones del Formulario
        btn_registrar = tk.Button(
            self.frame_formulario, text="💾 Registrar Voluntario", font=("Arial", 10, "bold"),
            bg=self.COLOR_BOTON_PRIMARIO, fg="white", width=24, bd=0, cursor="hand2",
            activebackground="#27AE60", activeforeground="white"
        )
        btn_registrar.configure(command=self._registrar)
        btn_registrar.grid(row=7, column=0, columnspan=2, pady=(15, 5))

        btn_ver_lista = tk.Button(
            self.frame_formulario, text="📋 Ver Lista de Voluntarios", font=("Arial", 10),
            bg=self.COLOR_BOTON_SECUNDARIO, fg="white", width=24, bd=0, cursor="hand2",
            activebackground="#2980B9", activeforeground="white"
        )
        btn_ver_lista.configure(command=self._ir_a_lista)
        btn_ver_lista.grid(row=8, column=0, columnspan=2, pady=(5, 15))

        # 4. --- VISTA: TABLA / LISTA DE REGISTROS ---
        self.frame_tabla = tk.Frame(self.contenedor_principal, bg=self.COLOR_TARJETA, bd=1, relief="solid")

        tk.Label(
            self.frame_tabla, text="Voluntarios Registrados", font=("Arial", 14, "bold"),
            bg=self.COLOR_TARJETA, fg=self.COLOR_TEXTO
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Configuración del estilo TTK para modernizar el Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview", background="#FFFFFF", foreground=self.COLOR_TEXTO,
            rowheight=25, fieldbackground="#FFFFFF", font=("Arial", 9)
        )
        style.configure(
            "Treeview.Heading", background="#ECEFF1", foreground=self.COLOR_TEXTO,
            font=("Arial", 10, "bold")
        )
        style.map("Treeview", background=[('selected', '#3498DB')], foreground=[('selected', 'white')])

        nombres_columnas = ("ID", "Nombre", "Teléfono", "Edad", "Correo", "Organización")
        self.tabla_voluntarios = ttk.Treeview(self.frame_tabla, columns=nombres_columnas, show="headings", height=7)

        for nombre_columna in nombres_columnas:
            self.tabla_voluntarios.heading(nombre_columna, text=nombre_columna)
            self.tabla_voluntarios.column(nombre_columna, width=95, anchor="center")
        self.tabla_voluntarios.grid(row=1, column=0, columnspan=2, padx=15, pady=10, sticky="nsew")

        # Botones inferiores de la Tabla
        btn_actualizar = tk.Button(
            self.frame_tabla, text="🔄 Actualizar", font=("Arial", 10),
            bg="#95A5A6", fg="white", width=14, bd=0, cursor="hand2"
        )
        btn_actualizar.configure(command=self._cargar_tabla)
        btn_actualizar.grid(row=2, column=0, pady=15, padx=10, sticky="e")

        btn_volver = tk.Button(
            self.frame_tabla, text="⬅️ Volver", font=("Arial", 10),
            bg="#7F8C8D", fg="white", width=14, bd=0, cursor="hand2"
        )
        btn_volver.configure(command=self._ir_a_formulario)
        btn_volver.grid(row=2, column=1, pady=15, padx=10, sticky="w")

    def _ir_a_lista(self):
        self.frame_formulario.pack_forget()
        self.frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        self._cargar_tabla()

    def _ir_a_formulario(self):
        self.frame_tabla.pack_forget()
        self.frame_formulario.pack(fill="both", expand=True, padx=20, pady=10)

    def _registrar(self):
        try:
            id_voluntario = self.entry_id.get()
            nombre = self.entry_nombre.get()
            telefono = self.entry_telefono.get()
            edad_str = self.entry_edad.get()
            correo = self.entry_correo.get()
            organizacion = self.entry_organizacion.get()

            try:
                edad = int(edad_str)
            except ValueError:
                raise ValueError("La edad debe ser un número entero válido.")

            self.controller.registrar_voluntario(id_voluntario, nombre, telefono, edad, correo, organizacion)

            messagebox.showinfo("Éxito", "Voluntario registrado correctamente.")
            self._limpiar_campos()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def _limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_organizacion.delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_voluntarios.get_children():
            self.tabla_voluntarios.delete(fila)

        for volu in self.controller.obtener_todos_los_voluntarios():
            self.tabla_voluntarios.insert("", "end", values=(
                volu["id_voluntario"], volu["nombre"], volu["telefono"],
                volu["edad"], volu["correo"], volu["organizacion"]
            ))


# -------- Main ejecutable para pruebas individuales -------------------------

if __name__ == "__main__":

    class ControladorVoluntariosFalso:
        def __init__(self):
            self.voluntarios_db = []

        def registrar_voluntario(self, id_v, nom, tel, edad, corr, org):
            if edad < 20:
                raise ValueError("El voluntario tiene que ser mayor de 20 años.")
            nuevo_dict = {
                "id_voluntario": id_v, "nombre": nom, "telefono": tel,
                "edad": edad, "correo": corr, "organizacion": org
            }
            self.voluntarios_db.append(nuevo_dict)

        def obtener_todos_los_voluntarios(self):
            return self.voluntarios_db


    root = tk.Tk()
    root.title("Sistema de Gestión de Voluntarios")

    root.geometry("680x520")
    root.configure(bg="#F4F6F7")

    controlador_test = ControladorVoluntariosFalso()

    vista = VoluntarioVista(root, controller=controlador_test)
    vista.pack(fill="both", expand=True)

    root.mainloop()