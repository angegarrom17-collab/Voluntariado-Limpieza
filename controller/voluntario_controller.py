from tkinter import messagebox
from view.voluntario_view import VoluntarioVistaModerna


class ControladorVoluntario:
    def __init__(self, root, servicio, app_controller=None):
        """
        :param root: Es el self.contenedor que viene del AppController
        :param servicio: Instancia de VoluntarioServicio
        :param app_controller: Instancia del AppController (para volver al menú)
        """
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

    def mostrar_menu_principal(self):
        """Delegamos la navegación de regreso al AppController."""
        if self.app_controller and hasattr(self.app_controller, 'mostrar_menu_principal'):
            self.app_controller.mostrar_menu_principal()