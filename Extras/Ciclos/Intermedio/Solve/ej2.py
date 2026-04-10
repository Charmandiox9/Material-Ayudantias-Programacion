stock = 10
print(f"Stock inicial: {stock} unidades.")

while stock > 0:
    accion = input("¿Qué desea hacer? (ENTREGAR/SALIR): ").upper()
    
    if accion == "SALIR":
        print(f"Cierre de turno. Stock final: {stock}")
        break
    elif accion == "ENTREGAR":
        stock -= 1
        print(f"Entregando... Stock restante: {stock}")
    else:
        print("Comando no reconocido.")

if stock == 0:
    print("Stock agotado. El sistema se cerrará.")
