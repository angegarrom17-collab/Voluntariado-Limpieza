import tkinter as tk
from tkinter import ttk, messagebox


class JornadaVista(tk.Frame):

    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self._build()

    def _build(self):

        self.frame_formulario = tk.Frame(self)
        self.frame_formulario.pack(fill="both", expand=True)

        tk.Label(self.frame_formulario, text="Registrar Nueva Jornada", font=("Arial", 13, "bold")).grid(row=0,column=0,columnspan=2,pady=10)
        labels = [
            "ID Jornada:",
            "Ubicación / Playa:",
            "Fecha (Dia/Mes/Año):",
            "Hora de Inicio:",
            "Descripción:",
            "Estado (Planificada/Activa):"
        ]
        for i, text in enumerate(labels):
            tk.Label(self.frame_formulario, text=text, font=("Arial", 11)).grid(row=i + 1, column=0, padx=10, pady=6,
                                                                                sticky="e")

        self.entry_id = tk.Entry(self.frame_formulario, width=35)
        self.entry_ubicacion = tk.Entry(self.frame_formulario, width=35)
        self.entry_fecha = tk.Entry(self.frame_formulario, width=35)
        self.entry_hora = tk.Entry(self.frame_formulario, width=35)
        self.entry_descripcion = tk.Entry(self.frame_formulario, width=35)
        self.entry_estado = tk.Entry(self.frame_formulario, width=35)

        self.entry_id.grid(row=1, column=1, padx=10, pady=6)
        self.entry_ubicacion.grid(row=2, column=1, padx=10, pady=6)
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=6)
        self.entry_hora.grid(row=4, column=1, padx=10, pady=6)
        self.entry_descripcion.grid(row=5, column=1, padx=10, pady=6)
        self.entry_estado.grid(row=6, column=1, padx=10, pady=6)

        tk.Button(self.frame_formulario, text="Registrar Jornada", font=("Arial", 11, "bold"), width=22,
                  command=self._registrar).grid(row=7, column=0, columnspan=2, pady=15)
        tk.Button(self.frame_formulario, text="Listar Jornadas", font=("Arial", 11), width=22,
                  command=self._ir_a_lista).grid(row=8, column=0, columnspan=2, pady=5)


#---------------lista---------------------------------
        self.frame_tabla = tk.Frame(self)

        tk.Label(self.frame_tabla, text="Lista de Jornadas Registradas", font=("Arial", 12, "bold")).grid(row=0, column=0,columnspan=2,pady=10)

        nombres_columnas = ("ID", "Ubicación", "Fecha", "Hora", "Descripción", "Estado")
        self.tabla_jornadas = ttk.Treeview(self.frame_tabla, columns=nombres_columnas, show="headings", height=8)

        for nombre_columna in nombres_columnas:
            self.tabla_jornadas.heading(nombre_columna, text=nombre_columna)
            self.tabla_jornadas.column(nombre_columna, width=110, anchor="center")
        self.tabla_jornadas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.frame_tabla, text="Actualizar lista", command=self._cargar_tabla).grid(row=2, column=0, pady=8)
        tk.Button(self.frame_tabla, text="Volver al Registro", command=self._ir_a_formulario).grid(row=2, column=1,
                                                                                                   pady=8)

    def _ir_a_lista(self):
        self.frame_formulario.pack_forget()
        self.frame_tabla.pack(fill="both", expand=True)
        self._cargar_tabla()

    def _ir_a_formulario(self):
        self.frame_tabla.pack_forget()
        self.frame_formulario.pack(fill="both", expand=True)


    def _registrar(self):
        try:
            id_jornada = self.entry_id.get()
            ubicacion = self.entry_ubicacion.get()
            fecha = self.entry_fecha.get()
            hora = self.entry_hora.get()
            descripcion = self.entry_descripcion.get()
            estado = self.entry_estado.get()

            if not id_jornada.strip() or not ubicacion.strip():
                raise ValueError("El ID y la Ubicación son obligatorios.")

            self.controller.registrar_jornada(
                id_jornada, ubicacion, fecha, hora, descripcion, estado
            )

            messagebox.showinfo("Éxito", "Jornada registrada correctamente.")
            self._limpiar_campos()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def _limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_ubicacion.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)

    def _cargar_tabla(self):
        for fila in self.tabla_jornadas.get_children():
            self.tabla_jornadas.delete(fila)

        for jor in self.controller.obtener_todas_las_jornadas():
            self.tabla_jornadas.insert("", "end", values=(
                jor["id_jornada"],
                jor["ubicacion"],
                jor["fecha"],
                jor["hora"],
                jor["descripcion"],
                jor["estado"]
            ))



#------------------Mini main-------------------------

if __name__ == "__main__":
    class ControladorJornadasFalso:
        def __init__(self):
            self.jornadas_db = []

        def registrar_jornada(self, id_j, ubi, fec, hor, desc, est):
            nueva_jornada = {
                "id_jornada": id_j,
                "ubicacion": ubi,
                "fecha": fec,
                "hora": hor,
                "descripcion": desc,
                "estado": est
            }
            self.jornadas_db.append(nueva_jornada)

        def obtener_todas_las_jornadas(self):
            return self.jornadas_db


    root = tk.Tk()
    root.title("Jornadas")
    root.geometry("680x400")

    controlador_test = ControladorJornadasFalso()

    vista = JornadaVista(root, controller=controlador_test)
    vista.pack(fill="both", expand=True, padx=15, pady=15)

    root.mainloop()