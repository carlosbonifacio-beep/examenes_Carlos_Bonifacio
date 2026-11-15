"""
Examen Final - Ejercicio 04: Control de inventario mediante diccionarios
"""

inventario = {
    "P001": {"nombre": "Laptop Lenovo", "precio": 3200.00, "cantidad": 5},
    "P002": {"nombre": "Mouse Inalámbrico", "precio": 85.00, "cantidad": 15},
    "P003": {"nombre": "Teclado Mecánico", "precio": 240.00, "cantidad": 8},
    "P004": {"nombre": "Monitor 24 pulgadas", "precio": 750.00, "cantidad": 4}
}

def mostrar_inventario(inv):
    print("----------------------------------------------------------------------------------------")
    print(f"{'CÓDIGO':<8} | {'PRODUCTO':<22} | {'PRECIO':<12} | {'STOCK':<8}")
    print("----------------------------------------------------------------------------------------")
    for codigo, datos in inv.items():
        print(f"{codigo:<8} | {datos['nombre']:<22} | S/. {datos['precio']:<8.2f} | {datos['cantidad']:<8}")
    print("----------------------------------------------------------------------------------------")

def registrar_compra(inv, codigo_producto, cantidad_solicitada):
    if codigo_producto not in inv:
        print(f"Error: El producto '{codigo_producto}' no existe en el inventario.\n")
        return False

    producto = inv[codigo_producto]
    if cantidad_solicitada <= 0:
        print("Error: La cantidad solicitada debe ser mayor a cero.\n")
        return False

    if cantidad_solicitada > producto["cantidad"]:
        print(f"Error: Stock insuficiente para '{producto['nombre']}'. Disponible: {producto['cantidad']}, Solicitado: {cantidad_solicitada}.\n")
        return False

    importe = producto["precio"] * cantidad_solicitada
    producto["cantidad"] -= cantidad_solicitada
    print(f"Compra exitosa: {cantidad_solicitada}x {producto['nombre']} | Importe total: S/. {importe:.2f}\n")
    return True

def valor_total_inventario(inv):
    return sum(datos["precio"] * datos["cantidad"] for datos in inv.values())

print("----- 1. INVENTARIO INICIAL -----")
mostrar_inventario(inventario)
print(f"Valor monetario inicial: S/. {valor_total_inventario(inventario):.2f}")

print("----- 2. OPERACIONES DE COMPRA -----")

registrar_compra(inventario, "P002", 4)

registrar_compra(inventario, "P999", 2)

registrar_compra(inventario, "P004", 10)

print("----- 3. INVENTARIO ACTUALIZADO Y VALOR TOTAL -----")
mostrar_inventario(inventario)
print(f"Valor monetario total actualizado: S/. {valor_total_inventario(inventario):.2f}")

