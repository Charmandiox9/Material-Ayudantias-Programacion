palabra_correcta = "python123"
intento = ""

while intento != palabra_correcta:
    intento = input("Palabra Secreta: ")
    if intento != palabra_correcta:
        print("Acceso Denegado.")

print("Acceso Concedido. Bienvenido al sistema.")
