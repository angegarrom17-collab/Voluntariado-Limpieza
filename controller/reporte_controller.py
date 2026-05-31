class ReporteController:

    def __init__(self, vista, repo, service):
        self.vista = vista
        self.repo = repo
        self.service = service

        # ---------------- BOTONES ----------------
        self.vista.boton_menu.config(command=self.volver_menu)
        self.vista.boton_limpiar.config(command=self.limpiar_tabla)

        # Cargar datos al abrir
        self.actualizar_reporte()

    # ==================================================
    # ACTUALIZAR REPORTE
    # ==================================================

    def actualizar_reporte(self):

        lista_basura = self.repo.obtener_basura()
        lista_animales = self.repo.obtener_animales()

        total = self.service.calcular_total_basura(lista_basura)
        promedio = self.service.calcular_promedio_basura(lista_basura)
        cantidad_animales = self.service.contar_animales(lista_animales)
        residuos_tipo = self.service.obtener_residuos_por_tipo(lista_basura)

        # -------- LABELS --------
        self.vista.label_total.config(text=f"Total basura: {total} kg")
        self.vista.label_promedio.config(text=f"Promedio: {promedio:.2f} kg")
        self.vista.label_animales.config(
            text=f"Animales afectados: {cantidad_animales}"
        )

        # -------- TABLA --------
        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        for tipo, peso in residuos_tipo.items():
            self.vista.tabla.insert(
                "",
                "end",
                values=(tipo, peso)
            )

    # ==================================================
    # LIMPIAR REPORTE (NUEVO)
    # ==================================================

    def limpiar_tabla(self):

        # borrar tabla
        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)

        # resetear textos
        self.vista.label_total.config(text="Total basura: --- kg")
        self.vista.label_promedio.config(text="Promedio: --- kg")
        self.vista.label_animales.config(text="Animales afectados: ---")


    def volver_menu(self):
        from view.principal_view import PrincipalView

        root = self.vista.master

        for widget in root.winfo_children():
            widget.destroy()

        PrincipalView(root)
