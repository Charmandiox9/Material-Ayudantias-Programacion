def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(valor):
    if valor < 18.5:
        return "Bajo peso"
    elif valor < 25:
        return "Normal"
    elif valor < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def generar_reporte():
    print("--- REPORTE NUTRICIONAL MEDISYSTEM ---")
    arch = open("pacientes.txt", "r", encoding="utf-8")
    for linea in arch:
        partes = linea.strip().split(",")
        nombre = partes[0]
        p = float(partes[1])
        a = float(partes[2])
        
        imc = calcular_imc(p, a)
        estado = clasificar_imc(imc)
        
        print(f"Paciente: {nombre:10} | IMC: {imc:.1f} | Estado: {estado}")
    arch.close()

# Programa Principal
generar_reporte()
