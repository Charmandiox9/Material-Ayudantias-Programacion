print("Calculadora de viaje")
cant_millas = int(input("Ingrese la cantidad de millas: "))
cant_km = round(cant_millas * 1.61, 2)

velocidad_mph = int(input("Velocidad a la que irán (mph): "))
velocidad_kmh = round(velocidad_mph * 1.609, 2)

print()

if velocidad_kmh > 140:
    print(f"Rick conduciendo a {velocidad_kmh} km/h está superando el límite permitido en carretera")
    print()

tiempo_h = round(cant_km / velocidad_kmh, 2)
tiempo_m = round(tiempo_h * 60, 2)

print("===RESULTADOS OBTENIDOS===")
print(f"{cant_millas} millas equivalen a {cant_km} kilómetros")
print(f"{velocidad_mph} mph equivalen a {velocidad_kmh} km/h")
print(f"Con los datos ingresados el viaje tardará aproximadamente {tiempo_h} horas lo que tambien equivale a {tiempo_m} minutos")
