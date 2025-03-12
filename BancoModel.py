class BancoModel:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def consultar_saldo(self):
        return self.saldo