# 1.Solicitud de valores numericos
def pedir_dos_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer valor numérico: "))
            num2 = float(input("Ingrese el segundo valor numérico: "))
        except ValueError:
            print("Error: Debe ingresar únicamente valores numéricos. Intente nuevamente.\n")
        else:
            print("Números ingresados correctamente.")
            return num1, num2


# 2. Sumar dos valores
def sumar(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: No se pueden sumar tipos incompatibles.")
        return None


# 3. Función para dividir dos valores (incluye else y finally)
def dividir(a, b):
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        print("Error: Operación entre tipos de datos incompatibles.")
    else:
        print(f"Operación de división realizada con éxito.")
    finally:
        print("----- Finalizó el intento de división -----")
    return resultado


# 4. Lista de N elementos ingresados por consola
def registrar_lista():
    while True:
        try:
            n = int(input("¿Cuántos elementos desea registrar en la lista? (N): "))
            if n <= 0:
                print("Debe registrar al menos 1 elemento.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad N.\n")

    lista = []
    i = 0
    while i < n:
        try:
            val = float(input(f"Ingrese el elemento [{i + 1} de {n}]: "))
            lista.append(val)
            i += 1
        except ValueError:
            print("Error: El elemento debe ser un valor numérico. Intente este elemento de nuevo.")

    return lista


# 5. Consultar un elemento por índice
def consultar_indice(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        print(f"Error: El índice {indice} no existe en la lista (fuera de rango).")
        return None
    except TypeError:
        print("Error: El índice ingresado debe ser un número entero.")
        return None

print("------ PRUEBA 1: Operaciones con datos válidos ------")
val1, val2 = pedir_dos_numeros()
print(f"Suma: {val1} + {val2} = {sumar(val1, val2)}")
print(f"División: {val1} / {val2} = {dividir(val1, val2)}")

mi_lista = registrar_lista()
print(f"Lista creada: {mi_lista}")

# Consulta con un índice válido
posicion = int(input("Ingrese el índice a consultar en la lista: "))
res_elem = consultar_indice(mi_lista, posicion)
if res_elem is not None:
    print(f"El elemento en la posición {posicion} es: {res_elem}")

print("--------------------------------------------------------------")

print("----- PRUEBA 2: Error de división entre cero -----")
print(f"Resultado división entre cero (10 / 0): {dividir(10, 0)}")

print("--------------------------------------------------------------")

print("----- PRUEBA 3: Error de consulta a posición inexistente -----")
lista_demo = [10.0, 20.0, 30.0]
print(f"Lista de prueba: {lista_demo}")
consultar_indice(lista_demo, 99)

