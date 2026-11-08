from datetime import datetime

class Persona:
    # 1. Datos iniciales
    def __init__(self, nombre="", edad=0, saldo=0.0, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

        self.fecha_registro = datetime.now()

    # 2. Registro
    def registrar_persona(self):
        self.nombre = input("Ingrese el nombre de la persona: ")

        while True:
            try:
                edad_ingresada = int(input("Ingrese la edad: "))
                if edad_ingresada < 0:
                    print("Error: La edad no puede ser negativa. Intente nuevamente.")
                else:
                    self.edad = edad_ingresada
                    break
            except ValueError:
                print("Error: La edad debe ser un número entero válido. Intente nuevamente.")

    # 3. Cumpleaños
    def cumpleanios(self):
        self.edad += 1

    def mostrar_fecha_registro(self):
        fecha_formateada = self.fecha_registro.strftime("%Y-%m-%d %H:%M")
        print(f"Fecha y hora de registro de {self.nombre}: {fecha_formateada}")

# 4. Dos objetos de la clase Persona
print("----- REGISTRO DE PERSONA 1 ------")
persona1 = Persona()
persona1.registrar_persona()

print("----- REGISTRO DE PERSONA 2 -----")
persona2 = Persona()
persona2.registrar_persona()

# Cumpleaños
persona1.cumpleanios()
persona2.cumpleanios()

# Edades actualizadas
print("----- EDADES ACTUALIZADAS Y REGISTRO -----")
print(f"{persona1.nombre} ahora tiene {persona1.edad} años.")
persona1.mostrar_fecha_registro()

print(f"{persona2.nombre} ahora tiene {persona2.edad} años.")
persona2.mostrar_fecha_registro()