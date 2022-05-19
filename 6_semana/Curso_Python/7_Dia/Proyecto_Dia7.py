# app cuenta bancaria

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'El cliente {self.nombre} {self.apellido} con Num. Cuenta {self.numero_cuenta} tiene un balance de: {self.balance}'

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print(f'Haz depositado {monto_deposito} con exito')

    def retirar(self,monto_retiro):
        if monto_retiro > self.balance:
            print("No puedes retirar esa cantidad tu saldo es menor")
        else:
            self.balance -= monto_retiro
            print(f"Haz Retirado {monto_retiro} con exito'")



def crear_cliente():
    nombre = input("Ingresa su nombre:")
    apellido = input("Ingresa tu apellido: ")
    num_cuenta = input("Ingresa tu numero de cuenta: ")
    #se crea la instancia
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = "x"

    while opcion != 3:

        menu = """ Bienvenido al Menu:
        [1] Depositar
        [2] Retirar
        [3] Salir
        """
        print(menu)
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            monto_depositar = int(input("Cuanto va a depositar?: "))
            mi_cliente.depositar(monto_depositar)
        elif opcion == 2:
            monto_retirar = int(input("Cuanto vas a retirar?: "))
            mi_cliente.retirar(monto_retirar)
        print(mi_cliente)

    print("Gracias por elegirnos")

inicio()





