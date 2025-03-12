import tkinter as tk
from BancoModel import BancoModel
from BancoView import BancoView
from BancoController import BancoController

if __name__ == "__main__":
    modelo = BancoModel()
    root = tk.Tk()
    vista = BancoView(root)  # Asegúrate de pasar 'root' aquí
    controlador = BancoController(modelo, vista)
    root.mainloop()