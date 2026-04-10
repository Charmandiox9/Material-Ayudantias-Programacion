# Ejercicio 1
def calcular_recarga(tiempo, tipo_estacion):
    estacion = tipo_estacion.capitalize()
    
    if estacion == "Solar":
        tasa = 5.0
    elif estacion == "Electrica":
        tasa = 15.0
    elif estacion == "Termica":
        tasa = 8.0
    else:
        tasa = 1.0
        
    return tiempo * tasa

# Programa Principal
minutos = float(input("Minutos en la estación: "))
tipo = input("Tipo de estación: ")

energia = calcular_recarga(minutos, tipo)
print(f"Energía recuperada: {energia} unidades.")
