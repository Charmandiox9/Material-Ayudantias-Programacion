# Ejercicio 1
total_poblacion = 0
cantidad = 0

arch = open("especies.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

print("--- ESPECIES EN ESTADO CRÍTICO ---")
while linea != "":
    partes = linea.split(",")
    nombre = partes[0]
    poblacion = int(partes[1])
    
    total_poblacion += poblacion
    cantidad += 1
    
    if poblacion < 500:
        print(f"- {nombre} ({poblacion} individuos)")
    
    linea = arch.readline().strip()

arch.close()

if cantidad > 0:
    promedio = total_poblacion / cantidad
    print("----------------------------------")
    print(f"Promedio de población general: {promedio:.1f}")
