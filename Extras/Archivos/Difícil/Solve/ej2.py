# Ejercicio 2
busqueda = input("Ingrese artista a buscar: ").strip().lower()

total_segundos = 0
max_popularidad = -1
cancion_top = ""
encontrado = False

arch = open("catalogo.txt", "r", encoding="utf-8")

print(f"\nCanciones encontradas de '{busqueda}':")
for linea in arch:
    partes = linea.strip().split(";")
    artista = partes[0]
    cancion = partes[1]
    segundos = int(partes[2])
    popularidad = int(partes[3])
    
    if artista.lower() == busqueda:
        encontrado = True
        print(f"- {cancion} ({segundos} seg)")
        total_segundos += segundos
        
        if popularidad > max_popularidad:
            max_popularidad = popularidad
            cancion_top = cancion

arch.close()

if encontrado:
    minutos = total_segundos // 60
    restante_seg = total_segundos % 60
    print(f"\nDuración total: {minutos} min {restante_seg} seg")
    print(f"Canción recomendada (más popular): {cancion_top}")
else:
    print("No se encontraron registros de ese artista.")
