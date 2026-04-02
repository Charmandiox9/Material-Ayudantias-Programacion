arch = open("ej2.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
  partes = linea.strip().split(",")
  cobertura = int(partes[0])
  tests_fallidos = int(partes[1])
  is_hotfix = int(partes[2])

  if (cobertura > 80 and tests_fallidos == 0) or (is_hotfix == 1 and tests_fallidos == 0):
      print("Despliegue Aprobado: Parche de emergencia detectado sin errores en los tests.")
  else:
      print("Despliegue Rechazado: No se cumplen los criterios de cobertura o hay tests fallidos.")
  linea = arch.readline()