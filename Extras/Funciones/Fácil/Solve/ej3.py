# Ejercicio 3
def mostrar_menu():
    print("--- PANEL DE CONTROL ---")
    print("1. Escanear sistema")
    print("2. Limpiar registros")
    print("3. Salir")
    print("------------------------")

def validar_opcion(opc):
    # Retorna True si está entre 1 y 3
    if opc == 1 or opc == 2 or opc == 3:
        return True
    return False

# Programa Principal
mostrar_menu()
seleccion = int(input("Seleccione una opción: "))

if validar_opcion(seleccion):
    print(f"Ejecutando opción {seleccion}...")
else:
    print("Opción inválida. Reintente.")
