import tkinter as tk
from tkinter import messagebox

class BancoView:
    def __init__(self, master):  # Asegúrate de que 'master' esté aquí
        self.master = master
        self.master.title("Banco")

        self.saldo_label = tk.Label(master, text="Saldo: 0")
        self.saldo_label.pack()

        self.cantidad_entry = tk.Entry(master)
        self.cantidad_entry.pack()

        self.depositar_button = tk.Button(master, text="Depositar", command=self.depositar)
        self.depositar_button.pack()

        self.retirar_button = tk.Button(master, text="Retirar", command=self.retirar)
        self.retirar_button.pack()

        self.consultar_button = tk.Button(master, text="Consultar Saldo", command=self.consultar_saldo)
        self.consultar_button.pack()

    def depositar(self):
        cantidad = float(self.cantidad_entry.get())
        return cantidad

    def retirar(self):
        cantidad = float(self.cantidad_entry.get())
        return cantidad

    def consultar_saldo(self, saldo):
        self.saldo_label.config(text=f"Saldo: {saldo}")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)