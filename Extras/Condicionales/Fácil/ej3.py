temperatura = float(input("Temperatura actual (C°): "))

if temperatura > 45.0:
  print(f"Alerta: Estado en Peligro por alta temperatura ({temperatura}°C).")
else:
  print(f"Temperatura estable: {temperatura}°C.")