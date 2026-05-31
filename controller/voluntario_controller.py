import tkinter as tk  #  ¡EL VERDADERO TKINTER!
from tkinter import messagebox, ttk
from view.voluntario_view import VoluntarioVistaModerna


class ControladorVoluntario:
    def __init__(self, root, servicio, app_controller=None):

        self.root = root
        self.servicio = servicio
        self.app_controller = app_controller

        # 1. Creamos la vista pasándole ESTE controlador desde el nacimiento
        self.vista = VoluntarioVistaModerna(self.root, controller=self)

        # 2. Le hacemos el pack INMEDIATAMENTE aquí dentro para evitar la pantalla blanca
        self.vista.pack(fill="both", expand=True)

    def registrar_voluntario(self, id_v: str, nom: str, tel: str, edad_str: str, corr: str, org: str):
        """Recibe los datos de la vista, los procesa y los manda al servicio."""
        try:
            edad = int(edad_str)
        except ValueError:
            messagebox.showerror("Error de Tipo", "La edad debe ser un número entero válido.")
            return

        try:
            # Lógica de negocio real
            self.servicio.registrar_voluntario(
                id_voluntario=id_v,
                nombre=nom,
                telefono=tel,
                edad=edad,
                correo=corr,
                organizacion=org
            )
            messagebox.showinfo("Éxito", f"¡Gracias {nom}! Interés registrado correctamente.")

            if hasattr(self.vista, '_limpiar_campos'):
                self.vista._limpiar_campos()

        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error en el sistema: {str(e)}")

    def mostrar_tabla_voluntarios(self):
        """Abre una ventana flotante con la tabla de voluntarios registrados."""
        # 1. Obtener los datos reales del servicio
        lista_voluntarios = self.servicio.obtener_todos_los_voluntarios()

        # 2. Crear la ventana flotante (Toplevel con 'l' minúscula)
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Voluntarios Registrados")
        ventana_tabla.geometry("850x400")
        ventana_tabla.configure(bg="#BEEED9")
        ventana_tabla.grab_set()

        # Título interno
        tk.Label(
            ventana_tabla, text="LISTADO DE VOLUNTARIOS",
            font=("Segoe UI", 14, "bold"), fg="#1b4f72", bg="#BEEED9"
        ).pack(pady=15)

        # 3. Contenedor para la tabla
        frame_tabla = tk.Frame(ventana_tabla)
        frame_tabla.pack(expand=True, fill="both", padx=20, pady=10)

        scroll = tk.Scrollbar(frame_tabla)
        scroll.pack(side="right", fill="y")

        # 4. Estructura de las columnas (Treeview)
        columnas = ("id", "nombre", "telefono", "edad", "correo", "organizacion")
        tabla = ttk.Treeview(
            frame_tabla, columns=columnas, show="headings",
            yscrollcommand=scroll.set, height=12
        )
        scroll.config(command=tabla.yview)

        # Cabeceras
        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre Completo")
        tabla.heading("telefono", text="Teléfono")
        tabla.heading("edad", text="Edad")
        tabla.heading("correo", text="Correo Electrónico")
        tabla.heading("organizacion", text="Organización")

        # Ancho de columnas
        tabla.column("id", width=80, anchor="center")
        tabla.column("nombre", width=180, anchor="w")
        tabla.column("telefono", width=100, anchor="center")
        tabla.column("edad", width=60, anchor="center")
        tabla.column("correo", width=180, anchor="w")
        tabla.column("organizacion", width=180, anchor="w")

        tabla.pack(expand=True, fill="both")

        # 5. Insertar datos
        for vol in lista_voluntarios:
            tabla.insert("", tk.END, values=(
                vol.get("id_voluntario", ""),
                vol.get("nombre", ""),
                vol.get("telefono", ""),
                vol.get("edad", ""),
                vol.get("correo", ""),
                vol.get("organizacion", "")
            ))

        # Botón para cerrar
        tk.Button(
            ventana_tabla, text="Cerrar Ventana", font=("Segoe UI", 10, "bold"),
            bg="#78909c", fg="white", bd=0, width=15, height=2, cursor="hand2",
            command=ventana_tabla.destroy
        ).pack(pady=15)


    def mostrar_menu_principal(self):
        """Delegamos la navegación de regreso al AppController."""
        if self.app_controller and hasattr(self.app_controller, 'mostrar_menu_principal'):
            self.app_controller.mostrar_menu_principal()