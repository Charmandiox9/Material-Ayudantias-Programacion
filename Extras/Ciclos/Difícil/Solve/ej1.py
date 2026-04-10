tamano = int(input("Tamaño de la grilla: "))
pos_x = int(input("Tu posición X: "))
pos_y = int(input("Tu posición Y: "))
print()

for y in range(tamano):
    for x in range(tamano):
        if x == pos_x and y == pos_y:
            print("[X]", end="   ")
        else:
            print(f"({x},{y})", end=" ")
    print() # Salto de línea al terminar una fila
