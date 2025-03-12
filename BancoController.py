class BancoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.vista.depositar_button.config(command=self.realizar_deposito)
        self.vista.retirar_button.config(command=self.realizar_retiro)
        self.vista.consultar_button.config(command=self.consultar_saldo)

    def realizar_deposito(self):
        cantidad = self.vista.depositar()
        if self.modelo.depositar(cantidad):
            self.vista.mostrar_mensaje("Depósito exitoso.")
        else:
            self.vista.mostrar_mensaje("Error en el depósito.")

    def realizar_retiro(self):
        cantidad = self.vista.retirar()
        if self.modelo.retirar(cantidad):
            self.vista.mostrar_mensaje("Retiro exitoso.")
        else:
            self.vista.mostrar_mensaje("Error en el retiro. Saldo insuficiente.")

    def consultar_saldo(self):
        saldo = self.modelo.consultar_saldo()
        self.vista.consultar_saldo(saldo)