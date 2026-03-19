
clp_a_usd = 920
clp_a_eur = 1070
usd_a_eur = 0.88
eur_a_usd = 1.14

print("Conversor de dinero")
print("1) CLP a USD")
print("2) CLP a EUR")
print("3) USD a CLP")
print("4) USD a EUR")
print("5) EUR a CLP")
print("6) EUR a USD")

opcion = int(input("Selecciona una opción: "))
monto = float(input("Ingresa el monto a convertir: "))

if opcion == 1:
    monto_convertido = monto / clp_a_usd
    moneda_origen = "CLP"
    moneda_destino = "USD"
elif opcion == 2:
    monto_convertido = monto / clp_a_eur
    moneda_origen = "CLP"
    moneda_destino = "EUR"
elif opcion == 3:
    monto_convertido = monto * clp_a_usd
    moneda_origen = "USD"
    moneda_destino = "CLP"
elif opcion == 4:
    monto_convertido = monto * usd_a_eur
    moneda_origen = "USD"
    moneda_destino = "EUR"
elif opcion == 5:
    monto_convertido = monto * clp_a_eur
    moneda_origen = "EUR"
    moneda_destino = "CLP"
else:
    monto_convertido = monto * eur_a_usd
    moneda_origen = "EUR"
    moneda_destino = "USD"

print("\n===CONVERSION REALIZADA===")
print(f"{monto} {moneda_origen} equivalen a {round(monto_convertido,2)} {moneda_destino}")

if moneda_destino == "USD" and monto_convertido < 5000:
    print("Puede que vayan con muy poca plata")
