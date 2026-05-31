import tkinter as tk
from tkinter import messagebox, ttk


class JornadaController:
    def __init__(self, root, servicio, app_controller=None):
        """
        :param root: Es el self.contenedor que viene del AppController
        :param servicio: Instancia de VoluntarioServicio (que maneja las jornadas)
        :param app_controller: Instancia del AppController central
        """
        self.root = root
        self.servicio = servicio
        self.app_controller = app_controller

        # Importamos la vista aquí para evitar importaciones circulares
        from view.jornada_view import JornadaVistaModerna

        # 1. Creamos la vista pasándole este controlador desde el nacimiento
        self.vista = JornadaVistaModerna(self.root, controller=self)

        # 2. Le hacemos el pack de inmediato para evitar pantallas en blanco
        self.vista.pack(fill="both", expand=True)

    def registrar_jornada(self, id_jornada: str, fecha: str, desc: str, basura_str: str, obs: str, id_zona: str):
        """Procesa, valida la conversión de enteros y envía al servicio."""
        # Validar que la cantidad de basura sea un número entero
        try:
            cantidad_basura = int(basura_str)
        except ValueError:
            messagebox.showerror("Error de Tipo", "La cantidad de basura (kg) debe ser un número entero válido.")
            return

        try:
            # Lógica de negocio real delegada al servicio
            self.servicio.registrar_jornada(
                id_jornada=id_jornada,
                fecha_jornada=fecha,
                descripcion=desc,
                cantidadBasuraTotal=cantidad_basura,
                observaciones=obs,
                id_zona=id_zona
            )
            messagebox.showinfo("Éxito", f"¡Jornada {id_jornada} registrada correctamente!")

            # Intentar limpiar campos si el método existe en la vista
            if hasattr(self.vista, '_limpiar_campos'):
                self.vista._limpiar_campos()

        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error en el sistema: {str(e)}")

    def mostrar_reporte_jornadas(self):
        """Abre una ventana flotante con el reporte real de jornadas."""
        # 1. Obtener los datos directamente del servicio conectado al archivo JSON
        try:
            lista_jornadas = self.servicio.obtener_reporte_jornadas()
            if not lista_jornadas:
                lista_jornadas = []
        except Exception:
            lista_jornadas = []

        # 2. Crear la ventana flotante (Toplevel)
        ventana_reporte = tk.Toplevel(self.root)
        ventana_reporte.title("Reporte de Jornadas de Limpieza")
        ventana_reporte.geometry("850x400")
        ventana_reporte.configure(bg="#BEEED9")
        ventana_reporte.grab_set()

        # Título
        tk.Label(
            ventana_reporte, text="REPORTE DE JORNADAS DE LIMPIEZA",
            font=("Segoe UI", 14, "bold"), fg="#1b4f72", bg="#BEEED9"
        ).pack(pady=15)

        # 3. Contenedor de la tabla
        frame_tabla = tk.Frame(ventana_reporte)
        frame_tabla.pack(expand=True, fill="both", padx=20, pady=10)

        scroll = tk.Scrollbar(frame_tabla)
        scroll.pack(side="right", fill="y")

        # 4. Estructura de las columnas de la tabla
        columnas = ("id", "fecha", "descripcion", "basura", "voluntarios")
        tabla = ttk.Treeview(
            frame_tabla, columns=columnas, show="headings",
            yscrollcommand=scroll.set, height=12
        )
        scroll.config(command=tabla.yview)

        # Cabeceras
        tabla.heading("id", text="ID Jornada")
        tabla.heading("fecha", text="Fecha")
        tabla.heading("descripcion", text="Descripción")
        tabla.heading("basura", text="Basura (kg)")
        tabla.heading("voluntarios", text="Cant. Voluntarios")

        # Ancho de columnas
        tabla.column("id", width=100, anchor="center")
        tabla.column("fecha", width=120, anchor="center")
        tabla.column("descripcion", width=280, anchor="w")
        tabla.column("basura", width=120, anchor="center")
        tabla.column("voluntarios", width=130, anchor="center")

        tabla.pack(expand=True, fill="both")

        # 5. Insertar los datos reales mapeando las llaves exactas del JSON
        for j in lista_jornadas:
            # Soportamos tanto llaves en mayúscula como en minúscula según tu capa de negocio
            id_j = j.get("ID", j.get("id_jornada", ""))
            fec = j.get("Fecha", j.get("fecha_jornada", ""))
            des = j.get("Descripción", j.get("descripcion", ""))
            bas = j.get("Basura (kg)", j.get("cantidadBasuraTotal", 0))
            vol = j.get("Voluntarios", 0)

            tabla.insert("", tk.END, values=(id_j, fec, des, bas, vol))

        # Botón para cerrar
        tk.Button(
            ventana_reporte, text="Cerrar Reporte", font=("Segoe UI", 10, "bold"),
            bg="#78909c", fg="white", bd=0, width=15, height=2, cursor="hand2",
            command=ventana_reporte.destroy
        ).pack(pady=15)

    def mostrar_menu_principal(self):
        """Regresar al menú usando AppController."""
        if self.app_controller and hasattr(self.app_controller, 'mostrar_menu_principal'):
            self.app_controller.mostrar_menu_principal()