import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR = "#1A6B8A"
COLOR_TOPBAR2 = "#2BA0C0"
COLOR_FONDO = "#E8F4F8"
COLOR_ACENTO = "#F0A500"
COLOR_BORDE = "#90CAD8"
COLOR_CAMPO_BG = "#FFFFFF"
COLOR_TEXTO = "#0D3D50"
COLOR_LABEL = "#1A6B8A"
COLOR_TH_FG = "#E0F7FA"
COLOR_ROW_PAR = "#EBF6FA"
COLOR_ROW_HOVER = "#D0ECF5"

class ZonaVista(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg=COLOR_FONDO)
        self.controller = controller
        self._build()

    def _build(self):
        self._build_topbar()
        self._build_form()
        self._build_separator()
        self._build_tabla()

    def _build_topbar(self):
        topbar = tk.Frame(self, bg=COLOR_TOPBAR, height=62)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)
        bloque_texto = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_texto.pack(side="left", padx=24, pady=8)
        tk.Label(bloque_texto, text="Gestion de Zonas", font=("Segoe UI", 13, "bold"), bg=COLOR_TOPBAR, fg="#E0F7FA").pack(anchor="w")
        tk.Label(bloque_texto, text="Sistema de monitoreo costero  ·  Modulo de zonas", font=("Segoe UI", 9), bg=COLOR_TOPBAR, fg="#B2EBF2").pack(anchor="w")
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)
        tk.Button(bloque_btns, text="Registrar", font=("Segoe UI", 10, "bold"), bg=COLOR_ACENTO, fg="white", activebackground="#CC8C00", activeforeground="white", bd=0, padx=18, pady=6, cursor="hand2", command=self._registrar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Limpiar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E0F7FA", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._limpiar_campos).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Salir", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E0F7FA", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._salir).pack(side="left")

    def _build_form(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(22, 0))
        for c in range(3):
            frame.columnconfigure(c, weight=1)
        campos = [("ID Zona", "entry_id_zona", 0, 0, 1), ("Nombre", "entry_nombre_zona", 0, 1, 1), ("Ubicacion", "entry_ubicacion", 0, 2, 1), ("Nivel de Contaminacion", "entry_nivel_contaminacion", 1, 0, 1), ("Descripcion", "entry_descripcion", 1, 1, 2)]
        for label_texto, attr, fila, col, colspan in campos:
            fila_label = fila * 2
            fila_entry = fila * 2 + 1
            tk.Label(frame, text=label_texto.upper(), font=("Segoe UI", 8, "bold"), bg=COLOR_FONDO, fg=COLOR_LABEL).grid(row=fila_label, column=col, columnspan=colspan, sticky="w", padx=(0, 22), pady=(10, 2))
            entry = tk.Entry(frame, font=("Segoe UI", 10), bd=1, relief="solid", bg=COLOR_CAMPO_BG, fg=COLOR_TEXTO, insertbackground=COLOR_TOPBAR, highlightthickness=1, highlightbackground=COLOR_BORDE, highlightcolor=COLOR_TOPBAR)
            entry.grid(row=fila_entry, column=col, columnspan=colspan, sticky="ew", padx=(0, 22), pady=(0, 4), ipady=4)
            setattr(self, attr, entry)

    def _build_separator(self):
        canvas = tk.Canvas(self, height=28, bg=COLOR_FONDO, highlightthickness=0)
        canvas.pack(fill="x", padx=36, pady=(14, 0))
        puntos = []
        ancho = 928
        for i in range(0, ancho + 1, 20):
            import math
            y = 14 + 6 * math.sin(i / 80 * math.pi)
            puntos.extend([i, y])
        canvas.create_line(puntos, fill=COLOR_BORDE, width=2, smooth=True)

    def _build_tabla(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True, padx=36, pady=(10, 18))
        fila_enc = tk.Frame(frame, bg=COLOR_FONDO)
        fila_enc.pack(fill="x", pady=(0, 10))
        tk.Label(fila_enc, text="ZONAS REGISTRADAS", font=("Segoe UI", 10, "bold"), bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")
        tk.Button(fila_enc, text="Borrar por ID", font=("Segoe UI", 9), bg=COLOR_CAMPO_BG, fg=COLOR_TOPBAR, bd=1, relief="solid", padx=10, pady=3, cursor="hand2", command=self._borrar_por_id).pack(side="right")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Oceano.Treeview.Heading", font=("Segoe UI", 9, "bold"), background=COLOR_TOPBAR, foreground=COLOR_TH_FG, relief="flat")
        style.configure("Oceano.Treeview", font=("Segoe UI", 10), rowheight=30, background=COLOR_CAMPO_BG, fieldbackground=COLOR_CAMPO_BG, foreground=COLOR_TEXTO)
        style.map("Oceano.Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        columnas = ("ID", "Nombre", "Ubicacion", "Contaminacion")
        self.tabla_zonas = ttk.Treeview(frame, columns=columnas, show="headings", height=8, style="Oceano.Treeview")
        anchos = {"ID": 70, "Nombre": 200, "Ubicacion": 260, "Contaminacion": 130}
        for col in columnas:
            self.tabla_zonas.heading(col, text=col)
            self.tabla_zonas.column(col, width=anchos[col], anchor="center")
        self.tabla_zonas.tag_configure("par", background=COLOR_ROW_PAR)
        self.tabla_zonas.tag_configure("impar", background=COLOR_CAMPO_BG)
        self.tabla_zonas.pack(fill="both", expand=True)
        self.lbl_footer = tk.Label(frame, text="", font=("Segoe UI", 8), bg=COLOR_FONDO, fg="#5A9DB0")
        self.lbl_footer.pack(anchor="w", pady=(6, 0))
        self._cargar_tabla()

    def _registrar(self):
        # 1. Obtenemos datos
        id_raw = self.entry_id_zona.get().strip()
        nombre = self.entry_nombre_zona.get().strip()
        ubicacion = self.entry_ubicacion.get().strip()
        nivel = self.entry_nivel_contaminacion.get().strip().lower()
        desc = self.entry_descripcion.get().strip()

        #Validación de campos vacíos
        if not all([id_raw, nombre, ubicacion, nivel]):
            messagebox.showwarning("Atención", "Complete todos los campos obligatorios.")
            return

        #Validación entero ID
        try:
            id_int = int(id_raw)
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        #Validación de Niveles
        niveles_validos = ["bajo", "medio", "alto", "critico"]
        if nivel not in niveles_validos:
            messagebox.showerror("Error", f"Nivel inválido. Use: {', '.join(niveles_validos)}")
            return

        #Validación de Duplicados
        zonas_existentes = self.controller.get_all_zonas()
        if any(z.id_zona == id_int for z in zonas_existentes):
            messagebox.showerror("Error", f"Ya existe una zona con el ID {id_int}.")
            return

        #Registra
        try:
            self.controller.registrar_zona(id_int, nombre, ubicacion, nivel, desc)
            messagebox.showinfo("Éxito", f"Zona '{nombre}' registrada correctamente.")
            self._limpiar_campos()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error inesperado", str(e))

    def _limpiar_campos(self):
        for attr in ("entry_id_zona", "entry_nombre_zona", "entry_ubicacion", "entry_nivel_contaminacion", "entry_descripcion"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_zonas.get_children():
            self.tabla_zonas.delete(fila)
        zonas = self.controller.get_all_zonas()
        for i, zona in enumerate(zonas):
            tag = "par" if i % 2 == 0 else "impar"
            self.tabla_zonas.insert("", "end", values=(zona.id_zona, zona.nombre_zona, zona.ubicacion, zona.nivel_contaminacion), tags=(tag,))
        self.lbl_footer.config(text=f"Mostrando {len(zonas)} zona(s) registrada(s)")


    def _borrar_por_id(self):
        id_val = self.entry_id_zona.get().strip()
        if not id_val:
            messagebox.showwarning("Atencion", "Ingrese un ID para borrar.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Esta seguro de eliminar el registro con ID '{id_val}'?"):
            return
        try:
            if self.controller and hasattr(self.controller, 'eliminar_zona'):
                self.controller.eliminar_zona(id_val)
                messagebox.showinfo("Exito", "Registro eliminado.")
                self._limpiar_campos()
                self._cargar_tabla()
            else:
                messagebox.showerror("Error", "Controlador no conectado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _salir(self):
        self.controller.volver_inicio()
