posicion_actual = int(input("Posición actual: "))
comando = input("Comando a ejecutar: ").upper()

nueva_posicion = posicion_actual

if comando == "SIGUIENTE":
  nueva_posicion += 1
elif comando == "ANTERIOR":
  if nueva_posicion - 1 < 0:
    nueva_posicion = 0
    print("No se puede ir a una posición menor a 0, se mantiene en la posición actual.")
  else:
    nueva_posicion -= 1
elif comando == "INICIO":
  nueva_posicion = 0
elif comando == "FIN":
  nueva_posicion = 99

print(f"Comando {comando} ejecutado. Nueva posición: {nueva_posicion}")