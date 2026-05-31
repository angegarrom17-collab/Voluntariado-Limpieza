from model.animal_afectado import AnimalAfectado
from model.basura_recolectada import BasuraRecolectada


class FaunaController:

    def __init__(self, vista_animal, vista_basura, fauna_repository):
        self.vista_animal = vista_animal
        self.vista_basura = vista_basura
        self.repo = fauna_repository

        # ---------------- BOTONES ANIMAL ----------------
        if self.vista_animal:
            self.vista_animal.boton_registrar.config(command=self.registrar_animal)
            self.vista_animal.boton_limpiar.config(command=self.limpiar_animal)
            self.vista_animal.boton_buscar.config(command=self.buscar_animal)
            self.vista_animal.boton_menu.config(command=self.volver_menu)

            self.cargar_tabla_animales()

        # ---------------- BOTONES BASURA ----------------
        if self.vista_basura:
            self.vista_basura.boton_registrar.config(command=self.registrar_basura)
            self.vista_basura.boton_limpiar.config(command=self.limpiar_basura)
            self.vista_basura.boton_menu.config(command=self.volver_menu)

            self.cargar_tabla_basura()

    # =========================================================
    #  ANIMALES
    # =========================================================

    def registrar_animal(self):
        try:
            especie = self.vista_animal.entry_especie.get()
            estado = self.vista_animal.entry_estado.get()
            descripcion = self.vista_animal.entry_descripcion.get()

            animal = AnimalAfectado(especie, estado, descripcion)
            self.repo.agregar_animal(animal)

            self.cargar_tabla_animales()
            self.limpiar_animal()

        except Exception as e:
            print("Error animal:", e)

    def limpiar_animal(self):
        self.vista_animal.entry_id.delete(0, "end")
        self.vista_animal.entry_especie.delete(0, "end")
        self.vista_animal.entry_estado.delete(0, "end")
        self.vista_animal.entry_descripcion.delete(0, "end")

    def buscar_animal(self):
        pass

    def cargar_tabla_animales(self):
        if not self.vista_animal:
            return

        for fila in self.vista_animal.tabla.get_children():
            self.vista_animal.tabla.delete(fila)

        for i, animal in enumerate(self.repo.obtener_animales()):
            self.vista_animal.tabla.insert(
                "",
                "end",
                values=(i, animal.especie, animal.estado, animal.descripcion)
            )

    # =========================================================
    # 🗑 BASURA
    # =========================================================

    def registrar_basura(self):
        try:
            tipo = self.vista_basura.entry_tipo.get()
            peso = float(self.vista_basura.entry_peso.get())

            basura = BasuraRecolectada(tipo, peso, "N/A")
            self.repo.agregar_basura(basura)

            self.cargar_tabla_basura()
            self.limpiar_basura()

        except Exception as e:
            print("Error basura:", e)

    def limpiar_basura(self):
        self.vista_basura.entry_tipo.delete(0, "end")
        self.vista_basura.entry_peso.delete(0, "end")

    def cargar_tabla_basura(self):
        if not self.vista_basura:
            return

        for fila in self.vista_basura.tabla.get_children():
            self.vista_basura.tabla.delete(fila)

        for basura in self.repo.obtener_basura():
            self.vista_basura.tabla.insert(
                "",
                "end",
                values=(basura.tipoResiduo, basura.pesoKilos)
            )

    def volver_menu(self):
        from view.principal_view import PrincipalView

        root = self.vista_animal.master if self.vista_animal else self.vista_basura.master

        for widget in root.winfo_children():
            widget.destroy()

        PrincipalView(root)
