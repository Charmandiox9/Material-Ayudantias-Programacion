total_pacientes = 0
criticos = 0
suma_gravedad = 0

while True:
    nombre = input("Nombre del paciente (o FIN): ")
    if nombre.upper() == "FIN":
        break
    
    # Validación de gravedad
    gravedad = 0
    while gravedad < 1 or gravedad > 5:
        gravedad = int(input("Gravedad (1-5): "))
        if gravedad < 1 or gravedad > 5:
            print("Error: La gravedad debe estar entre 1 y 5.")
    
    total_pacientes += 1
    suma_gravedad += gravedad
    if gravedad >= 4:
        criticos += 1

print("\n--- REPORTE FINAL ---")
if total_pacientes > 0:
    promedio = suma_gravedad / total_pacientes
    print(f"Total pacientes: {total_pacientes}")
    print(f"Casos Críticos: {criticos}")
    print(f"Promedio de gravedad: {promedio:.2f}")
else:
    print("No se registraron pacientes.")
