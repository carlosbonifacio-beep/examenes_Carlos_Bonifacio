# Registro de participantes
participantes = []

participantes.append("Carlos")
participantes.append("Mario")
participantes.append("Jose")

# Nuevo participante
participantes.insert(1,"Daniela")

# nombre actualizado
participantes[0] = "Carlos Enrique"

# Eliminar participante
participantes.remove("Jose")

print("Lista final de participantes", participantes)
print("Cantidad de participantes registrados", len(participantes))
