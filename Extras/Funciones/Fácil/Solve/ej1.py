# Ejercicio 1
def calcular_danio(base, es_critico):
    if es_critico:
        return base * 2.0
    return base

# Programa Principal
b = float(input("Ataque base: "))
c_input = input("¿Fue crítico? (S/N): ").upper()

# Convertimos la entrada a booleano
critico = c_input == "S"

danio_final = calcular_danio(b, critico)
print(f"El daño total infligido es: {danio_final}")
