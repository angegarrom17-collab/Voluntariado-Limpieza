import tkinter as tk
from view.principal_view import PrincipalView
from view.voluntario_view import VoluntarioVistaModerna


# NOTA: Asegúrate de importar las demás vistas si vas a usarlas más adelante:
# from view.usuario_view import UsuarioVista
# from view.zona_view import ZonaVista
# from view.jornada_view import JornadaVistaModerna


class ControladorPrincipal:
    def __init__(self):
        # 1. Creamos la ventana de la aplicación
        self.root = tk.Tk()
        self.root.title("Proyecto OFC Desarrollo - Protección del Mar")
        self.root.geometry("1000x650")  # Ajustado al tamaño de tu fondo (1000x650)

        # 2. Base de datos temporal en memoria para los voluntarios
        self.voluntarios_db = []

        # 3. Guardamos la vista actual
        self.vista_actual = None

        # Cargamos el Menú de inicio al arrancar
        self.mostrar_menu_principal()

    def limpiar_pantalla(self):
        """ Destruye por completo la vista anterior para que no deje residuos en la ventana """
        if self.vista_actual is not None:
            self.vista_actual.destroy()

    def mostrar_menu_principal(self):
        """ Regresa o muestra el menú principal """
        self.limpiar_pantalla()

        # Instanciamos la vista principal
        self.vista_actual = PrincipalView(self.root, controller=self)
        # Como tu PrincipalView ya tiene el self.pack() adentro, no hace falta ponerlo aquí.

    def mostrar_registro_voluntarios(self):
        """ Limpia la pantalla y monta la vista de voluntarios """
        self.limpiar_pantalla()

        # Instanciamos la pantalla de voluntarios
        self.vista_actual = VoluntarioVistaModerna(self.root, controller=self)

        # 🚨 ¡AQUÍ ESTABA EL TRUCO!
        # Forzamos a que se muestre en la ventana por si la vista no se empaqueta sola.
        self.vista_actual.pack(fill="both", expand=True)

    # --- Métodos para las demás vistas (Para cuando los conectes) ---

    def mostrar_registro_usuarios(self):
        """ Limpia la pantalla y monta la vista de usuarios """
        self.limpiar_contenedor()

        # Instanciamos UsuarioVista pasándole el contenedor y este controlador
        self.vista_actual = UsuarioVista(self.contenedor, controller=self)

        # Forzamos el empaquetado dinámico
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_registro_zonas(self):
        self.limpiar_pantalla()
        # self.vista_actual = ZonaVista(self.root, controller=self)
        # self.vista_actual.pack(fill="both", expand=True)
        print("Abriendo Zonas...")  # Temporal para pruebas

    def mostrar_registro_jornadas(self):
        self.limpiar_pantalla()
        # self.vista_actual = JornadaVistaModerna(self.root, controller=self)
        # self.vista_actual.pack(fill="both", expand=True)
        print("Abriendo Jornadas...")  # Temporal para pruebas

    # --- Lógica de Negocio ---

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
        print(f"✅ Guardado con éxito: {nom}")

    def obtener_todos_los_voluntarios(self):
        """ Devuelve la lista para la tabla de voluntarios """
        return self.voluntarios_db

    def iniciar_aplicacion(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ControladorPrincipal()
    app.iniciar_aplicacion()