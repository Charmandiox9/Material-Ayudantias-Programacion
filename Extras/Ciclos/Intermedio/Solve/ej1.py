cantidad = int(input("Total de contenedores: "))

for i in range(1, cantidad + 1):
    if i % 2 == 0:
        print(f"Contenedor #{i}: RECOGIDO")
    else:
        print(f"Contenedor #{i}: Ignorado")

print("Escaneo finalizado.")
