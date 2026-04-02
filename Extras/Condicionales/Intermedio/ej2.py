costo_base = 2
descuento = 0
horas_consumidas = int(input("Ingrese el número de horas consumidas este mes: "))

if horas_consumidas < 50:
  costo_total = costo_base
  descuento = 0
elif horas_consumidas >= 50 and horas_consumidas < 100:
  descuento = 0.1
else:
  descuento = 0.2

print(f"Horas: {horas_consumidas} | Descuento: {descuento*100}% | Total a pagar: ${costo_base * (1 - descuento)}")