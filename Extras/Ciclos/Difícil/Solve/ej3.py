monto = float(input("Monto inicial: "))
anos = int(input("Años a proyectar: "))
print()

for i in range(1, anos + 1):
    monto = monto * 1.05 # Interés del 5%
    
    mensaje_extra = ""
    if i % 2 == 0:
        monto = monto * 1.02 # Bono del 2%
        mensaje_extra = " (¡Bono par aplicado!)"
    
    print(f"Año {i}: ${monto:.2f}{mensaje_extra}")
