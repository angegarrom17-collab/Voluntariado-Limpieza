import tkinter as tk
from tkinter import ttk, messagebox


class VoluntarioVista(tk.Frame):

    def __init__(self, root, controller):
        super().__init__(root)  # Quitamos el fondo personalizado
        self.controller = controller
        self._build()

    def _build(self):
        self.frame_formulario = tk.Frame(self)
        self.frame_formulario.pack(fill="both", expand=True)

        tk.Label(self.frame_formulario, text="Registrar Voluntario", font=("Arial", 13, "bold")).grid(row=0, column=0,
                                                                                                      columnspan=2,
                                                                                                      pady=10)

        labels = ["Identificador (ID):", "Nombre:", "Teléfono:", "Edad:", "Correo:", "Organización:"]
        for i, text in enumerate(labels):
            tk.Label(self.frame_formulario, text=text, font=("Arial", 11)).grid(row=i + 1, column=0, padx=10, pady=6,
                                                                                sticky="e")

        self.entry_id = tk.Entry(self.frame_formulario, width=35)
        self.entry_nombre = tk.Entry(self.frame_formulario, width=35)
        self.entry_telefono = tk.Entry(self.frame_formulario, width=35)
        self.entry_edad = tk.Entry(self.frame_formulario, width=35)
        self.entry_correo = tk.Entry(self.frame_formulario, width=35)
        self.entry_organizacion = tk.Entry(self.frame_formulario, width=35)

        self.entry_id.grid(row=1, column=1, padx=10, pady=6)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=6)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=6)
        self.entry_edad.grid(row=4, column=1, padx=10, pady=6)
        self.entry_correo.grid(row=5, column=1, padx=10, pady=6)
        self.entry_organizacion.grid(row=6, column=1, padx=10, pady=6)

        tk.Button(self.frame_formulario, text="Registrar Voluntario", font=("Arial", 11, "bold"), width=22,
                  command=self._registrar).grid(row=7, column=0, columnspan=2, pady=15)
        tk.Button(self.frame_formulario, text="Listar Voluntarios", font=("Arial", 11), width=22,
                  command=self._ir_a_lista).grid(row=8, column=0, columnspan=2, pady=5)



        #------------LISTA--------------------
        self.frame_tabla = tk.Frame(self)

        tk.Label(self.frame_tabla, text="Lista de Voluntarios Registrados", font=("Arial", 12, "bold")).grid(row=0,column=0, columnspan=2, pady=10)

        nombres_columnas = ("ID", "Nombre", "Teléfono", "Edad", "Correo", "Organización")
        self.tabla_voluntarios = ttk.Treeview(self.frame_tabla, columns=nombres_columnas, show="headings", height=8)

        for nombre_columna in nombres_columnas:
            self.tabla_voluntarios.heading(nombre_columna, text=nombre_columna)
            self.tabla_voluntarios.column(nombre_columna, width=100, anchor="center")
        self.tabla_voluntarios.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.frame_tabla, text="Actualizar lista", command=self._cargar_tabla).grid(row=2, column=0, pady=8)
        tk.Button(self.frame_tabla, text="Volver al Registro", command=self._ir_a_formulario).grid(row=2, column=1,pady=8)

    def _ir_a_lista(self):
        self.frame_formulario.pack_forget()
        self.frame_tabla.pack(fill="both", expand=True)
        self._cargar_tabla()

    def _ir_a_formulario(self):
        self.frame_tabla.pack_forget()
        self.frame_formulario.pack(fill="both", expand=True)

    def _registrar(self):
        try:
            id_voluntario = self.entry_id.get()
            nombre = self.entry_nombre.get()
            telefono = self.entry_telefono.get()
            edad_str = self.entry_edad.get()
            correo = self.entry_correo.get()
            organizacion = self.entry_organizacion.get()

            try:
                edad = int(edad_str)
            except ValueError:
                raise ValueError("La edad debe ser un número entero válido.")

            self.controller.registrar_voluntario(id_voluntario, nombre, telefono, edad, correo, organizacion)

            messagebox.showinfo("Éxito", "Voluntario registrado correctamente.")
            self._limpiar_campos()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def _limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_organizacion.delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_voluntarios.get_children():
            self.tabla_voluntarios.delete(fila)

        for volu in self.controller.obtener_todos_los_voluntarios():
            self.tabla_voluntarios.insert("", "end", values=(
                volu["id_voluntario"], volu["nombre"], volu["telefono"],
                volu["edad"], volu["correo"], volu["organizacion"]
            ))


#--------main para revisar-------------------------

if __name__ == "__main__":

    class ControladorVoluntariosFalso:
        def __init__(self):
            self.voluntarios_db = []

        def registrar_voluntario(self, id_v, nom, tel, edad, corr, org):
            if edad < 20:
                raise ValueError("El voluntario tiene que ser mayor de 20 años.")
            nuevo_dict = {
                "id_voluntario": id_v, "nombre": nom, "telefono": tel,
                "edad": edad, "correo": corr, "organizacion": org
            }
            self.voluntarios_db.append(nuevo_dict)

        def obtener_todos_los_voluntarios(self):
            return self.voluntarios_db


    root = tk.Tk()
    root.title("Voluntarios")
    root.geometry("650x400")

    controlador_test = ControladorVoluntariosFalso()

    vista = VoluntarioVista(root, controller=controlador_test)
    vista.pack(fill="both", expand=True, padx=15, pady=15)

    root.mainloop()