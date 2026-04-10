# Ejercicio 1
max_co2 = -1
hora_max = ""
suma_co2 = 0
cantidad = 0

arch = open("calidad_aire.txt", "r", encoding="utf-8")
for linea in arch:
    partes = linea.strip().split(",")
    hora = partes[0]
    nivel = int(partes[1])
    
    suma_co2 += nivel
    cantidad += 1
    
    if nivel > max_co2:
        max_co2 = nivel
        hora_max = hora

arch.close()

if cantidad > 0:
    promedio = suma_co2 / cantidad
    print(f"Máximo CO2: {max_co2} ppm a las {hora_max}")
    print(f"Promedio diario: {promedio:.2f} ppm")
    
    if promedio > 400:
        print("ALERTA DE CONTAMINACIÓN: El nivel supera el umbral de seguridad.")
    else:
        print("Niveles dentro del rango aceptable.")
