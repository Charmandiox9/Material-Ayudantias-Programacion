def convertir_a_minutos(hora):
    partes = hora.split(":")
    horas = int(partes[0])
    minutos = int(partes[1])

    total = horas * 60 + minutos

    return total

def calcular_permanencia(entrada, salida):
    minutos_entrada = convertir_a_minutos(entrada)
    minutos_salida = convertir_a_minutos(salida)

    permanencia = minutos_salida - minutos_entrada

    if permanencia < 0:
        permanencia = permanencia + 24 * 60

    return permanencia

def calcular_cobro(tipo, minutos):
    cobro = 0

    if tipo == "emergencia":
        cobro = 0

    else:
        bloques = minutos // 30

        if minutos % 30 != 0:
            bloques = bloques + 1

        cobro = bloques * 1000

        if minutos > 180:
            cobro = cobro + 5000

        if tipo == "funcionario":
            cobro = int(cobro * 0.5)

    return cobro

def calcular_cobro_teorico_emergencia(minutos):
    bloques = minutos // 30

    if minutos % 30 != 0:
        bloques = bloques + 1

    cobro = bloques * 1000

    if minutos > 180:
        cobro = cobro + 5000

    return cobro

def obtener_momento(hora):
    minutos = convertir_a_minutos(hora)

    inicio_manana = convertir_a_minutos("07:01")
    fin_manana = convertir_a_minutos("12:00")

    inicio_tarde = convertir_a_minutos("12:01")
    fin_tarde = convertir_a_minutos("21:00")

    if minutos >= inicio_manana and minutos <= fin_manana:
        momento = "Mañana"

    elif minutos >= inicio_tarde and minutos <= fin_tarde:
        momento = "Tarde"

    else:
        momento = "Noche"

    return momento


def buscar_patente(patentes, patente_buscada):
    posicion = -1

    for i in range(len(patentes)):
        if patentes[i] == patente_buscada:
            posicion = i
            return posicion

    return posicion

def buscar_estado_pago(patentes_pago, estados_pago, patente):
    estado = "NO_APLICA"

    for i in range(len(patentes_pago)):
        if patentes_pago[i] == patente:
            estado = estados_pago[i]
            return estado

    return estado

def copiar_lista(lista_original):
    copia = []

    for i in range(len(lista_original)):
        copia.append(lista_original[i])

    return copia

def leer_estacionamiento(nombre_archivo):
    patentes = []
    tipos = []
    entradas = []
    salidas = []
    fechas = []
    minutos = []
    cobros = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    linea = archivo.readline().strip()

    while linea != "":
        partes = linea.split(";")

        patente = partes[0]
        tipo = partes[1]
        entrada = partes[2]
        salida = partes[3]
        fecha = partes[4]

        permanencia = calcular_permanencia(entrada, salida)
        cobro = calcular_cobro(tipo, permanencia)

        patentes.append(patente)
        tipos.append(tipo)
        entradas.append(entrada)
        salidas.append(salida)
        fechas.append(fecha)
        minutos.append(permanencia)
        cobros.append(cobro)

        linea = archivo.readline().strip()

    archivo.close()

    return patentes, tipos, entradas, salidas, fechas, minutos, cobros

def leer_pagos(nombre_archivo):
    patentes_pago = []
    estados_pago = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    linea = archivo.readline().strip()

    while linea != "":
        partes = linea.split(";")

        patente = partes[0]
        estado = partes[1]

        patentes_pago.append(patente)
        estados_pago.append(estado)

        linea = archivo.readline().strip()

    archivo.close()

    return patentes_pago, estados_pago

def ordenar_por_minutos(patentes, tipos, entradas, salidas, fechas, minutos, cobros):
    for i in range(len(minutos) - 1):
        for j in range(i + 1, len(minutos)):

            if minutos[j] > minutos[i]:

                aux = minutos[i]
                minutos[i] = minutos[j]
                minutos[j] = aux

                aux = patentes[i]
                patentes[i] = patentes[j]
                patentes[j] = aux

                aux = tipos[i]
                tipos[i] = tipos[j]
                tipos[j] = aux

                aux = entradas[i]
                entradas[i] = entradas[j]
                entradas[j] = aux

                aux = salidas[i]
                salidas[i] = salidas[j]
                salidas[j] = aux

                aux = fechas[i]
                fechas[i] = fechas[j]
                fechas[j] = aux

                aux = cobros[i]
                cobros[i] = cobros[j]
                cobros[j] = aux

def obtener_mes(fecha):
    partes = fecha.split("-")
    mes = int(partes[1])

    return mes

def ordenar_por_mes(patentes, tipos, entradas, salidas, fechas, minutos, cobros):
    for i in range(len(fechas) - 1):
        for j in range(i + 1, len(fechas)):

            mes_i = obtener_mes(fechas[i])
            mes_j = obtener_mes(fechas[j])

            if mes_j < mes_i:

                aux = fechas[i]
                fechas[i] = fechas[j]
                fechas[j] = aux

                aux = patentes[i]
                patentes[i] = patentes[j]
                patentes[j] = aux

                aux = tipos[i]
                tipos[i] = tipos[j]
                tipos[j] = aux

                aux = entradas[i]
                entradas[i] = entradas[j]
                entradas[j] = aux

                aux = salidas[i]
                salidas[i] = salidas[j]
                salidas[j] = aux

                aux = minutos[i]
                minutos[i] = minutos[j]
                minutos[j] = aux

                aux = cobros[i]
                cobros[i] = cobros[j]
                cobros[j] = aux

def mostrar_mayor_permanencia(patentes, tipos, entradas, salidas, fechas, minutos, cobros):
    patentes_copia = copiar_lista(patentes)
    tipos_copia = copiar_lista(tipos)
    entradas_copia = copiar_lista(entradas)
    salidas_copia = copiar_lista(salidas)
    fechas_copia = copiar_lista(fechas)
    minutos_copia = copiar_lista(minutos)
    cobros_copia = copiar_lista(cobros)

    ordenar_por_minutos(
        patentes_copia,
        tipos_copia,
        entradas_copia,
        salidas_copia,
        fechas_copia,
        minutos_copia,
        cobros_copia
    )

    print()
    print("5 vehículos con mayor tiempo de permanencia")

    limite = 5

    if len(patentes_copia) < 5:
        limite = len(patentes_copia)

    for i in range(limite):
        print("Patente:", patentes_copia[i],
              "- Tipo:", tipos_copia[i],
              "- Minutos:", minutos_copia[i],
              "- Cobro: $", cobros_copia[i])

def mostrar_estadisticas_por_tipo(tipos, minutos):
    suma_pacientes = 0
    cont_pacientes = 0
    pacientes_mayor_180 = 0

    suma_funcionarios = 0
    cont_funcionarios = 0
    funcionarios_mayor_180 = 0

    total_no_cobrado_emergencia = 0

    for i in range(len(tipos)):

        if tipos[i] == "paciente":
            suma_pacientes = suma_pacientes + minutos[i]
            cont_pacientes = cont_pacientes + 1

            if minutos[i] > 180:
                pacientes_mayor_180 = pacientes_mayor_180 + 1

        elif tipos[i] == "funcionario":
            suma_funcionarios = suma_funcionarios + minutos[i]
            cont_funcionarios = cont_funcionarios + 1

            if minutos[i] > 180:
                funcionarios_mayor_180 = funcionarios_mayor_180 + 1

        elif tipos[i] == "emergencia":
            total_no_cobrado_emergencia = total_no_cobrado_emergencia + calcular_cobro_teorico_emergencia(minutos[i])

    print()
    print("Promedios y porcentajes por tipo de vehículo")

    if cont_pacientes > 0:
        promedio_pacientes = suma_pacientes / cont_pacientes
        porcentaje_pacientes = pacientes_mayor_180 * 100 / cont_pacientes
        print("Promedio permanencia pacientes:", promedio_pacientes)
        print("Porcentaje pacientes con más de 180 minutos:", porcentaje_pacientes, "%")
    else:
        print("No hay pacientes registrados")

    if cont_funcionarios > 0:
        promedio_funcionarios = suma_funcionarios / cont_funcionarios
        porcentaje_funcionarios = funcionarios_mayor_180 * 100 / cont_funcionarios
        print("Promedio permanencia funcionarios:", promedio_funcionarios)
        print("Porcentaje funcionarios con más de 180 minutos:", porcentaje_funcionarios, "%")
    else:
        print("No hay funcionarios registrados")

    print("Total no cobrado por vehículos de emergencia: $", total_no_cobrado_emergencia)

def mostrar_ordenados_por_mes(patentes, tipos, entradas, salidas, fechas, minutos, cobros):
    patentes_copia = copiar_lista(patentes)
    tipos_copia = copiar_lista(tipos)
    entradas_copia = copiar_lista(entradas)
    salidas_copia = copiar_lista(salidas)
    fechas_copia = copiar_lista(fechas)
    minutos_copia = copiar_lista(minutos)
    cobros_copia = copiar_lista(cobros)

    ordenar_por_mes(
        patentes_copia,
        tipos_copia,
        entradas_copia,
        salidas_copia,
        fechas_copia,
        minutos_copia,
        cobros_copia
    )

    print()
    print("Registros ordenados por mes")

    for i in range(len(patentes_copia)):
        mes = obtener_mes(fechas_copia[i])

        print("Patente:", patentes_copia[i],
              "- Mes:", mes,
              "- Tipo:", tipos_copia[i],
              "- Cobro: $", cobros_copia[i])

def mostrar_busqueda_patente(patentes, tipos, entradas, salidas, fechas, minutos, cobros):
    patente_buscada = input("Ingrese patente a buscar: ").upper()

    posicion = buscar_patente(patentes, patente_buscada)

    print()

    if posicion == -1:
        print("Patente no encontrada")

    else:
        momento = obtener_momento(entradas[posicion])

        print("Patente encontrada")
        print("Posición dentro del archivo:", posicion + 1)
        print("Tipo de vehículo:", tipos[posicion])
        print("Minutos de permanencia:", minutos[posicion])
        print("Cobro asociado: $", cobros[posicion])
        print("Momento de entrada:", momento)

def mostrar_morosos(patentes, tipos, cobros, patentes_pago, estados_pago):
    total_pendiente = 0
    total_deberia_recaudarse = 0
    total_recaudado = 0

    mayor_deuda = -1
    patente_mayor_deuda = ""

    patentes_morosas = []

    for i in range(len(patentes)):

        if tipos[i] != "emergencia":
            estado = buscar_estado_pago(patentes_pago, estados_pago, patentes[i])

            total_deberia_recaudarse = total_deberia_recaudarse + cobros[i]

            if estado == "PAGADO":
                total_recaudado = total_recaudado + cobros[i]

            elif estado == "PENDIENTE":
                total_pendiente = total_pendiente + cobros[i]
                patentes_morosas.append(patentes[i])

                if cobros[i] > mayor_deuda:
                    mayor_deuda = cobros[i]
                    patente_mayor_deuda = patentes[i]

    print()
    print("Vehículos morosos")

    if len(patentes_morosas) == 0:
        print("No hay vehículos morosos")

    else:
        print("Patentes con pago pendiente:", patentes_morosas)
        print("Monto total pendiente: $", total_pendiente)

        if total_deberia_recaudarse > 0:
            porcentaje_recaudado = total_recaudado * 100 / total_deberia_recaudarse
            print("Porcentaje recaudado respecto al total:", porcentaje_recaudado, "%")

        print("Patente con mayor deuda:", patente_mayor_deuda)
        print("Mayor deuda: $", mayor_deuda)


def mostrar_resumen_final(patentes, tipos, cobros, patentes_pago, estados_pago):
    cantidad_total = len(patentes)
    cantidad_cobrables = 0
    recaudacion_efectiva = 0
    monto_pendiente = 0

    for i in range(len(patentes)):

        if tipos[i] != "emergencia":
            cantidad_cobrables = cantidad_cobrables + 1

            estado = buscar_estado_pago(patentes_pago, estados_pago, patentes[i])

            if estado == "PAGADO":
                recaudacion_efectiva = recaudacion_efectiva + cobros[i]

            elif estado == "PENDIENTE":
                monto_pendiente = monto_pendiente + cobros[i]

    print()
    print("Resumen final")
    print("Cantidad total de vehículos:", cantidad_total)
    print("Cantidad de vehículos cobrables:", cantidad_cobrables)
    print("Recaudación efectiva: $", recaudacion_efectiva)
    print("Monto pendiente: $", monto_pendiente)


# ------------------------------------------------------------
# Muestra el menú principal.
# ------------------------------------------------------------
def mostrar_menu():
    print()
    print("MENÚ - Control de estacionamiento")
    print("1. Mostrar los 5 vehículos con mayor tiempo de permanencia")
    print("2. Mostrar promedios y porcentajes por tipo de vehículo")
    print("3. Ordenar registros por mes")
    print("4. Buscar una patente")
    print("5. Mostrar morosos")
    print("6. Cerrar programa")

def main():
    patentes, tipos, entradas, salidas, fechas, minutos, cobros = leer_estacionamiento("estacionamiento.txt")
    patentes_pago, estados_pago = leer_pagos("pagos.txt")

    print("Sistema de control de estacionamiento - Centro Médico San Byte")

    opcion = ""

    while opcion != "6":
        mostrar_menu()

        opcion = input("Ingrese una opción: ")

        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
            print("Opción inválida")
            opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_mayor_permanencia(
                patentes,
                tipos,
                entradas,
                salidas,
                fechas,
                minutos,
                cobros
            )

        elif opcion == "2":
            mostrar_estadisticas_por_tipo(
                tipos,
                minutos
            )

        elif opcion == "3":
            mostrar_ordenados_por_mes(
                patentes,
                tipos,
                entradas,
                salidas,
                fechas,
                minutos,
                cobros
            )

        elif opcion == "4":
            mostrar_busqueda_patente(
                patentes,
                tipos,
                entradas,
                salidas,
                fechas,
                minutos,
                cobros
            )

        elif opcion == "5":
            mostrar_morosos(
                patentes,
                tipos,
                cobros,
                patentes_pago,
                estados_pago
            )

        elif opcion == "6":
            mostrar_resumen_final(
                patentes,
                tipos,
                cobros,
                patentes_pago,
                estados_pago
            )

            print("Sistema finalizado")


main()