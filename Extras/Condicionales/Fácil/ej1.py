numero_combo = int(input("Ingrese el numero de combo: "))

if numero_combo % 2 == 0:
  print(f"El combo {numero_combo} genera un Ataque Crítico.")
else:
  print(f"El combo {numero_combo} genera un Ataque Normal.")