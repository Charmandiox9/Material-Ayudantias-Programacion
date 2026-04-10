# Ejercicio 3
total = 0
negativos = 0

arch = open("comentarios.txt", "r", encoding="utf-8")

print("Analizando comentarios...")
for linea in arch:
    comentario = linea.strip()
    if comentario == "":
        continue
        
    total += 1
    # Convertimos a minúsculas para buscar palabras clave
    texto_min = comentario.lower()
    
    es_negativo = False
    for palabra in texto_min.split(" "):
        if palabra == "error" or palabra == "malo" or palabra == "lento" or palabra == "mal":
            es_negativo = True
            negativos += 1
            break
    
    status = "[Negativo]" if es_negativo else "[Positivo]"
    print(f"{status} {comentario}")

arch.close()

if total > 0:
    porcentaje = (negativos / total) * 100
    print("\n--- RESULTADOS ---")
    print(f"Total comentarios: {total}")
    print(f"Comentarios Negativos: {negativos}")
    print(f"Índice de insatisfacción: {porcentaje:.1f}%")
