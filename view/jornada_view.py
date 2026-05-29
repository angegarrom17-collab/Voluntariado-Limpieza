import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


class JornadaVistaModerna(tk.Frame):
    def __init__(self, parent, controller=None):
        # Heredamos de tk.Frame de manera estándar
        super().__init__(parent)
        self.controller = controller

        # Empaquetamos para llenar la ventana de 1000x650
        self.pack(fill="both", expand=True)
        self._build_interface()

    def _build_interface(self):
        # 1. 🖼️ GENERACIÓN AUTOMÁTICA DEL FONDO CON ALGAS EN LOS BORDES
        ancho, alto = 1000, 650
        # Fondo base con el color verde pastel de la aplicación (#BEEED9)
        imagen_fondo = Image.new("RGBA", (ancho, alto), "#BEEED9")
        draw = ImageDraw.Draw(imagen_fondo)

        try:
            # Intentamos cargar el archivo de imagen de alga transparente
            alga_original = Image.open("view/alga.png")
        except FileNotFoundError:
            try:
                alga_original = Image.open("alga.png")
            except FileNotFoundError:
                alga_original = None

        # Si el archivo alga.png existe, lo replicamos en los bordes
        if alga_original:
            alga_borde = alga_original.resize((80, 100))
            # Borde izquierdo
            for y in range(0, alto, 90):
                imagen_fondo.paste(alga_borde, (10, y), alga_borde)
            # Borde derecho
            for y in range(0, alto, 90):
                imagen_fondo.paste(alga_borde, (910, y), alga_borde)
        else:
            # SI NO ENCUENTRA EL ARCHIVO: Dibuja algas vectoriales artísticas para que no falle
            for y in range(30, alto, 120):
                # Siluetas de algas en la izquierda
                draw.chord([(-20, y), (60, y + 100)], 270, 90, fill="#5F7A61")
                draw.chord([(-10, y + 40), (40, y + 120)], 270, 90, fill="#4A604C")
                # Siluetas de algas en la derecha
                draw.chord([(940, y), (1020, y + 100)], 90, 270, fill="#5F7A61")
                draw.chord([(960, y + 40), (1010, y + 120)], 90, 270, fill="#4A604C")

        # Convertimos la imagen procesada a un formato compatible con Tkinter
        self.foto_fondo = ImageTk.PhotoImage(imagen_fondo)

        # Label que sostiene el fondo completo
        label_fondo = tk.Label(self, image=self.foto_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # 2. 🌊 TÍTULO PRINCIPAL (Centrado sobre el fondo generado)
        self.titulo = tk.Label(
            self,
            text="🌊 Registrar Nueva Jornada 🌊",
            font=("Comic Sans MS", 22, "bold"),
            bg="#BEEED9",
            fg="#1b4f72"
        )
        self.titulo.place(x=250, y=25)

        # 3. 📝 CONTENEDOR DE CAMPOS (Totalmente fusionado con el fondo)
        frame_campos = tk.Frame(self, bg="#BEEED9")
        frame_campos.place(x=200, y=110)

        labels_texto = [
            "ID Jornada:",
            "Fecha:",
            "Descripción:",
            "Basura (kg):",
            "Observaciones:",
            "ID Zona:"
        ]

        self.entries = {}

        # Ciclo de rejilla (Grid) directo y limpio adaptado a la clase
        for i, texto in enumerate(labels_texto):
            lbl = tk.Label(
                frame_campos, text=texto, font=("Comic Sans MS", 12, "bold"),
                bg="#BEEED9", fg="#1b4f72"
            )
            lbl.grid(row=i, column=0, padx=15, pady=8, sticky="e")

            entry = tk.Entry(
                frame_campos, font=("Arial", 11), width=42,
                bd=1, relief="solid"
            )
            entry.grid(row=i, column=1, padx=15, pady=8, sticky="w")

            self.entries[texto] = entry

        # 4. 🎛️ SECCIÓN DE BOTONES (Alineados abajo en el espacio limpio)
        frame_botones = tk.Frame(self, bg="#BEEED9")
        frame_botones.place(x=380, y=490)

        self.btn_registrar = tk.Button(
            frame_botones,
            text="Registrar Jornada",
            font=("Comic Sans MS", 12, "bold"),
            bg="#5F7A61",
            fg="#FFFFFF",
            width=22,
            bd=1,
            relief="solid",
            cursor="hand2",
            command=self.registrar_jornada
        )
        self.btn_registrar.pack(pady=5)

        self.btn_reporte = tk.Button(
            frame_botones,
            text="Ver Reporte",
            font=("Comic Sans MS", 12),
            bg="#7F8C8D",
            fg="#FFFFFF",
            width=22,
            bd=1,
            relief="solid",
            cursor="hand2",
            command=self.ver_reporte
        )
        self.btn_reporte.pack(pady=5)

    def registrar_jornada(self):
        """ Captura los strings de las cajas de texto """
        id_j = self.entries["ID Jornada:"].get().strip()
        fecha = self.entries["Fecha:"].get().strip()
        desc = self.entries["Descripción:"].get().strip()
        basura = self.entries["Basura (kg):"].get().strip()
        obs = self.entries["Observaciones:"].get().strip()
        zona = self.entries["ID Zona:"].get().strip()

        if not (id_j and fecha and desc and basura and zona):
            messagebox.showwarning("Atención", "Por favor, complete los campos obligatorios.")
            return

        try:
            if self.controller:
                self.controller.registrar_nueva_jornada(id_j, fecha, desc, basura, obs, zona)
            messagebox.showinfo("Éxito", f"Jornada '{id_j}' registrada correctamente.")
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ver_reporte(self):
        messagebox.showinfo("Navegación", "Abriendo módulo de reportes...")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


# --- EJECUCIÓN DEL MÓDULO INDEPENDIENTE ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba de Fondo Dinámico Marina")
    root.geometry("1000x650")
    root.resizable(False, False)

    app = JornadaVistaModerna(root)

    root.mainloop()