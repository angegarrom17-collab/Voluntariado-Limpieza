import tkinter as tk
from tkinter import ttk, messagebox

COLOR_TOPBAR   = "#0B3C5D"
COLOR_TOPBAR2  = "#1565C0"
COLOR_FONDO    = "#EEF4FB"
COLOR_ACENTO   = "#1976D2"
COLOR_BORDE    = "#90B4D8"
COLOR_CAMPO_BG = "#FFFFFF"
COLOR_TEXTO    = "#062036"
COLOR_LABEL    = "#0B3C5D"
COLOR_TH_FG    = "#E3F2FD"
COLOR_ROW_PAR  = "#E3F2FD"
COLOR_SEP      = "#90B4D8"
COLOR_CARD_BG  = "#FFFFFF"
COLOR_CARD_BD  = "#B0CDE6"


class ReporteVista(tk.Frame):

    def __init__(self, parent, controller=None):
        super().__init__(parent, bg=COLOR_FONDO)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self._build()

    def _build(self):
        self._build_topbar()
        self._build_resumen()
        self._build_separator()
        self._build_tabla()

    # ─── TOPBAR ───────────────────────────────────────────────────
    def _build_topbar(self):
        topbar = tk.Frame(self, bg=COLOR_TOPBAR, height=62)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        bloque_texto = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_texto.pack(side="left", padx=24, pady=8)

        tk.Label(bloque_texto,
                 text="Reporte General",
                 font=("Segoe UI", 13, "bold"),
                 bg=COLOR_TOPBAR, fg="#E3F2FD").pack(anchor="w")

        tk.Label(bloque_texto,
                 text="Sistema de monitoreo costero  ·  Resumen de impacto ambiental",
                 font=("Segoe UI", 9),
                 bg=COLOR_TOPBAR, fg="#90B4D8").pack(anchor="w")

        bloque_btns = tk.Frame(topbar, bg=COLOR_TOPBAR)
        bloque_btns.pack(side="right", padx=20)

        tk.Button(bloque_btns,
                  text="Generar Reporte",
                  font=("Segoe UI", 10, "bold"),
                  bg=COLOR_ACENTO, fg="white",
                  activebackground="#1565C0", activeforeground="white",
                  bd=0, padx=18, pady=6, cursor="hand2",
                  command=self._generar).pack(side="left", padx=(0, 8))

        tk.Button(bloque_btns,
                  text="Limpiar",
                  font=("Segoe UI", 10),
                  bg=COLOR_TOPBAR, fg="#E3F2FD",
                  activebackground=COLOR_TOPBAR2, activeforeground="white",
                  bd=1, relief="solid", padx=14, pady=6, cursor="hand2",
                  command=self._limpiar).pack(side="left", padx=(0, 8))

        tk.Button(bloque_btns,
                  text="<-  Salir",
                  font=("Segoe UI", 10),
                  bg=COLOR_TOPBAR, fg="#E3F2FD",
                  activebackground=COLOR_TOPBAR2, activeforeground="white",
                  bd=1, relief="solid", padx=14, pady=6, cursor="hand2",
                  command=self._salir).pack(side="left")

    # ─── TARJETAS RESUMEN ─────────────────────────────────────────
    def _build_resumen(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="x", padx=36, pady=(24, 0))

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        tarjetas = [
            ("Total Basura",      "lbl_total",    "0.00 kg"),
            ("Promedio",          "lbl_promedio", "0.00 kg"),
            ("Animales Afectados","lbl_animales", "0"),
        ]

        for col, (titulo, attr, valor_inicial) in enumerate(tarjetas):
            card = tk.Frame(frame,
                            bg=COLOR_CARD_BG,
                            bd=1, relief="solid",
                            highlightthickness=1,
                            highlightbackground=COLOR_CARD_BD)
            card.grid(row=0, column=col, sticky="ew",
                      padx=(0 if col == 0 else 12, 0), pady=0, ipady=10)

            tk.Label(card,
                     text=titulo.upper(),
                     font=("Segoe UI", 8, "bold"),
                     bg=COLOR_CARD_BG, fg=COLOR_LABEL
                     ).pack(pady=(12, 4))

            lbl = tk.Label(card,
                           text=valor_inicial,
                           font=("Segoe UI", 20, "bold"),
                           bg=COLOR_CARD_BG, fg=COLOR_TOPBAR)
            lbl.pack(pady=(0, 12))

            setattr(self, attr, lbl)

    # ─── SEPARADOR ────────────────────────────────────────────────
    def _build_separator(self):
        tk.Frame(self, bg=COLOR_SEP, height=1).pack(fill="x", padx=36, pady=16)

    # ─── TABLA RESIDUOS POR TIPO ──────────────────────────────────
    def _build_tabla(self):
        frame = tk.Frame(self, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True, padx=36, pady=(0, 18))

        fila_enc = tk.Frame(frame, bg=COLOR_FONDO)
        fila_enc.pack(fill="x", pady=(0, 10))

        tk.Label(fila_enc,
                 text="RESIDUOS POR TIPO",
                 font=("Segoe UI", 10, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_TOPBAR).pack(side="left")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Reporte.Treeview.Heading",
                        font=("Segoe UI", 9, "bold"),
                        background=COLOR_TOPBAR,
                        foreground=COLOR_TH_FG,
                        relief="flat")
        style.configure("Reporte.Treeview",
                        font=("Segoe UI", 10),
                        rowheight=30,
                        background=COLOR_CAMPO_BG,
                        fieldbackground=COLOR_CAMPO_BG,
                        foreground=COLOR_TEXTO)
        style.map("Reporte.Treeview",
                  background=[("selected", COLOR_ACENTO)],
                  foreground=[("selected", "white")])

        columnas = ("Tipo de Residuo", "Peso Total (kg)")
        self.tabla = ttk.Treeview(frame,
                                   columns=columnas,
                                   show="headings",
                                   height=10,
                                   style="Reporte.Treeview")

        anchos = {"Tipo de Residuo": 560, "Peso Total (kg)": 240}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")

        self.tabla.tag_configure("par",   background=COLOR_ROW_PAR)
        self.tabla.tag_configure("impar", background=COLOR_CAMPO_BG)
        self.tabla.pack(fill="both", expand=True)

        self.lbl_footer = tk.Label(frame,
                                    text="Presione 'Generar Reporte' para cargar los datos.",
                                    font=("Segoe UI", 8),
                                    bg=COLOR_FONDO, fg="#5A7FA0")
        self.lbl_footer.pack(anchor="w", pady=(6, 0))

    # ─── ACCIONES ─────────────────────────────────────────────────
    def _generar(self):
        if not self.controller:
            messagebox.showinfo("Sin controlador",
                                "Conecte el controlador para generar el reporte.")
            return
        try:
            total    = self.controller.obtener_total_basura()
            promedio = self.controller.obtener_promedio_basura()
            animales = self.controller.obtener_total_animales()
            por_tipo = self.controller.obtener_residuos_por_tipo()

            self.lbl_total.config(text=f"{total:.2f} kg")
            self.lbl_promedio.config(text=f"{promedio:.2f} kg")
            self.lbl_animales.config(text=str(animales))

            for fila in self.tabla.get_children():
                self.tabla.delete(fila)

            for i, (tipo, peso) in enumerate(por_tipo.items()):
                tag = "par" if i % 2 == 0 else "impar"
                self.tabla.insert("", "end",
                                   values=(tipo, f"{peso:.2f}"),
                                   tags=(tag,))

            self.lbl_footer.config(
                text=f"Reporte generado correctamente  ·  {len(por_tipo)} tipo(s) de residuo")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _limpiar(self):
        self.lbl_total.config(text="0.00 kg")
        self.lbl_promedio.config(text="0.00 kg")
        self.lbl_animales.config(text="0")
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        self.lbl_footer.config(
            text="Presione 'Generar Reporte' para cargar los datos.")

    def _salir(self):
        if self.controller and hasattr(self.controller, "volver_inicio"):
            self.controller.volver_inicio()
        else:
            self.winfo_toplevel().destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema Costero - Reporte General")
    root.geometry("1000x650")
    root.resizable(False, False)

    class ControladorFalso:
        def obtener_total_basura(self):    return 127.5
        def obtener_promedio_basura(self): return 15.9
        def obtener_total_animales(self):  return 8
        def obtener_residuos_por_tipo(self):
            return {"Plastico": 58.0, "Vidrio": 22.0, "Metal": 47.5}
        def volver_inicio(self): print("[SALIR]")

    ReporteVista(root, ControladorFalso())
    root.mainloop()