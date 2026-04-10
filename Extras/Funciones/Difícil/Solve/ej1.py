import math

def obtener_distancia(x, y):
    # Fórmula: raíz cuadrada de (x^2 + y^2)
    return math.sqrt(x**2 + y**2)

def procesar_archivo(nombre_archivo):
    print(f"--- ANALIZANDO ARCHIVO: {nombre_archivo} ---")
    try:
        arch = open(nombre_archivo, "r", encoding="utf-8")
        for linea in arch:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                posX = float(partes[0])
                posY = float(partes[1])
                dist = obtener_distancia(posX, posY)
                print(f"Punto ({posX}, {posY}) -> Distancia al origen: {dist:.2f}")
        arch.close()
    except FileNotFoundError:
        print("Error: El archivo no existe.")

# Programa Principal
procesar_archivo("telemetria.txt")
