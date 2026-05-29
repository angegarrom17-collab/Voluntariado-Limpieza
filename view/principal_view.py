from tkinter import *
from PIL import Image, ImageTk

# ---------------- VENTANA ----------------

ventana = Tk()
ventana.title("Protección del Mar")
ventana.geometry("1000x650")
ventana.resizable(False, False)

# ---------------- IMAGEN DE FONDO ----------------

imagen = Image.open("marr.png")

imagen = imagen.resize((1000, 650))

fondo = ImageTk.PhotoImage(imagen)

labelFondo = Label(ventana, image=fondo)
labelFondo.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- TITULO ----------------

titulo = Label(
    ventana,
    text="🌊 PROTEJAMOS NUESTRO MAR 🌊",
    font=("Comic Sans MS", 24, "bold"),
    fg="#1b4f72",
    bg="#BEEED9"
)

titulo.place(x=210, y=25)

# ---------------- SUBTITULO ----------------

subtitulo = Label(
    ventana,
    text="Pequeñas acciones, grandes cambios",
    font=("Comic Sans MS", 16, "bold"),
    fg="#1b4f72",
    bg="#BEEED9"
)

subtitulo.place(x=300, y=80)

# ---------------- FRAME BOTONES ----------------

frame = Frame(
    ventana,
    bg="#C0EEE4",
    bd=0
)

frame.place(x=170, y=170)

# ---------------- ESTILO ----------------

fuente = ("Comic Sans MS", 12, "bold")

# ---------------- FILA 1 ----------------

btnUsuarios = Button(
    frame,
    text="👤\nUsuarios",
    font=fuente,
    bg="#bde0fe",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnUsuarios.grid(row=0, column=0, padx=15, pady=15)

# ----------------

btnJornadas = Button(
    frame,
    text="🌊\nJornadas",
    font=fuente,
    bg="#c8f2c2",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnJornadas.grid(row=0, column=1, padx=15, pady=15)

# ----------------

btnVoluntarios = Button(
    frame,
    text="🤝\nVoluntarios",
    font=fuente,
    bg="#fff1b6",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnVoluntarios.grid(row=0, column=2, padx=15, pady=15)

# ----------------

btnZona = Button(
    frame,
    text="📍\nZona",
    font=fuente,
    bg="#d8c6ff",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnZona.grid(row=0, column=3, padx=15, pady=15)

# ---------------- FILA 2 ----------------

btnMaterial = Button(
    frame,
    text="♻️\nMaterial",
    font=fuente,
    bg="#ffd6d6",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnMaterial.grid(row=1, column=0, padx=15, pady=15)

# ----------------

btnAnimal = Button(
    frame,
    text="🐢\nAnimal\nAfectado",
    font=fuente,
    bg="#caf0f8",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnAnimal.grid(row=1, column=1, padx=15, pady=15)

# ----------------

btnBasura = Button(
    frame,
    text="🗑️\nBasura\nRecolectada",
    font=fuente,
    bg="#e0ccff",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnBasura.grid(row=1, column=2, padx=15, pady=15)

# ----------------

btnReporte = Button(
    frame,
    text="📊\nReporte",
    font=fuente,
    bg="#ffdfba",
    fg="#0b3c5d",
    width=15,
    height=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)

btnReporte.grid(row=1, column=3, padx=15, pady=15)

# ---------------- MENSAJE ----------------

mensaje = Label(
    ventana,
    text="Juntos hacemos la diferencia 🌎",
    font=("Comic Sans MS", 14, "bold"),
    fg="white",
    bg="#000000"
)

mensaje.place(x=330, y=600)

# ---------------- BOTON SALIR ----------------

btnSalir = Button(
    ventana,
    text="✖",
    font=("Comic Sans MS", 10, "bold"),
    bg="white",
    fg="#0b3c5d",
    bd=0,
    relief="flat",
    width=3,
    cursor="hand2",
    command=ventana.destroy
)

btnSalir.place(x=950, y=610)

# ---------------- EJECUTAR ----------------

ventana.mainloop()

if __name__ == "__main__":
    class PrincipalView:
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