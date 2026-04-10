cantidad = int(input("Cantidad de paquetes: "))

print("Iniciando transmisión...")
for i in range(1, cantidad + 1):
    print(f"Enviando paquete #{i}")
print("Transmisión completada.")
