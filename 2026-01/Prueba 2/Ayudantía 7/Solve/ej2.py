def cambio(lista,i,j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j]= aux
    return lista

def ordenar_hoja_ruta(codigos, clientes, productos, distancias):
    n = len(distancias)
    for i in range(n - 1):
        for j in range(i + 1,n):
            if distancias[i] > distancias[j]:
                cambio(distancias,i,j)
                cambio(codigos,i,j)
                cambio(clientes,i,j)
                cambio(productos,i,j)

def calcular_reporte(distancias):
    menor = distancias[0]
    mayor = distancias[0]
    
    indice_menor = 0
    indice_mayor = 0
    suma_total = 0
    
    for i in range(len(distancias)):
        valor_actual = distancias[i]
        suma_total += valor_actual
        
        if valor_actual < menor:
            menor = valor_actual
            indice_menor = i
            
        if valor_actual > mayor:
            mayor = valor_actual
            indice_mayor = i
            
    promedio = suma_total / len(distancias)
    promedio = round(promedio,2)
    
    return [indice_menor, indice_mayor, promedio]


archivo_paquetes = open("paquetes.txt", "r", encoding="utf-8")
linea_paquetes = archivo_paquetes.readline().strip()

codigos = []
clientes = []
productos = []
distancias = []

while linea_paquetes != '':
    datos_p = linea_paquetes.split(",")
    cod_p = datos_p[0]
    nombre = datos_p[1]
    producto = datos_p[2]
    
    archivo_rutas = open("rutas.txt", "r", encoding="utf-8")
    linea_rutas = archivo_rutas.readline().strip()
    
    distancia_encontrada = 0.0
    
    while linea_rutas != '':
        datos_r = linea_rutas.split(",")
        cod_r = datos_r[0]
        
        if cod_p == cod_r:
            distancia_encontrada = float(datos_r[2])
            break
        
        linea_rutas = archivo_rutas.readline().strip()
        
    codigos.append(cod_p)
    clientes.append(nombre)
    productos.append(producto)
    distancias.append(distancia_encontrada)
    
    linea_paquetes = archivo_paquetes.readline().strip()

ordenar_hoja_ruta(codigos, clientes, productos, distancias)

print()
print('============================')
print("HOJA DE RUTA EFICIENTE")
print('============================')
print(f"{'CÓDIGO':<10} | {'CLIENTE':<20} | {'DISTANCIA':<10}")
print('============================')

for i in range(len(distancias)):
    print(f"{codigos[i]:<10} | {clientes[i]:<20} | {distancias[i]:<10} KM")
print('============================')


indice_min = calcular_reporte(distancias)[0]
indice_max = calcular_reporte(distancias)[1]
promedio_dist = calcular_reporte(distancias)[2]

print()
print('============================')
print("REPORTE DE RENDIMIENTO PARA EL JEFE")
print('============================')
print(f"Domicilio mas cercano: {clientes[indice_min]} ({codigos[indice_min]}) a {distancias[indice_min]} KM")
print(f"Domicilio mas lejano:  {clientes[indice_max]} ({codigos[indice_max]}) a {distancias[indice_max]} KM")
print(f"Promedio de distancia por envio: {promedio_dist} KM")
print('============================')

print("MENSAJE AL CARTERO:")
print("¡Problema resulto cartero, ahora puedes entregarme mi procesador!")
print('============================')
