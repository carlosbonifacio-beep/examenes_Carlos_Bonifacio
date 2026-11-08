from datetime import datetime

class Persona:
    def __init__(self, nombre="", edad=0, saldo=0.0, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = float(saldo)
        self.nacionalidad = nacionalidad
        self.fecha_registro = datetime.now()

    # Consultar saldo
    def consultar_saldo(self):
        print(f"El saldo actual de {self.nombre} es: S/. {self.saldo:.2f}")
        return self.saldo

    # Transferir dinero
    def transferir(self, destinatario, monto):
        # 1. Validar que el monto sea un valor numérico (int o float)
        if not isinstance(monto, (int, float)):
            print(" Operación rechazada: El monto debe ser un valor numérico.")
            return False

        # 2. Mayor a cero
        if monto <= 0:
            print(f" Operación rechazada: El monto a transferir (S/. {monto}) debe ser mayor a 0.")
            return False

        # 3. Saldo adecuado
        if monto > self.saldo:
            print(f" Operación rechazada: {self.nombre} no tiene saldo suficiente. Saldo disponible: S/. {self.saldo:.2f}, Intento de envío: S/. {monto:.2f}")
            return False

        self.saldo -= monto
        destinatario.saldo += monto
        print(f" Transferencia exitosa: {self.nombre} transfirió S/. {monto:.2f} a {destinatario.nombre}.")
        return True

# Crear dos personas con saldo inicial
persona1 = Persona(nombre="Enrique", edad=25, saldo=500.0)
persona2 = Persona(nombre="Giorgia", edad=30, saldo=200.0)

print("----- SALDOS INICIALES -----")
persona1.consultar_saldo()
persona2.consultar_saldo()

print("----- CASO 1: Transferencia válida -----")
# Juan transfiere 150 soles a María
persona1.transferir(persona2, 150.0)

# Saldos actualizados
persona1.consultar_saldo()
persona2.consultar_saldo()

print("----- CASO 2: Transferencia rechazada (Saldo insuficiente) -----")
# María intenta transferir 500 soles a Juan (solo tiene 350 soles)
persona2.transferir(persona1, 500.0)

# Sin cambios
persona1.consultar_saldo()
persona2.consultar_saldo()

print("----- CASO 3: Transferencia rechazada (Monto menor o igual a cero) -----")
# Juan intenta transferir un monto de 0 o negativo
persona1.transferir(persona2, -50.0)


