"""
Examen Final - Ejercicio 03: Sistema de registro de pedidos de Rappi
"""
from datetime import datetime

def registrar_pedido(func):
    def wrapper(*args, **kwargs):
        inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{inicio}] Ejecutando '{func.__name__}'...")
        resultado = func(*args, **kwargs)
        fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{fin}] La función '{func.__name__}' finalizó correctamente.")
        return resultado
    return wrapper

def _validar_precios(precios):
    for precio in precios:
        if type(precio) not in (int, float) or precio <= 0:
            return False, precio
    return True, None

@registrar_pedido
def calcular_total(*args):
    es_valido, precio_invalido = _validar_precios(args)
    if not es_valido:
        print(f"Error: Precio inválido detectado ({precio_invalido}). Todos los precios deben ser numéricos y mayores que cero.")
        return None
    total = sum(args)
    print(f"Total calculado ({len(args)} precios): S/. {total:.2f}")
    return total

@registrar_pedido
def procesar_pedido(cliente, **kwargs):
    es_valido, precio_invalido = _validar_precios(kwargs.values())
    if not es_valido:
        print(f"Error en el pedido de {cliente}: Precio inválido ({precio_invalido}). No se realizó el cálculo.")
        return None
    total = sum(kwargs.values())
    print(f"Pedido de {cliente} procesado ({len(kwargs)} productos): S/. {total:.2f}")
    return total

print("----- 1. PRUEBAS DE calcular_total (*args) -----")
calcular_total(18.50, 24.00, 12.50)

calcular_total(10.0, 15.5, 8.0, 22.0, 14.5, 9.0)

print("----- 2. PRUEBAS DE procesar_pedido (**kwargs) -----")

procesar_pedido(
    "Carlos Bonifacio",
    hamburguesa=25.00,
    papas_fritas=9.50,
    gaseosa=6.00,
    helado=11.50
)

procesar_pedido(
    "Ana Torres",
    pizza=42.00,
    ensalada=-15.00,
    jugo=8.50
)

