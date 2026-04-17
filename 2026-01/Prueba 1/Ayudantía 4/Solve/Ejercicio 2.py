def leerArchivo(archivo):
    arch = open(archivo, "r", encoding = "utf-8")
    return arch

def calcularPromedio(suma, contador):
    return (suma/contador)

def imprimirPromedio(categoria, promedio):
    print(f"Promedio de tiempo de dificultad {categoria}: {promedio} segundos")


nombre_archivo = input("Ingrese el nombre del archivo: ")
arch = leerArchivo(nombre_archivo)
linea = arch.readline().strip()

menorTiempo = 99999
jugadorMenorTiempo = ""

contFacil = 0
contIntermedio = 0
contDificil = 0
sumaTiempoFacil = 0
sumaTiempoIntermedio = 0
sumaTiempoDificil = 0

pistasLaboratorio = 0

print()
print("1) Jugadores que no lograron salir del Escape Room:")
while linea != "":
    partes = linea.split(",")
    pieza = partes[0]
    dificultad = partes[1]
    jugador = partes[2]
    edad = int(partes[3])
    pistas = int(partes[4])
    puzzles = int(partes[5])
    tiempo_salida = int(partes[6])
    
    
    if tiempo_salida == -1:
        print(f"- {jugador} ({edad})")
    
    elif tiempo_salida < menorTiempo:
        menorTiempo = tiempo_salida
        jugadorMenorTiempo = jugador
    
    elif dificultad == "facil":
        contFacil += 1
        sumaTiempoFacil += tiempo_salida
    elif dificultad == "intermedio":
        contIntermedio += 1
        sumaTiempoIntermedio += tiempo_salida
    elif dificultad == "dificil":
        contDificil += 1
        sumaTiempoDificil += tiempo_salida
    
    if pieza == "Laboratorio X":
        pistasLaboratorio += pistas
    
    
    linea = arch.readline().strip()

print()
print(f"2) {jugadorMenorTiempo} fue el/la jugador/a más rápido/a, demorando {menorTiempo} segundos.")

print()
print("3) Promedios:")
promedioFacil = round(calcularPromedio(sumaTiempoFacil, contFacil))
promedioIntermedio = round(calcularPromedio(sumaTiempoIntermedio, contIntermedio))
promedioDificil = round(calcularPromedio(sumaTiempoDificil, contDificil))
s
imprimirPromedio("Facil", promedioFacil)
imprimirPromedio("Intermedio", promedioIntermedio)
imprimirPromedio("Dificil", promedioDificil)

print()
print(f"4) Pistas utilizadas en Laboratorio X: {pistasLaboratorio}")