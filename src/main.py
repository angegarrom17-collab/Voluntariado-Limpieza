import tkinter as tk
from src.controller.app_controller import AppController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Monitoreo Costero")
    root.geometry("1000x650")
    root.resizable(False, False)
    app = AppController(root)
    app.mostrar_principal()
    root.mainloop()