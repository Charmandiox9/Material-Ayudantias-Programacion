# Ejercicio 2
def libras_a_kilos(peso_lb):
    # 1 lb = 0.453592 kg, usaremos 0.453 por simplicidad según enunciado
    FACTOR = 0.453
    return peso_lb * FACTOR

# Programa Principal
lb = float(input("Ingrese peso en libras: "))
kg = libras_a_kilos(lb)

print(f"Peso equivalente: {kg:.2f} kg")
