"""
Examen Final - Ejercicio 02: Ejecución del módulo operaciones.py
"""

from operaciones import (
    generar_lista,
    eliminar_duplicados,
    ordenar_listas,
    mayor_par,
    obtener_elemento
)

for ejecucion, cantidad in enumerate([8, 12], start=1):
    print(f"----- EJECUCIÓN {ejecucion} (n = {cantidad}) -----")
    lista_orig = generar_lista(cantidad)
    lista_unica = eliminar_duplicados(lista_orig)
    asc, desc = ordenar_listas(lista_orig)
    par_max = mayor_par(lista_orig)

    print(f"Lista original:      {lista_orig}")
    print(f"Sin duplicados:      {lista_unica}")
    print(f"Orden ascendente:    {asc}")
    print(f"Orden descendente:   {desc}")
    print(f"Mayor número par:    {par_max}")

print("----- PRUEBAS DE POSICIONES Y CANTIDAD INVÁLIDA -----")
lista_prueba = generar_lista(5)
print(f"Lista de prueba: {lista_prueba}")

print(f"Posición válida (índice 2): {obtener_elemento(lista_prueba, 2)}")

print(f"Posición inválida (índice 15): {obtener_elemento(lista_prueba, 15)}")

try:
    generar_lista(-4)
except ValueError as e:
    print(f"Prueba con n = -4 -> {e}")
