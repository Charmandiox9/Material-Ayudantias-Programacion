# 04 · Listas

Colecciones ordenadas y mutables de elementos en Python.

---

## 1. ¿Qué es una lista?

Una lista almacena **múltiples valores en una sola variable**, en un orden definido. Puede contener elementos de distintos tipos.

```python
notas     = [6.5, 4.0, 5.2, 3.8]
nombres   = ["Ana", "Bob", "Carlos"]
mixta     = [1, "hola", True, 3.14]
vacia     = []
```

---

## 2. Acceder a elementos (indexación)

Los índices comienzan en **0**. Los índices negativos cuentan desde el final.

```python
frutas = ["manzana", "pera", "uva", "kiwi"]

print(frutas[0])    # "manzana"
print(frutas[2])    # "uva"
print(frutas[-1])   # "kiwi"   (último elemento)
print(frutas[-2])   # "uva"    (penúltimo)
```

---

## 3. Modificar elementos

Las listas son **mutables**: puedes cambiar, agregar o eliminar elementos.

```python
notas = [6.5, 4.0, 5.2]
notas[1] = 4.5          # modifica el índice 1
print(notas)            # [6.5, 4.5, 5.2]
```

---

## 4. Métodos principales

```python
lista = [3, 1, 4, 1, 5]

lista.append(9)          # agrega al final           → [3,1,4,1,5,9]
lista.insert(0, 0)       # inserta en posición 0     → [0,3,1,4,1,5,9]
lista.remove(1)          # elimina la primera ocurrencia de 1
lista.pop()              # elimina y retorna el último elemento
lista.pop(2)             # elimina y retorna el índice 2
lista.sort()             # ordena in-place (ascendente)
lista.sort(reverse=True) # ordena descendente
lista.reverse()          # invierte in-place
lista.count(1)           # cuántas veces aparece 1
lista.index(4)           # índice de la primera ocurrencia de 4
lista.clear()            # vacía la lista
```

---

## 5. Funciones sobre listas

```python
notas = [6.5, 4.0, 5.2, 3.8, 7.0]

len(notas)       # 5    — cantidad de elementos
sum(notas)       # 26.5 — suma total
max(notas)       # 7.0  — valor máximo
min(notas)       # 3.8  — valor mínimo
sorted(notas)    # retorna una NUEVA lista ordenada (no modifica la original)
```

---

## 6. Recorrer listas

### Con `for`

```python
notas = [6.5, 4.0, 5.2]
for nota in notas:
    print(f"Nota: {nota:.1f}")
```

### Con `for` e índice (`enumerate`)

```python
for i, nota in enumerate(notas):
    print(f"Nota {i+1}: {nota:.1f}")
```

### Con `while`

```python
i = 0
while i < len(notas):
    print(notas[i])
    i += 1
```

---

## 7. Verificar pertenencia

```python
frutas = ["manzana", "pera", "uva"]

"pera" in frutas         # True
"kiwi" not in frutas     # True
```

---

## 8. Listas anidadas (listas de listas)

```python
# Matriz 2x3 como lista de listas
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[0])       # [1, 2, 3]
print(matriz[1][2])    # 6
```

---

## Ejemplo integrador

```python
def ingresar_notas(cantidad):
    """Lee `cantidad` notas del usuario y las retorna en una lista."""
    notas = []
    for i in range(1, cantidad + 1):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)
    return notas

def estadisticas(notas):
    """Retorna promedio, máximo y mínimo de una lista de notas."""
    return sum(notas) / len(notas), max(notas), min(notas)

def mostrar_reporte(notas):
    """Procedimiento: imprime el reporte completo."""
    prom, maxi, mini = estadisticas(notas)
    aprobados = [n for n in notas if n >= 4.0]

    print(f"\nNotas     : {notas}")
    print(f"Promedio  : {prom:.2f}")
    print(f"Máxima    : {maxi:.1f}")
    print(f"Mínima    : {mini:.1f}")
    print(f"Aprobados : {len(aprobados)} de {len(notas)}")

# Programa principal
n      = int(input("¿Cuántas notas? "))
notas  = ingresar_notas(n)
mostrar_reporte(notas)
```