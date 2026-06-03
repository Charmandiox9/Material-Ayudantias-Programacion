archivo = open("bodega.txt", "r", encoding="utf-8")
linea = archivo.readline().strip()

componentes = []
cantidades = []

while linea != '':
    datos = linea.split(",")
    articulo = (datos[0]).lower()
    cantidad = int(datos[1])
    
    componentes.append(articulo)
    cantidades.append(cantidad)
    
    linea = archivo.readline().strip()

print("=== INICIANDO SISTEMA DE OPTIMIZACION DE BODEGA ===")
buscado = (input("Ingrese el articulo a consultar: ")).lower()

while buscado != '':
    encontrado = False
    
    for i in range(len(componentes)):
        if componentes[i] == buscado:
            encontrado = True
            print()
            print(f"Articulo encontrado: {componentes[i]}")
            print(f"Cantidad disponible: {cantidades[i]} unidades")
            
            if cantidades[i] < 5:
                print("ALERTA: ¡Stock critico en bodega! Se necesitan reponer unidades")
            break
    
    if not encontrado:
        print()
        print("El componente no existe en los registros de la bodega")
    
    print()
    buscado = input("Ingrese el articulo a consultar: ")

print("=== CERRANDO SISTEMA DE OPTIMIZACION DE BODEGA ===")