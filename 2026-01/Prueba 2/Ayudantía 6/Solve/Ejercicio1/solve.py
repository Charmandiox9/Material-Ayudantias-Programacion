def es_codigo_valido(grupo, codigo):
    valido = 0

    if grupo == "analgesico":
        if codigo >= 100 and codigo <= 199:
            valido = 1

    elif grupo == "antibiotico":
        if codigo >= 200 and codigo <= 299:
            valido = 1

    elif grupo == "vitamina":
        if codigo >= 300 and codigo <= 399:
            valido = 1

    return valido

def obtener_grupo(codigo):
    grupo = "invalido"

    if codigo >= 100 and codigo <= 199:
        grupo = "analgesico"

    elif codigo >= 200 and codigo <= 299:
        grupo = "antibiotico"

    elif codigo >= 300 and codigo <= 399:
        grupo = "vitamina"

    return grupo

def buscar_codigo(lista, codigo):
    posicion = -1

    for i in range(len(lista)):
        if lista[i] == codigo:
            posicion = i
            return posicion

    return posicion

def retirar_codigo(lista, codigo):
    retirado = 0

    posicion = buscar_codigo(lista, codigo)

    if posicion != -1:
        lista.pop(posicion)
        retirado = 1

    return retirado

def leer_inventario(nombre_archivo):
    analgesicos = []
    antibioticos = []
    vitaminas = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    grupo_actual = ""

    linea = archivo.readline().strip()

    while linea != "":
        partes = linea.split(",")

        if len(partes) == 3:
            grupo_actual = partes[0]

        else:
            codigo = int(linea)

            if es_codigo_valido(grupo_actual, codigo) == 1:

                if grupo_actual == "analgesico":
                    analgesicos.append(codigo)

                elif grupo_actual == "antibiotico":
                    antibioticos.append(codigo)

                elif grupo_actual == "vitamina":
                    vitaminas.append(codigo)

        linea = archivo.readline().strip()

    archivo.close()

    return analgesicos, antibioticos, vitaminas

def leer_receta(nombre_archivo):
    receta = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    linea = archivo.readline().strip()

    while linea != "":
        codigo = int(linea)
        receta.append(codigo)

        linea = archivo.readline().strip()

    archivo.close()

    return receta

def receta_valida(nombre_receta):
    valida = 0

    if nombre_receta == "receta_1":
        valida = 1

    elif nombre_receta == "receta_2":
        valida = 1

    elif nombre_receta == "receta_3":
        valida = 1

    return valida


def obtener_archivo_receta(nombre_receta):
    archivo = ""

    if nombre_receta == "receta_1":
        archivo = "receta_1.txt"

    elif nombre_receta == "receta_2":
        archivo = "receta_2.txt"

    elif nombre_receta == "receta_3":
        archivo = "receta_3.txt"

    return archivo

def revisar_receta(receta, analgesicos, antibioticos, vitaminas):
    entregados = []
    no_disponibles = []
    invalidos = []

    for i in range(len(receta)):
        codigo = receta[i]
        grupo = obtener_grupo(codigo)

        if grupo == "invalido":
            invalidos.append(codigo)

        elif grupo == "analgesico":
            retirado = retirar_codigo(analgesicos, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

        elif grupo == "antibiotico":
            retirado = retirar_codigo(antibioticos, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

        elif grupo == "vitamina":
            retirado = retirar_codigo(vitaminas, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

    return entregados, no_disponibles, invalidos

def determinar_grupo_mas_entregado(entregados):
    cont_analgesico = 0
    cont_antibiotico = 0
    cont_vitamina = 0

    for i in range(len(entregados)):
        codigo = entregados[i]
        grupo = obtener_grupo(codigo)

        if grupo == "analgesico":
            cont_analgesico = cont_analgesico + 1

        elif grupo == "antibiotico":
            cont_antibiotico = cont_antibiotico + 1

        elif grupo == "vitamina":
            cont_vitamina = cont_vitamina + 1

    mayor = cont_analgesico
    grupo_mayor = "analgesico"
    empate = 0

    if cont_antibiotico > mayor:
        mayor = cont_antibiotico
        grupo_mayor = "antibiotico"
        empate = 0

    elif cont_antibiotico == mayor and mayor > 0:
        empate = 1

    if cont_vitamina > mayor:
        mayor = cont_vitamina
        grupo_mayor = "vitamina"
        empate = 0

    elif cont_vitamina == mayor and mayor > 0:
        empate = 1

    if mayor == 0:
        grupo_mayor = "ninguno"

    elif empate == 1:
        grupo_mayor = "empate"

    return grupo_mayor

def mostrar_resultado(receta, entregados, no_disponibles, invalidos):
    medicamentos_solicitados = len(receta)
    codigos_validos = len(receta) - len(invalidos)
    medicamentos_entregados = len(entregados)
    medicamentos_no_disponibles = len(no_disponibles)
    codigos_invalidos = len(invalidos)

    grupo_mas_entregado = determinar_grupo_mas_entregado(entregados)

    print()
    print("Medicamentos solicitados:", medicamentos_solicitados)
    print("Códigos válidos solicitados:", codigos_validos)
    print("Medicamentos entregados:", medicamentos_entregados)
    print("Medicamentos no disponibles:", medicamentos_no_disponibles)
    print("Códigos inválidos:", codigos_invalidos)

    print()
    print("Lista de entregados:", entregados)
    print("Lista de no disponibles:", no_disponibles)
    print("Lista de inválidos:", invalidos)

    print()
    print("Grupo más entregado:", grupo_mas_entregado)

    if medicamentos_no_disponibles == 0:
        print("Estado: Receta completa")
    else:
        print("Estado: Receta incompleta")

def preguntar_continuar():
    opcion = input("¿Desea revisar otra receta? (Si - No): ").lower()

    while opcion != "si" and opcion != "no":
        print("Opción inválida")
        opcion = input("¿Desea revisar otra receta? (Si - No): ").lower()

    return opcion

def main():
    analgesicos, antibioticos, vitaminas = leer_inventario("inventario.txt")

    print("Bienvenido al sistema de Farmacia Turno de Invierno")
    print()

    continuar = "si"
    

    while continuar == "si":
        nombre_receta = input("Ingrese receta a revisar: ").lower()

        while receta_valida(nombre_receta) == 0:
            print("Opción inválida")
            print()
            nombre_receta = input("Ingrese receta a revisar: ").lower()

        archivo_receta = obtener_archivo_receta(nombre_receta)

        receta = leer_receta(archivo_receta)

        entregados, no_disponibles, invalidos = revisar_receta(
            receta,
            analgesicos,
            antibioticos,
            vitaminas
        )

        mostrar_resultado(
            receta,
            entregados,
            no_disponibles,
            invalidos
        )
        
        print()
        
        continuar = preguntar_continuar()
        
        print()

    print("Sistema finalizado")


main()