total = 0.0
meta = 1000.0

print(f"Meta: ${meta}")

while total < meta:
    deposito = float(input("Ingrese monto del depósito: "))
    total += deposito
    print(f"Saldo actual: ${total}")

print(f"¡Meta alcanzada! Saldo final: ${total}")
