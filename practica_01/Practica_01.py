# Calificaciones
nota_matematica = 17
nota_ciencia = 14
nota_historia = 15

peso_matematica = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

# Nota final ponderada
nota_final = (nota_matematica * peso_matematica) + (nota_ciencia * peso_ciencia) + (nota_historia * peso_historia)

#Nota
print(f"La nota final es: {nota_final:.1f}")

# Aprueba con mas o igual a 13
aprobado = nota_final >= 13.0
print(f"¿Aprobado?: {aprobado}")
Estado_Str = "Aprobado" if aprobado else "Desaprobado"
Final = f"El estudiante tuvo una nota final de {nota_final:.1f} y su estado final es: {Estado_Str}"
print(Final)

print("-----------------------------------------------------")








