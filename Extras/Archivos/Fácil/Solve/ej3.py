# Ejercicio 3
arch = open("senales.txt", "r", encoding="utf-8")

print("--- MENSAJES DECODIFICADOS ---")
for linea in arch.readlines():
    texto = linea.strip()
    # Filtramos líneas de ruido (.....) o vacías
    if texto != "" and texto != "....." and texto != "......":
        print(texto)

arch.close()
print("------------------------------")
