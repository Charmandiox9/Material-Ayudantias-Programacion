
id_paciente = int(input("Ingrese el ID del paciente: "))
edad_paciente = int(input("Ingrese la edad del paciente: "))

if edad_paciente < 13:
  print(f"Paciente {id_paciente} derivado a : Pediatría")
elif edad_paciente >= 13 and edad_paciente < 18:
  print(f"Paciente {id_paciente} derivado a : Medcina Adolescente")
elif edad_paciente >= 18 and edad_paciente < 65:
  print(f"Paciente {id_paciente} derivado a : Medicina General")
else:
  print(f"Paciente {id_paciente} derivado a : Geriatría")