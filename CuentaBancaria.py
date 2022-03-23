class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    nombre_banco = "Cuenta Independencia Bank07"
    def __init__(self, tasa_interes=0.01, balance=0.0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
    def deposito(self, amount):
        self.balance +=amount
        return self
    def retiro(self, amount):
        self.balance -=amount
        return self
    def mostrar_info_cuenta(self):
        print("Estimado tienes un balance de cuenta de:", self.balance)
    def generar_interes(self):
        self.balance+=(self.balance*self.tasa_interes)
        return self
primera_cuenta=CuentaBancaria()
segunda_cuenta=CuentaBancaria()
primera_cuenta.deposito(2000).deposito(2000).deposito(2000).retiro(3000).generar_interes().mostrar_info_cuenta()
segunda_cuenta.deposito(1000000).deposito(1000000).retiro(2000).retiro(3000).retiro(7000).retiro(2000).generar_interes().mostrar_info_cuenta()