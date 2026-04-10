# Ejercicio 3
intentos_fallidos = 0

arch = open("access_log.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

print("--- ALERTA DE SEGURIDAD: INTENTOS FALLIDOS ---")
while linea != "":
    partes = linea.split(",")
    ip = partes[0]
    estado = partes[1]
    hora = partes[2]
    
    if estado == "FALLIDO":
        print(f"[{hora}] IP Sospechosa: {ip}")
        intentos_fallidos += 1
        
    linea = arch.readline().strip()

arch.close()
print("----------------------------------------------")
print(f"Total de intentos fallidos bloqueados: {intentos_fallidos}")
