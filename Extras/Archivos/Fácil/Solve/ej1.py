# Ejercicio 1
total_entradas = 0
total_sol = 0

arch = open("diario_marte.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
    total_entradas += 1
    # Contamos "SOL" en la línea (sin importar si es SOL 1 o solar)
    for palabra in linea.split(" "):
        if palabra.upper() == "SOL":
            total_sol += 1
    linea = arch.readline()

arch.close()

print("Leyendo diario marciano...")
print(f"Total de entradas registradas: {total_entradas}")
print(f"Menciones de la palabra 'SOL': {total_sol}")
print("Análisis de misión completado.")
