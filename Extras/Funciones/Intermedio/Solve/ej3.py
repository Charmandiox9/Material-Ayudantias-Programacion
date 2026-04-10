# Ejercicio 3
def obtener_impuesto(pais):
    pais_limpio = pais.strip().capitalize()
    if pais_limpio == "China":
        return 0.05
    elif pais_limpio == "Usa":
        return 0.15
    else:
        return 0.20

def calcular_costo_total(precio_base, pais):
    porcentaje = obtener_impuesto(pais)
    monto_impuesto = precio_base * porcentaje
    return precio_base + monto_impuesto, monto_impuesto, porcentaje

# Programa Principal
precio = float(input("Precio del producto: "))
origen = input("País de origen: ")

total, imp_monto, imp_porc = calcular_costo_total(precio, origen)

print("\n--- DESGLOSE DE IMPORTACIÓN ---")
print(f"Precio Base: ${precio:.2f}")
print(f"Impuesto ({imp_porc*100:.0f}%): ${imp_monto:.2f}")
print(f"Total a Pagar: ${total:.2f}")
