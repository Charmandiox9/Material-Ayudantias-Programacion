arch = open("problema1.txt", "r", encoding="utf-8")
linea =  arch.readline().strip()

total_ventas = 0
sucursal_mas_ventas = ""
mas_ventas = -1

prod_mas_caro = ""
mas_caro = -1
sucursal_prod_mas_caro = ""

while linea != "":
    cant_sucursales = int(linea)
    linea =  arch.readline().strip()
    for sucursal in range(cant_sucursales):
        partes = linea.split(",")
        sucursal = partes[0]
        cant_productos = int(partes[1])
        prod_mayor_venta = ""
        mayor_venta = -1
        cant_ventas_unitarias = 0
        total = 0
        linea =  arch.readline().strip()
        for producto in range(cant_productos):
            partes = linea.split(",")
            producto = partes[0]
            cantidad_vendida = int(partes[1])
            precio_unitario = int(partes[2])
            total += cantidad_vendida * precio_unitario
            total_ventas += cantidad_vendida * precio_unitario
            if cantidad_vendida * precio_unitario > mayor_venta:
                mayor_venta = cantidad_vendida * precio_unitario
                prod_mayor_venta = producto
            if cantidad_vendida == 1:
                cant_ventas_unitarias += 1
                
            if precio_unitario > mas_caro:
                mas_caro = precio_unitario
                prod_mas_caro = producto
                sucursal_prod_mas_caro = sucursal
                
            linea =  arch.readline().strip()
        
        if total > mas_ventas:
            mas_ventas = total
            sucursal_mas_ventas = sucursal
            
        
        porcentaje = (cant_ventas_unitarias/cant_productos) * 100
        print(f"Producto con mayor venta en sucursal {sucursal}")
        print(f"es {prod_mayor_venta} con total {mayor_venta}")
        print(f"porcentaje de ventas unitarias es {porcentaje:.2f}% \n")
    
    print(f"Total de ventas {total_ventas}")
    print(f"La sucursal con mas ventas es {sucursal_mas_ventas}")
    print(f"con total de ventas {mas_ventas}")
    print(f"El producto mas caro fue {prod_mas_caro}")
    print(f"vendido en la sucursal {sucursal_prod_mas_caro}")
    print(f"con un precio de {mas_caro}")