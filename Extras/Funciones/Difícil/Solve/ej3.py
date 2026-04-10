def es_ip_valida(ip):
    # Una validación simple: debe tener 3 puntos
    if ip.count(".") == 3:
        return True
    return False

def esta_bloqueada(ip, archivo_lista_negra):
    arch = open(archivo_lista_negra, "r", encoding="utf-8")
    encontrado = False
    for linea in arch:
        if linea.strip() == ip:
            encontrado = True
            break
    arch.close()
    return encontrado

# Programa Principal
ip_usuario = input("Ingrese dirección IP para conectar: ")

if es_ip_valida(ip_usuario):
    if esta_bloqueada(ip_usuario, "blacklist.txt"):
        print("[ACCESO DENEGADO] La IP se encuentra en la lista negra.")
    else:
        print("[ACCESO CONCEDIDO] Bienvenido al servidor.")
else:
    print("[ERROR] El formato de la IP no es válido.")
