import tkinter as tk
from view.principal_view import PrincipalView
from view.voluntario_view import VoluntarioVistaModerna


class ControladorPrincipal:
    def __init__(self):
        # 1. Creamos la ventana de la aplicación
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión Ecológica")
        self.root.geometry("950x600")

        # 2. Base de datos temporal en memoria para los voluntarios
        self.voluntarios_db = []

        # 3. Cargamos la VISTA PRINCIPAL primero (Menú de inicio)
        # Le pasamos 'self' como controlador para que la vista pueda pedir acciones
        self.vista_actual = PrincipalView(self.root, controller=self)

    def mostrar_registro_voluntarios(self):
        """
        Este método limpia la pantalla principal y monta encima
        la vista celeste de registro de voluntarios.
        """
        # Destruimos o despaquetamos la vista principal para limpiar la ventana
        if hasattr(self, 'vista_actual'):
            self.vista_actual.pack_forget()  # Si usa pack
            # self.vista_actual.grid_forget() # Descomenta esta línea si tu PrincipalView usa grid

        # Instanciamos y mostramos la pantalla de voluntarios en la misma ventana
        self.vista_actual = VoluntarioVistaModerna(self.root, controller=self)

    def registrar_voluntario(self, id_v, nom, tel, edad, corr, org):
        """ Guarda los datos del voluntario en la lista """
        nuevo_voluntario = {
            "id_voluntario": id_v,
            "nombre": nom,
            "telefono": tel,
            "edad": edad,
            "correo": corr,
            "organizacion": org
        }
        self.voluntarios_db.append(nuevo_voluntario)
        print(f" Guardado con éxito: {nom}")

    def obtener_todos_los_voluntarios(self):
        """ Devuelve la lista para la tabla de voluntarios """
        return self.voluntarios_db

    def iniciar_aplicacion(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ControladorPrincipal()
    app.iniciar_aplicacion()