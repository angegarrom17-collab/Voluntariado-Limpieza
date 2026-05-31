class MaterialController:

    def __init__(self, vista, material_service):
        self.vista = vista
        self.service = material_service

        # ---------------- BOTONES ----------------
        self.vista.boton_registrar.config(command=self.registrar)
        self.vista.boton_limpiar.config(command=self.limpiar)
        self.vista.boton_usar.config(command=self.usar_material)
        self.vista.boton_buscar.config(command=self.buscar)
        self.vista.boton_menu.config(command=self.volver_menu)

        # Cargar tabla al iniciar
        self.cargar_tabla()

    # =========================================================
    # REGISTRAR MATERIAL
    # =========================================================

    def registrar(self):
        try:
            idMaterial = self.vista.entry_id.get()
            nombre = self.vista.entry_nombre.get()
            unidad = self.vista.entry_unidad.get()
            cantidad = int(self.vista.entry_cantidad.get())

            self.service.registrar_material(
                idMaterial,
                nombre,
                unidad,
                cantidad
            )

            self.cargar_tabla()
            self.limpiar()

        except Exception as e:
            print("Error:", e)

    # =========================================================
    # LIMPIAR
    # =========================================================

    def limpiar(self):
        self.vista.entry_id.delete(0, "end")
        self.vista.entry_nombre.delete(0, "end")
        self.vista.entry_unidad.delete(0, "end")
        self.vista.entry_cantidad.delete(0, "end")

    # =========================================================
    # USAR MATERIAL
    # =========================================================

    def usar_material(self):
        try:
            idMaterial = self.vista.entry_id.get()
            cantidad = int(self.vista.entry_cantidad.get())

            self.service.usar_material(idMaterial, cantidad)

            self.cargar_tabla()

        except Exception as e:
            print("Error:", e)

    # =========================================================
    # BUSCAR
    # =========================================================

    def buscar(self):
        try:
            idMaterial = self.vista.entry_id.get()
            materiales = self.service.obtener_materiales()

            for mat in materiales:
                if mat.idMaterial == idMaterial:
                    self.vista.entry_nombre.delete(0, "end")
                    self.vista.entry_nombre.insert(0, mat.nombre)

                    self.vista.entry_unidad.delete(0, "end")
                    self.vista.entry_unidad.insert(0, mat.unidadMedida)

                    self.vista.entry_cantidad.delete(0, "end")
                    self.vista.entry_cantidad.insert(0, mat.cantidadDisponible)

        except Exception as e:
            print("Error:", e)

    # =========================================================
    # TABLA
    # =========================================================

    def cargar_tabla(self):
        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        materiales = self.service.obtener_materiales()

        for mat in materiales:
            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    mat.idMaterial,
                    mat.nombre,
                    mat.unidadMedida,
                    mat.cantidadDisponible
                )
            )

    def volver_menu(self):
        from view.principal_view import PrincipalView

        root = self.vista.master

        for widget in root.winfo_children():
            widget.destroy()

        PrincipalView(root)
