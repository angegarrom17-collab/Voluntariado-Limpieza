import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR = "#00695C"
COLOR_TOPBAR2 = "#00897B"
COLOR_FONDO = "#E0F2F1"
COLOR_ACENTO = "#26A69A"
COLOR_BORDE = "#80CBC4"
COLOR_CAMPO_BG = "#FFFFFF"
COLOR_TEXTO = "#00352C"
COLOR_LABEL = "#00695C"
COLOR_TH_FG = "#E0F2F1"
COLOR_ROW_PAR = "#E0F2F1"
COLOR_SEP = "#80CBC4"

class FaunaVista(tk.Frame):
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
        tk.Label(bloque_texto, text="Fauna Afectada", font=("Segoe UI", 13, "bold"), bg=COLOR_TOPBAR, fg="#E0F2F1").pack(anchor="w")
        tk.Label(bloque_texto, text="Sistema de monitoreo costero  ·  Modulo de fauna marina", font=("Segoe UI", 9), bg=COLOR_TOPBAR, fg="#B2DFDB").pack(anchor="w")
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)
        tk.Button(bloque_btns, text="Registrar", font=("Segoe UI", 10, "bold"), bg=COLOR_ACENTO, fg="white", activebackground="#00796B", activeforeground="white", bd=0, padx=18, pady=6, cursor="hand2", command=self._registrar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Buscar ID", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E0F2F1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._buscar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Limpiar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E0F2F1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._limpiar_campos).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Salir", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E0F2F1", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._salir).pack(side="left")

    def _build_form(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(22, 0))
        for c in range(3):
            frame.columnconfigure(c, weight=1)
        campos = [("ID Animal", "entry_id", 0, 0, 1), ("Especie", "entry_especie", 0, 1, 1), ("Estado", "entry_estado", 0, 2, 1), ("Descripcion", "entry_descripcion", 1, 0, 3)]
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
        tk.Label(fila_enc, text="ANIMALES REGISTRADOS", font=("Segoe UI", 10, "bold"), bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")
        tk.Button(fila_enc, text="Borrar por ID", font=("Segoe UI", 9), bg=COLOR_CAMPO_BG, fg=COLOR_TOPBAR, bd=1, relief="solid", padx=10, pady=3, cursor="hand2", command=self._borrar_por_id).pack(side="right")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Fauna.Treeview.Heading", font=("Segoe UI", 9, "bold"), background=COLOR_TOPBAR, foreground=COLOR_TH_FG, relief="flat")
        style.configure("Fauna.Treeview", font=("Segoe UI", 10), rowheight=30, background=COLOR_CAMPO_BG, fieldbackground=COLOR_CAMPO_BG, foreground=COLOR_TEXTO)
        style.map("Fauna.Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        columnas = ("ID", "Especie", "Estado", "Descripcion")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10, style="Fauna.Treeview")
        anchos = {"ID": 80, "Especie": 200, "Estado": 160, "Descripcion": 360}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")
        self.tabla.tag_configure("par", background=COLOR_ROW_PAR)
        self.tabla.tag_configure("impar", background=COLOR_CAMPO_BG)
        self.tabla.pack(fill="both", expand=True)
        self.lbl_footer = tk.Label(frame, text="", font=("Segoe UI", 8), bg=COLOR_FONDO, fg="#00897B")
        self.lbl_footer.pack(anchor="w", pady=(6, 0))
        self._cargar_tabla()

    def _registrar(self):
        id_a = self.entry_id.get().strip()
        esp = self.entry_especie.get().strip()
        est = self.entry_estado.get().strip()
        desc = self.entry_descripcion.get().strip()

        if not all([id_a, esp, est]):
            messagebox.showwarning("Atención", "Complete los campos obligatorios: ID, Especie y Estado.")
            return

        if self.controller:
            self.controller.registrar_animal(id_a, esp, est, desc)

    def _buscar(self):
        id_a = self.entry_id.get().strip()
        if not id_a:
            messagebox.showwarning("Atencion", "Ingrese un ID para buscar.")
            return
        if self.controller:
            try:
                animal = self.controller.buscar_animal(id_a)
                if animal:
                    self.entry_especie.delete(0, tk.END); self.entry_especie.insert(0, animal.especie)
                    self.entry_estado.delete(0, tk.END); self.entry_estado.insert(0, animal.estado)
                    self.entry_descripcion.delete(0, tk.END); self.entry_descripcion.insert(0, animal.descripcion)
                else:
                    messagebox.showinfo("Sin resultados", f"No se encontro animal con ID '{id_a}'.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_especie", "entry_estado", "entry_descripcion"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        if self.controller:
            animales = self.controller.get_all_animales()
            for i, a in enumerate(animales):
                tag = "par" if i % 2 == 0 else "impar"
                self.tabla.insert("", "end", values=(getattr(a, "idAnimal", ""), a.especie, a.estado, a.descripcion), tags=(tag,))
            self.lbl_footer.config(text=f"Mostrando {len(animales)} animal(es) registrado(s)")


    def _borrar_por_id(self):
        id_val = self.entry_id.get().strip()
        if not id_val:
            messagebox.showwarning("Atencion", "Ingrese un ID para borrar.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Esta seguro de eliminar el registro con ID '{id_val}'?"):
            return
        try:
            if self.controller and hasattr(self.controller, 'eliminar_animal'):
                self.controller.eliminar_animal(id_val)
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

    def notificar_registro_exitoso(self):
        self._limpiar_campos()
        self._cargar_tabla()