print("Bienvenido forastero, ¿Qué quieres hacer?")
print("1) Comprar Suministros")
print("2) Salir")
opcion = int(input("Ingrese una opcion: "))
print()

if opcion == 1:
    monto_disponible = float(input("Ingresa el monto disponible: "))
    gasto = float(input("Ingresa el monto que deseas gastar: "))

    if gasto > monto_disponible:
        print("No tienes dinero suficiente")

    if gasto <= 20000:
        descuento = 0
    elif gasto <= 50000:
        descuento = 0.05
    elif gasto <= 100000:
        descuento = 0.10
    else:
        descuento = 0.15

    gasto_descuento = gasto - (gasto * descuento)

    if gasto % 2 == 0:
        gasto_descuento = gasto_descuento - (gasto_descuento * 0.03)
        print("El mercader del refugio te dio un descuento extra del 3%")

    dinero_restante = monto_disponible - gasto_descuento

    print("\n===RESUMEN DE LA COMPRA===")
    print(f"Monto inicial: {monto_disponible}")
    print(f"Gasto original: {gasto}")
    print(f"Gasto con descuento: {gasto_descuento}")
    print(f"Dinero restante: {dinero_restante}")
elif opcion == 2:
    print("Buena suerte sobreviviendo")