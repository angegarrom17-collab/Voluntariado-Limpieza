import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR = "#37474F"
COLOR_TOPBAR2 = "#546E7A"
COLOR_FONDO = "#ECEFF1"
COLOR_ACENTO = "#78909C"
COLOR_BORDE = "#B0BEC5"
COLOR_CAMPO_BG = "#FFFFFF"
COLOR_TEXTO = "#1C2B33"
COLOR_LABEL = "#37474F"
COLOR_TH_FG = "#ECEFF1"
COLOR_ROW_PAR = "#ECEFF1"
COLOR_SEP = "#B0BEC5"

class MaterialVista(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, bg=COLOR_FONDO)
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
        tk.Label(bloque_texto, text="Gestion de Materiales", font=("Segoe UI", 13, "bold"), bg=COLOR_TOPBAR, fg="#ECEFF1").pack(anchor="w")
        tk.Label(bloque_texto, text="Sistema de voluntariado  ·  Modulo de inventario", font=("Segoe UI", 9), bg=COLOR_TOPBAR, fg="#CFD8DC").pack(anchor="w")
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)
        tk.Button(bloque_btns, text="Registrar", font=("Segoe UI", 10, "bold"), bg=COLOR_ACENTO, fg="white", activebackground="#546E7A", activeforeground="white", bd=0, padx=18, pady=6, cursor="hand2", command=self._registrar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Usar Material", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#ECEFF1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._usar_material).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Buscar ID", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#ECEFF1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._buscar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Limpiar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#ECEFF1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._limpiar_campos).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Salir", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#ECEFF1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._salir).pack(side="left")

    def _build_form(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(22, 0))
        for c in range(4):
            frame.columnconfigure(c, weight=1)
        campos = [("ID Material", "entry_id", 0, 0, 1), ("Nombre", "entry_nombre", 0, 1, 1), ("Unidad de Medida", "entry_unidad", 0, 2, 1), ("Cantidad Disponible", "entry_cantidad", 0, 3, 1)]
        for label_texto, attr, fila, col, colspan in campos:
            fila_label = fila * 2
            fila_entry = fila * 2 + 1
            tk.Label(frame, text=label_texto.upper(), font=("Segoe UI", 8, "bold"), bg=COLOR_FONDO, fg=COLOR_LABEL).grid(row=fila_label, column=col, columnspan=colspan, sticky="w", padx=(0, 22), pady=(10, 2))
            entry = tk.Entry(frame, font=("Segoe UI", 10), bd=1, relief="solid", bg=COLOR_CAMPO_BG, fg=COLOR_TEXTO, insertbackground=COLOR_TOPBAR, highlightthickness=1, highlightbackground=COLOR_BORDE, highlightcolor=COLOR_TOPBAR)
            entry.grid(row=fila_entry, column=col, columnspan=colspan, sticky="ew", padx=(0, 22), pady=(0, 4), ipady=4)
            setattr(self, attr, entry)

    def _build_separator(self):
        tk.Frame(self, bg=COLOR_SEP, height=1).pack(fill="x", padx=36, pady=16)

    def _build_tabla(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True, padx=36, pady=(0, 18))
        fila_enc = tk.Frame(frame, bg=COLOR_FONDO)
        fila_enc.pack(fill="x", pady=(0, 10))
        tk.Label(fila_enc, text="MATERIALES REGISTRADOS", font=("Segoe UI", 10, "bold"), bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")
        tk.Button(fila_enc, text="Borrar por ID", font=("Segoe UI", 9), bg=COLOR_CAMPO_BG, fg=COLOR_TOPBAR, bd=1, relief="solid", padx=10, pady=3, cursor="hand2", command=self._borrar_por_id).pack(side="right")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Material.Treeview.Heading", font=("Segoe UI", 9, "bold"), background=COLOR_TOPBAR, foreground=COLOR_TH_FG, relief="flat")
        style.configure("Material.Treeview", font=("Segoe UI", 10), rowheight=30, background=COLOR_CAMPO_BG, fieldbackground=COLOR_CAMPO_BG, foreground=COLOR_TEXTO)
        style.map("Material.Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        columnas = ("ID", "Nombre", "Unidad", "Cantidad")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10, style="Material.Treeview")
        anchos = {"ID": 100, "Nombre": 280, "Unidad": 160, "Cantidad": 160}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")
        self.tabla.tag_configure("par", background=COLOR_ROW_PAR)
        self.tabla.tag_configure("impar", background=COLOR_CAMPO_BG)
        self.tabla.pack(fill="both", expand=True)
        self.lbl_footer = tk.Label(frame, text="", font=("Segoe UI", 8), bg=COLOR_FONDO, fg="#607D8B")
        self.lbl_footer.pack(anchor="w", pady=(6, 0))
        self._cargar_tabla()

    def _registrar(self):
        try:
            id_m = self.entry_id.get().strip()
            nom = self.entry_nombre.get().strip()
            uni = self.entry_unidad.get().strip()
            cant = self.entry_cantidad.get().strip()
            if not all([id_m, nom, uni, cant]):
                messagebox.showwarning("Atencion", "Complete todos los campos.")
                return
            if self.controller:
                self.controller.registrar_material(id_m, nom, uni, int(cant))
            messagebox.showinfo("Exito", f"Material '{nom}' registrado.")
            self._limpiar_campos()
            self._cargar_tabla()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un numero entero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _usar_material(self):
        id_m = self.entry_id.get().strip()
        cant = self.entry_cantidad.get().strip()
        if not all([id_m, cant]):
            messagebox.showwarning("Atencion", "Ingrese ID y cantidad a usar.")
            return
        try:
            if self.controller:
                self.controller.usar_material(id_m, int(cant))
                messagebox.showinfo("Exito", f"Se usaron {cant} unidades del material '{id_m}'.")
                self._cargar_tabla()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un numero entero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _buscar(self):
        id_m = self.entry_id.get().strip()
        if not id_m:
            messagebox.showwarning("Atencion", "Ingrese un ID para buscar.")
            return
        if self.controller:
            try:
                material = self.controller.buscar_material(id_m)
                if material:
                    self.entry_nombre.delete(0, tk.END); self.entry_nombre.insert(0, material.nombre)
                    self.entry_unidad.delete(0, tk.END); self.entry_unidad.insert(0, material.unidadMedida)
                    self.entry_cantidad.delete(0, tk.END); self.entry_cantidad.insert(0, material.cantidadDisponible)
                else:
                    messagebox.showinfo("Sin resultados", f"No se encontro material con ID '{id_m}'.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_nombre", "entry_unidad", "entry_cantidad"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        if self.controller:
            materiales = self.controller.get_all_materiales()
            for i, m in enumerate(materiales):
                tag = "par" if i % 2 == 0 else "impar"
                self.tabla.insert("", "end", values=(m.idMaterial, m.nombre, m.unidadMedida, m.cantidadDisponible), tags=(tag,))
            self.lbl_footer.config(text=f"Mostrando {len(materiales)} material(es) en inventario")


    def _borrar_por_id(self):
        id_val = self.entry_id.get().strip()
        if not id_val:
            messagebox.showwarning("Atencion", "Ingrese un ID para borrar.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Esta seguro de eliminar el registro con ID '{id_val}'?"):
            return
        try:
            if self.controller and hasattr(self.controller, 'eliminar_material'):
                self.controller.eliminar_material(id_val)
                messagebox.showinfo("Exito", "Registro eliminado.")
                self._limpiar_campos()
                self._cargar_tabla()
            else:
                messagebox.showerror("Error", "Controlador no conectado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _salir(self):
        if self.controller and hasattr(self.controller, "volver_inicio"):
            self.controller.volver_inicio()
        else:
            self.winfo_toplevel().destroy()