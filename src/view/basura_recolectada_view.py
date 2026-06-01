import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR = "#2E7D32"
COLOR_TOPBAR2 = "#43A047"
COLOR_FONDO = "#F1F8F1"
COLOR_ACENTO = "#66BB6A"
COLOR_BORDE = "#A5D6A7"
COLOR_CAMPO_BG = "#FFFFFF"
COLOR_TEXTO = "#1B3A1C"
COLOR_LABEL = "#2E7D32"
COLOR_TH_FG = "#E8F5E9"
COLOR_ROW_PAR = "#E8F5E9"
COLOR_SEP = "#A5D6A7"

class BasuraRecolectadaVista(tk.Frame):
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
        tk.Label(bloque_texto, text="Basura Recolectada", font=("Segoe UI", 13, "bold"), bg=COLOR_TOPBAR, fg="#E8F5E9").pack(anchor="w")
        tk.Label(bloque_texto, text="Sistema de monitoreo costero  ·  Modulo de residuos", font=("Segoe UI", 9), bg=COLOR_TOPBAR, fg="#C8E6C9").pack(anchor="w")
        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)
        tk.Button(bloque_btns, text="Registrar", font=("Segoe UI", 10, "bold"), bg=COLOR_ACENTO, fg="white", activebackground="#388E3C", activeforeground="white", bd=0, padx=18, pady=6, cursor="hand2", command=self._registrar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Actualizar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E8F5E9", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._actualizar).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Limpiar", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E8F5E9", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._limpiar_campos).pack(side="left", padx=(0, 8))
        tk.Button(bloque_btns, text="Salir", font=("Segoe UI", 10), bg=COLOR_TOPBAR, fg="#E8F5E9", activebackground=COLOR_TOPBAR2, activeforeground="white", bd=1, relief="solid", padx=14, pady=6, cursor="hand2", command=self._salir).pack(side="left")

    def _build_form(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(22, 0))
        for c in range(3):
            frame.columnconfigure(c, weight=1)
        campos = [("Tipo de Residuo", "entry_tipo", 0, 0, 1), ("Peso (kg)", "entry_peso", 0, 1, 1), ("Fecha", "entry_fecha", 0, 2, 1)]
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
        tk.Label(fila_enc, text="REGISTROS DE BASURA", font=("Segoe UI", 10, "bold"), bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")
        tk.Button(fila_enc, text="Recargar", font=("Segoe UI", 9), bg=COLOR_CAMPO_BG, fg=COLOR_TOPBAR, bd=1, relief="solid", padx=10, pady=3, cursor="hand2", command=self._cargar_tabla).pack(side="right")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Basura.Treeview.Heading", font=("Segoe UI", 9, "bold"), background=COLOR_TOPBAR, foreground=COLOR_TH_FG, relief="flat")
        style.configure("Basura.Treeview", font=("Segoe UI", 10), rowheight=30, background=COLOR_CAMPO_BG, fieldbackground=COLOR_CAMPO_BG, foreground=COLOR_TEXTO)
        style.map("Basura.Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        columnas = ("Tipo de Residuo", "Peso (kg)", "Fecha")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10, style="Basura.Treeview")
        anchos = {"Tipo de Residuo": 400, "Peso (kg)": 200, "Fecha": 200}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")
        self.tabla.tag_configure("par", background=COLOR_ROW_PAR)
        self.tabla.tag_configure("impar", background=COLOR_CAMPO_BG)
        self.tabla.pack(fill="both", expand=True)
        self.lbl_footer = tk.Label(frame, text="", font=("Segoe UI", 8), bg=COLOR_FONDO, fg="#4CAF50")
        self.lbl_footer.pack(anchor="w", pady=(6, 0))
        self._cargar_tabla()

    def _registrar(self):
        try:
            tipo = self.entry_tipo.get().strip()
            peso = self.entry_peso.get().strip()
            fecha = self.entry_fecha.get().strip()
            if not all([tipo, peso, fecha]):
                messagebox.showwarning("Atencion", "Complete todos los campos.")
                return
            if self.controller:
                self.controller.registrar_basura(tipo, float(peso), fecha)
            messagebox.showinfo("Exito", f"Residuo '{tipo}' registrado ({peso} kg).")
            self._limpiar_campos()
            self._cargar_tabla()
        except ValueError:
            messagebox.showerror("Error", "El peso debe ser un numero valido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _actualizar(self):
        sel = self.tabla.selection()
        if not sel:
            messagebox.showwarning("Atencion", "Seleccione un registro para actualizar.")
            return
        val = self.tabla.item(sel[0])["values"]
        self.entry_tipo.delete(0, tk.END); self.entry_tipo.insert(0, val[0])
        self.entry_peso.delete(0, tk.END); self.entry_peso.insert(0, val[1])
        self.entry_fecha.delete(0, tk.END); self.entry_fecha.insert(0, val[2])

    def _limpiar_campos(self):
        for attr in ("entry_tipo", "entry_peso", "entry_fecha"):
            getattr(self, attr).delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        if self.controller:
            registros = self.controller.get_all_basura()
            for i, b in enumerate(registros):
                tag = "par" if i % 2 == 0 else "impar"
                self.tabla.insert("", "end", values=(b.tipoResiduo, b.pesoKilos, b.fecha), tags=(tag,))
            self.lbl_footer.config(text=f"Mostrando {len(registros)} registro(s)")

    def _salir(self):
        if self.controller and hasattr(self.controller, "volver_inicio"):
            self.controller.volver_inicio()
        else:
            self.winfo_toplevel().destroy()