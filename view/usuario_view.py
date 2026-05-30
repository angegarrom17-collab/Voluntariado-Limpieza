import tkinter as tk
from tkinter import ttk, messagebox

# ── PALETA CAFÉ ADMINISTRATIVA ─────────────────────────────────────────────────
COLOR_TOPBAR      = "#6B4226"   # café oscuro  → topbar y encabezado de tabla
COLOR_FONDO       = "#F2EAD3"   # beige cálido → fondo general
COLOR_ACENTO      = "#C8956C"   # terracota    → botón primario y badges
COLOR_BORDE       = "#C9B49A"   # borde suave
COLOR_CAMPO_BG    = "#FFF9F2"   # blanco crema → fondo de inputs
COLOR_TEXTO       = "#3E2010"   # café muy oscuro → texto principal
COLOR_LABEL       = "#8B6347"   # café medio   → etiquetas de campo
COLOR_SEP         = "#D6C4A8"   # separador entre secciones
COLOR_ROW_PAR     = "#EDE0CC"   # fila par de la tabla
COLOR_TH_FG       = "#F9F3E8"   # texto del encabezado de tabla


class UsuarioVista(tk.Frame):

    def __init__(self, root, controller):
        super().__init__(root, bg=COLOR_FONDO)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self._build()

    # ──────────────────────────────────────────────────────────────────────────
    def _build(self):
        self._build_topbar()
        self._build_form()
        self._build_separator()
        self._build_tabla()

    # ── 1. TOPBAR ─────────────────────────────────────────────────────────────
    def _build_topbar(self):
        """
        Barra superior con título a la izquierda y los tres botones
        (Registrar / Limpiar / Salir) a la derecha.
        Reemplaza la sidebar lateral y los botones del panel del diseño anterior.
        """
        topbar = tk.Frame(self, bg=COLOR_TOPBAR, height=58)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        # Bloque de texto: título + subtítulo
        bloque_texto = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_texto.pack(side="left", padx=24, pady=8)

        tk.Label(bloque_texto,
                 text="Gestión de Usuarios",
                 font=("Segoe UI", 13, "bold"),
                 bg=COLOR_TOPBAR, fg="#F9F3E8"
                 ).pack(anchor="w")

        tk.Label(bloque_texto,
                 text="Sistema administrativo  ·  Módulo de acceso",
                 font=("Segoe UI", 9),
                 bg=COLOR_TOPBAR, fg="#D4B896"
                 ).pack(anchor="w")

        # Botones a la derecha del topbar
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)

        # Registrar (acento terracota)
        tk.Button(bloque_btns,
                  text="Registrar",
                  font=("Segoe UI", 10, "bold"),
                  bg=COLOR_ACENTO, fg="white",
                  activebackground="#A0522D", activeforeground="white",
                  bd=0, padx=16, pady=6, cursor="hand2",
                  command=self._registrar
                  ).pack(side="left", padx=(0, 8))

        # Limpiar (borde claro, sin relleno)
        tk.Button(bloque_btns,
                  text="Limpiar",
                  font=("Segoe UI", 10),
                  bg=COLOR_TOPBAR, fg="#F9F3E8",
                  activebackground="#8B5E3C", activeforeground="white",
                  bd=1, relief="solid", padx=14, pady=6, cursor="hand2",
                  highlightbackground="#F9F3E8",
                  command=self._limpiar_campos
                  ).pack(side="left", padx=(0, 8))

        # Salir (borde claro, llama al controlador o cierra la ventana)
        tk.Button(bloque_btns,
                  text="⬅  Salir",
                  font=("Segoe UI", 10),
                  bg=COLOR_TOPBAR, fg="#F9F3E8",
                  activebackground="#8B5E3C", activeforeground="white",
                  bd=1, relief="solid", padx=14, pady=6, cursor="hand2",
                  command=self._salir
                  ).pack(side="left")

    # ── 2. FORMULARIO ─────────────────────────────────────────────────────────
    def _build_form(self):
        """
        Cinco campos en una cuadrícula de 3 columnas usando grid().
        El quinto campo ocupa la primera celda de la segunda fila.
        """
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(24, 0))

        campos = [
            ("ID",                 "entry_id",          False),
            ("Nombre completo",    "entry_nombre",      False),
            ("Correo electrónico", "entry_correo",      False),
            ("Contraseña",         "entry_contrasena",  True),
            ("Tipo de usuario",    "entry_tipo",        False),
        ]

        for idx, (label_texto, attr, es_pass) in enumerate(campos):
            col = idx % 3          # columna: 0, 1, 2, 0, 1
            fila_base = (idx // 3) * 2   # cada campo ocupa 2 filas (label + entry)

            tk.Label(frame,
                     text=label_texto.upper(),
                     font=("Segoe UI", 8, "bold"),
                     bg=COLOR_FONDO, fg=COLOR_LABEL
                     ).grid(row=fila_base, column=col,
                            sticky="w", padx=(0, 24), pady=(10, 2))

            entry = tk.Entry(frame,
                             font=("Segoe UI", 10),
                             bd=1, relief="solid",
                             bg=COLOR_CAMPO_BG, fg=COLOR_TEXTO,
                             insertbackground=COLOR_TOPBAR,
                             show="*" if es_pass else "")
            entry.grid(row=fila_base + 1, column=col,
                       sticky="ew", padx=(0, 24), pady=(0, 4))

            setattr(self, attr, entry)

        # Las 3 columnas se expanden igual al redimensionar
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

    # ── 3. SEPARADOR ──────────────────────────────────────────────────────────
    def _build_separator(self):
        """Línea fina entre el formulario y la tabla."""
        tk.Frame(self, bg=COLOR_SEP, height=1).pack(fill="x", padx=36, pady=16)

    # ── 4. TABLA ──────────────────────────────────────────────────────────────
    def _build_tabla(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True, padx=36, pady=(0, 20))

        # Encabezado de sección
        fila_enc = tk.Frame(frame, bg=COLOR_FONDO)
        fila_enc.pack(fill="x", pady=(0, 10))

        tk.Label(fila_enc,
                 text="USUARIOS REGISTRADOS",
                 font=("Segoe UI", 10, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_TOPBAR
                 ).pack(side="left")

        tk.Button(fila_enc,
                  text="⟳  Actualizar",
                  font=("Segoe UI", 9),
                  bg=COLOR_FONDO, fg=COLOR_TOPBAR,
                  bd=1, relief="solid", padx=10, pady=3, cursor="hand2",
                  command=self._cargar_tabla
                  ).pack(side="right")

        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Cafe.Treeview.Heading",
                         font=("Segoe UI", 9, "bold"),
                         background=COLOR_TOPBAR,
                         foreground=COLOR_TH_FG,
                         relief="flat")
        style.configure("Cafe.Treeview",
                         font=("Segoe UI", 10),
                         rowheight=28,
                         background=COLOR_FONDO,
                         fieldbackground=COLOR_FONDO,
                         foreground=COLOR_TEXTO)
        style.map("Cafe.Treeview",
                  background=[("selected", COLOR_ACENTO)],
                  foreground=[("selected", "white")])

        columnas = ("ID", "Nombre", "Correo", "Tipo")
        self.tabla_usuarios = ttk.Treeview(frame,
                                            columns=columnas,
                                            show="headings",
                                            height=8,
                                            style="Cafe.Treeview")
        anchos = {"ID": 70, "Nombre": 220, "Correo": 260, "Tipo": 120}
        for col in columnas:
            self.tabla_usuarios.heading(col, text=col)
            self.tabla_usuarios.column(col, width=anchos[col], anchor="center")

        self.tabla_usuarios.pack(fill="both", expand=True)

        self.lbl_footer = tk.Label(frame,
                                    text="",
                                    font=("Segoe UI", 8),
                                    bg=COLOR_FONDO, fg=COLOR_LABEL)
        self.lbl_footer.pack(anchor="w", pady=(6, 0))

        self._cargar_tabla()

    # ── MÉTODOS DE LÓGICA ─────────────────────────────────────────────────────

    def _registrar(self):
        try:
            id_usuario = self.entry_id.get().strip()
            nombre     = self.entry_nombre.get().strip()
            correo     = self.entry_correo.get().strip()
            contrasena = self.entry_contrasena.get().strip()
            tipo       = self.entry_tipo.get().strip()

            if not (id_usuario and nombre and correo and contrasena and tipo):
                messagebox.showwarning("Atención", "Complete todos los campos.")
                return

            self.controller.registrar_usuario(
                int(id_usuario), nombre, correo, contrasena, tipo
            )
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado.")
            self._limpiar_campos()
            self._cargar_tabla()
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _limpiar_campos(self):
        for attr in ("entry_id", "entry_nombre", "entry_correo",
                     "entry_contrasena", "entry_tipo"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(fila)

        usuarios = self.controller.get_all_usuarios()
        for u in usuarios:
            self.tabla_usuarios.insert("", "end",
                values=(u.id_usuario, u.nombre, u.correo, u.tipo))

        self.lbl_footer.config(text=f"Mostrando {len(usuarios)} registro(s)")

    def _salir(self):
        """
        Intenta navegar hacia la ventana principal a través del controlador.
        Si el controlador no tiene ese método, cierra directamente la ventana.
        """
        if hasattr(self.controller, "volver_inicio"):
            self.controller.volver_inicio()
        else:
            self.winfo_toplevel().destroy()


# ── EJECUCIÓN INDEPENDIENTE ───────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema Administrativo · Usuarios")
    root.geometry("1000x650")
    root.resizable(False, False)

    class ControladorFalso:
        def registrar_usuario(self, id_, nombre, correo, contrasena, tipo):
            print(f"[REGISTRO] id={id_}, nombre={nombre}, tipo={tipo}")

        def get_all_usuarios(self):
            return []

        def volver_inicio(self):
            print("[SALIR] Navegando a ventana principal...")

    app = UsuarioVista(root, ControladorFalso())
    root.mainloop()