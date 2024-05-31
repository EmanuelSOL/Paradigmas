#Emanuel Solis Orozco
#Paradigmas de la programacion
#Aplicacion banco
###############################

class Cliente:
    def __init__(self, nombre,):
        self.nombre = nombre

    def __str__(self):
        return f"Cliente: {self.nombre}"

class CuentaBancaria:
    def __init__(self, cliente, numero_cuenta, saldo=0.0):
        self.cliente = cliente
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Deposito exitoso: {monto}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso: {monto}")
        else:
            print("Saldo insufuciente")

    def __str__(self):
        return f"Cuenta {self.numero_cuenta} - Cliente: {self.cliente.nombre} - Saldo: {self.saldo}"
    
    
class CuentaActiva(CuentaBancaria):
    def __init__(self, cliente, numero_cuenta, saldo=0.0):
        super().__init__(cliente, numero_cuenta, saldo)

    def retirar(self, monto):
        if monto > 0 and (self.saldo + 1000) >= monto:
            self.saldo -= monto
            print(f"Retiro exitoso: {monto}")
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"Cuenta Activa: {self.numero_cuenta} || Cliente: {self.cliente.nombre} || Saldo: {self.saldo}"
    
    
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.cuentas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente agregado: {cliente}")

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta abierta: {cuenta}")

    def __str__(self):
        return f"Banco: {self.nombre} - Clientes: {len(self.clientes)} - Cuentas: {len(self.cuentas)}"


def main():
    mi_banco = Banco("Banco RakanCoins")

    nombre_cliente = input("Ingrese su nombre: ")
    cliente = Cliente(nombre_cliente)

    mi_banco.agregar_cliente(cliente)

    numero_cuenta = input("Ingrese el número de cuenta: ")
    cuenta = CuentaActiva(cliente, numero_cuenta)
    
    mi_banco.abrir_cuenta(cuenta)

    while True:
        print("\nElija una operación:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar saldo")
        print("0. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            print(cuenta)
        elif opcion == "0":
            print("Gracias por usar nuestro sistema bancario.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
