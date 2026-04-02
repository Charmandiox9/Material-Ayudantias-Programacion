arch = open("ej2.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
  partes = linea.strip().split(",")
  estado = partes[0]
  simbolo_leido = int(partes[1])

  if estado == "A":
    if simbolo_leido == 1:
      print("Transición: Escribiendo '0' en la cinta. Nuevo estado interno: B.")
    else:
      print("Se detiene la máquina.")
  elif estado == "B":
    if simbolo_leido == 1:
      print("Transición: Escribiendo '1' en la cinta. Nuevo estado interno: A.")
    else:
      print("Transición: Escribiendo '0' en la cinta. Nuevo estado interno: C.")
  else:
    print("La máquina se detiene incondicionalmente.")

  linea = arch.readline()