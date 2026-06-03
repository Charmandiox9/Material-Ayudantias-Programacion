abecedario = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]

codigo = [6, 5, 12, 9, 3, 9, 4, 1, 4, 5, 19,0,22, 1, 19,0,2, 9, 5, 14,0,5, 14, 3, 1, 13, 9, 14, 1, 4, 15]

mensaje = ""

for i in range(len(codigo)):

    posicion = codigo[i]

    letra = abecedario[posicion]

    mensaje = mensaje + letra

mensaje = mensaje[0].upper() + mensaje[1:]

print(mensaje)