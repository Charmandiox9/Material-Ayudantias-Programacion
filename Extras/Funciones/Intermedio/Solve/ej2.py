# Ejercicio 2
def clasificar_pulso(latidos):
    if latidos < 60:
        return "Bradicardia"
    elif latidos <= 100:
        return "Normal"
    else:
        return "Taquicardia"

def mostrar_alerta(nombre, estado):
    if estado != "Normal":
        print(f"\n[ALERTA] El paciente {nombre} presenta: {estado}")
    else:
        print(f"\nEl paciente {nombre} tiene un pulso Normal.")

# Programa Principal
paciente = input("Nombre del paciente: ")
pulso = int(input("Pulso (latidos/min): "))

resultado = clasificar_pulso(pulso)
mostrar_alerta(paciente, resultado)
