import tkinter as tk
# Importamos las dos vistas desde tu carpeta view
from view.principal_view import PrincipalView
from view.voluntario_view import VoluntarioVistaModerna


class ControladorPrincipal:
    def __init__(self):
        # 1. Configuración de la ventana raíz (Root)
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión Ecológica - Proyecto OFC")
        self.root.geometry("950x600")

        # 2. Base de datos simulada en memoria para guardar los voluntarios
        self.voluntarios_db = []

        # 3. Guardamos la vista actual en una variable para poder cambiarla después
        self.vista_actual = None

        # 4. Arrancamos mostrando la Vista Principal (El menú de inicio)
        self.mostrar_vista_principal()

    def mostrar_vista_principal(self):
        """ Limpia la pantalla y carga el menú de bienvenida """
        if self.vista_actual is not None:
            self.vista_actual.destroy()  # Destruye la vista anterior si existe

        # Creamos la vista principal pasándole la raíz y este controlador
        self.vista_actual = PrincipalView(self.root, controller=self)
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_registro_voluntarios(self):
        """ Limpia el menú de bienvenida y monta el formulario de voluntarios """
        if self.vista_actual is not None:
            self.vista_actual.destroy()  # Borra el menú principal de la ventana

        # Creamos la vista de voluntarios encima de la misma ventana
        self.vista_actual = VoluntarioVistaModerna(self.root, controller=self)
        self.vista_actual.pack(fill="both", expand=True)

    # --- MÉTODOS DE LOGICA PARA EL REGISTRO ---
    def registrar_voluntario(self, id_v, nom, tel, edad, corr, org):
        """ Recibe los datos capturados por el formulario celeste y los guarda """
        nuevo_voluntario = {
            "id_voluntario": id_v,
            "nombre": nom,
            "telefono": tel,
            "edad": edad,
            "correo": corr,
            "organizacion": org
        }
        self.voluntarios_db.append(nuevo_voluntario)
        print(f" LOG MAIN: ¡Voluntario {nom} registrado de forma exitosa!")

    def obtener_todos_los_voluntarios(self):
        """ Envía la lista de voluntarios de memoria cuando se abre la tabla """
        return self.voluntarios_db

    def iniciar_aplicacion(self):
        """ Enciende el ciclo principal de la interfaz """
        self.root.mainloop()



# --- PUNTO DE ENTRADA ÚNICO ---
if __name__ == "__main__":

    app = ControladorPrincipal()
    app.iniciar_aplicacion()