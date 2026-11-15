"""
Módulo
"""

import random

def generar_lista(n):
    if type(n) is not int or n <= 0:
        raise ValueError("Error: La cantidad 'n' debe ser un número entero positivo mayor que cero.")
    return [random.randint(1, 100) for _ in range(n)]

def eliminar_duplicados(lista):
    sin_repetidos = []
    for num in lista:
        if num not in sin_repetidos:
            sin_repetidos.append(num)
    return sin_repetidos

def ordenar_listas(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente

def mayor_par(lista):
    pares = [num for num in lista if num % 2 == 0]
    if not pares:
        return "No existen números pares en la lista."
    return max(pares)

def obtener_elemento(lista, posicion):
    try:
        if type(posicion) is not int or posicion < 0:
            raise IndexError("No se admiten índices negativos o no enteros.")
        return lista[posicion]
    except IndexError:
        return f"Error: La posición {posicion} está fuera del rango de la lista."
