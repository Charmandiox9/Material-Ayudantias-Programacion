# Ejercicio 2
criticos = 0

arch = open("oxigeno.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

print("Verificando niveles de oxígeno...")
while linea != "":
    partes = linea.split(",")
    id_tanque = partes[0]
    carga = float(partes[1])
    
    if carga < 20.0:
        print(f"ALERTA: Tanque {id_tanque} bajo ({carga}%)")
        criticos += 1
    
    linea = arch.readline().strip()

arch.close()
print(f"Total tanques críticos encontrados: {criticos}")
