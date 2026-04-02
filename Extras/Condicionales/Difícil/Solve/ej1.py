arch = open("ej1.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
  partes = linea.strip().split(",")
  lado_a = int(partes[0])
  lado_b = int(partes[1])
  lado_c = int(partes[2])

  if (lado_a + lado_b) < lado_c:
    print(f"Malla invalida.")

  else:
    tipo_poligono = ""
    if lado_a == lado_b and lado_b == lado_c:
      tipo_poligono = "Equilátero"
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
      tipo_poligono = "Isósceles"
    else:
      tipo_poligono = "Escaleno"
    print(f"Malla válida: Generando colisión para polígono {tipo_poligono}.")

  linea = arch.readline()