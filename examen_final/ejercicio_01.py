"""
Examen Final - Ejercicio 01: Sistema de alquiler de vehículos
"""

class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio if anio > 0 else 2020

    def actualizar_marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and nueva_marca.strip():
            self.marca = nueva_marca.strip()
        else:
            print("Error: La marca ingresada no es válida.")

    def actualizar_anio(self, nuevo_anio):
        if isinstance(nuevo_anio, int) and nuevo_anio > 0:
            self.anio = nuevo_anio
        else:
            print(f"Error: El año ({nuevo_anio}) debe ser un entero mayor que cero.")

    def mostrar_datos(self):
        print(f"Vehículo: {self.marca} {self.modelo} | Año: {self.anio}")


class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca, modelo, codigo, tarifa_diaria, anio=2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = 0.0
        self.actualizar_tarifa(tarifa_diaria)

    def obtener_tarifa(self):
        return self.__tarifa_diaria

    def actualizar_tarifa(self, nueva_tarifa):
        if isinstance(nueva_tarifa, (int, float)) and nueva_tarifa > 0:
            self.__tarifa_diaria = float(nueva_tarifa)
            return True
        else:
            print(f"Error: La tarifa ({nueva_tarifa}) debe ser mayor que cero. No se modificó la tarifa.")
            return False

    def aumentar_tarifa(self, porcentaje=10):
        if porcentaje > 0:
            self.__tarifa_diaria *= (1 + porcentaje / 100)
            print(f"Tarifa aumentada en {porcentaje}%. Nueva tarifa: S/. {self.__tarifa_diaria:.2f}")

    def calcular_descuento(self, dias_alquiler):
        if dias_alquiler <= 0:
            print("Error: Los días de alquiler deben ser mayores a cero.")
            return

        importe_bruto = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            porcentaje_desc = 5
        elif 2 <= dias_alquiler <= 5:
            porcentaje_desc = 10
        else:
            porcentaje_desc = 15

        descuento = importe_bruto * (porcentaje_desc / 100)
        total_final = importe_bruto - descuento

        print(f"Código: {self.codigo} | Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.anio}")
        print(f"Tarifa actual: S/. {self.__tarifa_diaria:.2f} | Días: {dias_alquiler}")
        print(f"Importe antes del descuento: S/. {importe_bruto:.2f}")
        print(f"Descuento aplicado ({porcentaje_desc}%): S/. {descuento:.2f}")
        print(f"Total final a pagar: S/. {total_final:.2f}\n")

print("----- 1. CREACIÓN Y ACTUALIZACIÓN DE VEHÍCULOS -----")
v1 = VehiculoAlquiler("Toyota", "Corolla", "ALQ-001", 100.0, 2022)
v2 = VehiculoAlquiler("Hyundai", "Tucson", "ALQ-002", 150.0)  # Año por defecto 2020

v1.mostrar_datos()
v2.mostrar_datos()

v2.actualizar_marca("Kia")
v2.actualizar_anio(2023)
print("Datos de v2 tras actualizar marca y año:")
v2.mostrar_datos()

print("----- 2. DOS INCREMENTOS CONSECUTIVOS DE TARIFA -----")
v1.aumentar_tarifa()     # Incremento por defecto del 10% -> 110.00
v1.aumentar_tarifa(20)   # Segundo incremento del 20% -> 132.00

print("----- 3. CÁLCULO DE DESCUENTOS CON DISTINTAS CANTIDADES DE DÍAS -----")
v1.calcular_descuento(1)  # Menos de 2 días -> 5% descuento
v2.calcular_descuento(4)  # De 2 a 5 días -> 10% descuento
v2.calcular_descuento(7)  # Más de 5 días -> 15% descuento

print("----- 4. INTENTO DE ASIGNAR TARIFA NEGATIVA -----")
print(f"Tarifa actual de {v2.codigo} antes del intento: S/. {v2.obtener_tarifa():.2f}")
v2.actualizar_tarifa(-50.0)
print(f"Tarifa actual de {v2.codigo} después del intento: S/. {v2.obtener_tarifa():.2f}")