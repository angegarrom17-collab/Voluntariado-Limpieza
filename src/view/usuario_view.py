import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR = "#6B4226"
COLOR_FONDO = "#F2EAD3"
COLOR_ACENTO = "#C8956C"
COLOR_BORDE = "#C9B49A"
COLOR_CAMPO_BG = "#FFF9F2"
COLOR_TEXTO = "#3E2010"
COLOR_LABEL = "#8B6347"
COLOR_SEP = "#D6C4A8"
COLOR_ROW_PAR = "#EDE0CC"
COLOR_TH_FG = "#F9F3E8"

class UsuarioVista(tk.Frame):
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
        topbar = tk.Frame(self, bg=COLOR_TOPBAR, height=58)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)
        bloque_texto = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_texto.pack(side="left", padx=24, pady=8)
        tk.Label(bloque_texto, text="Gestion de Usuarios", font=("Segoe UI", 13, "bold"), bg=COLOR_TOPBAR, fg="#F9F3E8").pack(anchor="w")
        tk.Label(bloque_texto, text="Sistema administrativo  ·  Modulo de acceso", font=("Segoe UI", 9), bg=COLOR_TOPBAR, fg="#D4B896").pack(anchor="w")
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)
        tk.Button(bloque_btns, text="Registrar", font=("Segoe UI", 10, "bold"), bg=COLOR_ACENTO, fg="white", bd=0, padx=16, pady=6, cursor="hand2", command=self._registrar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Limpiar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#F9F3E8", activebackground="#8B5E3C", activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._limpiar_campos).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Salir", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#F9F3E8", activebackground="#8B5E3C", activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._salir).pack(side="left")

    def _build_form(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(24, 0))
        campos = [("ID", "entry_id", False), ("Nombre completo", "entry_nombre", False), ("Correo electronico", "entry_correo", False), ("Contrasena", "entry_contrasena", True), ("Tipo de usuario", "entry_tipo", False)]
        for idx, (label, attr, es_pass) in enumerate(campos):
            col = idx % 3
            fila_base = (idx // 3) * 2
            tk.Label(frame, text=label.upper(), font=("Segoe UI", 8, "bold"), bg=COLOR_FONDO, fg=COLOR_LABEL).grid(row=fila_base, column=col, sticky="w", padx=(0, 24), pady=(10, 2))
            entry = tk.Entry(frame, font=("Segoe UI", 10), bd=1, relief="solid", bg=COLOR_CAMPO_BG, fg=COLOR_TEXTO, insertbackground=COLOR_TOPBAR, show="*" if es_pass else "")
            entry.grid(row=fila_base + 1, column=col, sticky="ew", padx=(0, 24), pady=(0, 4))
            setattr(self, attr, entry)
        for i in range(3):
            frame.columnconfigure(i, weight=1)

    def _build_separator(self):
        tk.Frame(self, bg=COLOR_SEP, height=1).pack(fill="x", padx=36, pady=16)

    def _build_tabla(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True, padx=36, pady=(0, 20))
        fila_enc = tk.Frame(frame, bg=COLOR_FONDO)
        fila_enc.pack(fill="x", pady=(0, 10))
        tk.Label(fila_enc, text="USUARIOS REGISTRADOS", font=("Segoe UI", 10, "bold"), bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")
        tk.Button(fila_enc, text="Borrar por ID", font=("Segoe UI", 9), bg=COLOR_FONDO, fg=COLOR_TOPBAR, bd=1, relief="solid", padx=10, pady=3, cursor="hand2", command=self._borrar_por_id).pack(side="right")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Cafe.Treeview.Heading", font=("Segoe UI", 9, "bold"), background=COLOR_TOPBAR, foreground=COLOR_TH_FG, relief="flat")
        style.configure("Cafe.Treeview", font=("Segoe UI", 10), rowheight=28, background=COLOR_FONDO, fieldbackground=COLOR_FONDO, foreground=COLOR_TEXTO)
        style.map("Cafe.Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        columnas = ("ID", "Nombre", "Correo", "Tipo")
        self.tabla_usuarios = ttk.Treeview(frame, columns=columnas, show="headings", height=8, style="Cafe.Treeview")
        anchos = {"ID": 70, "Nombre": 220, "Correo": 260, "Tipo": 120}
        for col in columnas:
            self.tabla_usuarios.heading(col, text=col)
            self.tabla_usuarios.column(col, width=anchos[col], anchor="center")
        self.tabla_usuarios.pack(fill="both", expand=True)
        self.lbl_footer = tk.Label(frame, text="", font=("Segoe UI", 8), bg=COLOR_FONDO, fg=COLOR_LABEL)
        self.lbl_footer.pack(anchor="w", pady=(6, 0))
        self._cargar_tabla()

    def _registrar(self):
        id_usuario = self.entry_id.get().strip()
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        contrasena = self.entry_contrasena.get().strip()
        tipo = self.entry_tipo.get().strip()
        if not all([id_usuario, nombre, correo, contrasena, tipo]):
            messagebox.showwarning("Atencion", "Complete todos los campos.")
            return
        if not id_usuario.isdigit():
            messagebox.showerror("Error", "El ID debe ser numerico.")
            return
        try:
            self.controller.registrar_usuario(id_usuario, nombre, correo, contrasena, tipo)
            messagebox.showinfo("Exito", f"Usuario '{nombre}' registrado.")
            self._limpiar_campos()
            self._cargar_tabla()
        except ValueError as e:
            messagebox.showerror("Validacion", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_nombre", "entry_correo", "entry_contrasena", "entry_tipo"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(fila)
        usuarios = self.controller.get_all_usuarios()
        for u in usuarios:
            self.tabla_usuarios.insert("", "end", values=(u.id_usuario, u.nombre, u.correo, u.tipo))
        self.lbl_footer.config(text=f"Mostrando {len(usuarios)} registro(s)")


    def _borrar_por_id(self):
        id_val = self.entry_id.get().strip()
        if not id_val:
            messagebox.showwarning("Atencion", "Ingrese un ID para borrar.")
            return
        if not messagebox.askyesno("Confirmar", f"¿Esta seguro de eliminar el registro con ID '{id_val}'?"):
            return
        try:
            if self.controller and hasattr(self.controller, 'eliminar_usuario'):
                self.controller.eliminar_usuario(id_val)
                messagebox.showinfo("Exito", "Registro eliminado.")
                self._limpiar_campos()
                self._cargar_tabla()
            else:
                messagebox.showerror("Error", "Controlador no conectado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _salir(self):
        self.controller.volver_inicio()