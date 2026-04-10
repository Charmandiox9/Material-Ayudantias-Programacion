suma_temperaturas = 0.0
contador = 0

while True:
    temp = float(input("Ingrese temperatura (0 para finalizar): "))
    
    if temp == 0:
        break
    
    suma_temperaturas += temp
    contador += 1

if contador > 0:
    promedio = suma_temperaturas / contador
    print(f"\nLecturas realizadas: {contador}")
    print(f"Promedio de temperatura: {promedio:.2f}°C")
else:
    print("No se ingresaron lecturas.")
