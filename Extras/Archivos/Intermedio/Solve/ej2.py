# Ejercicio 2
max_vel = -1
dron_rapido = ""

arch = open("vuelos.txt", "r", encoding="utf-8")
lineas = arch.readlines()

for linea in lineas:
    partes = linea.strip().split(",")
    id_dron = partes[0]
    distancia = float(partes[1])
    tiempo = float(partes[2])
    
    velocidad = distancia / tiempo
    print(f"{id_dron}: {velocidad:.2f} km/min")
    
    if velocidad > max_vel:
        max_vel = velocidad
        dron_rapido = id_dron

arch.close()
print(f"\nEl dron más rápido fue: {dron_rapido}")
