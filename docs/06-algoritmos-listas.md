# 06 · Algoritmos sobre Listas

Búsqueda y ordenamiento implementados manualmente en Python.

---

## 1. Búsqueda Lineal

Recorre la lista elemento por elemento hasta encontrar el valor buscado.

- **Mejor caso:** el elemento está en la primera posición → O(1)
- **Peor caso:** el elemento no existe o está al final → O(n)

```python
def busqueda_lineal(lista, objetivo):
    """Retorna el índice del objetivo, o -1 si no existe."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

notas = [6.5, 3.8, 5.2, 4.0, 7.0]
idx = busqueda_lineal(notas, 5.2)

if idx != -1:
    print(f"Encontrado en índice {idx}")   # Encontrado en índice 2
else:
    print("No encontrado")
```

---

## 2. Búsqueda Binaria

Solo funciona sobre **listas ordenadas**. Divide el espacio de búsqueda a la mitad en cada paso.

- **Complejidad:** O(log n) — mucho más rápida que la lineal en listas grandes.

```python
def busqueda_binaria(lista, objetivo):
    """
    Retorna el índice del objetivo en una lista ORDENADA,
    o -1 si no existe.
    """
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        mid = (izq + der) // 2

        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            izq = mid + 1      # buscar en la mitad derecha
        else:
            der = mid - 1      # buscar en la mitad izquierda

    return -1

numeros = [1, 3, 5, 7, 9, 11, 15, 20]
print(busqueda_binaria(numeros, 11))   # 5
print(busqueda_binaria(numeros, 6))    # -1
```

### Paso a paso con lista [1, 3, 5, 7, 9, 11, 15, 20], buscando 11

```
izq=0  der=7  mid=3  lista[3]=7  → 7 < 11  → izq=4
izq=4  der=7  mid=5  lista[5]=11 → ¡encontrado! → return 5
```

---

## 3. Bubble Sort (Ordenamiento de burbuja)

Compara pares adyacentes y los intercambia si están en el orden incorrecto. Repite hasta que no haya intercambios.

- **Complejidad:** O(n²) — simple de entender, lento para listas grandes.

```python
def bubble_sort(lista):
    """Ordena la lista in-place de menor a mayor."""
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):    # cada pasada "burbujea" el mayor al final
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]   # intercambio

notas = [6.5, 3.8, 5.2, 4.0, 7.0, 1.5]
bubble_sort(notas)
print(notas)   # [1.5, 3.8, 4.0, 5.2, 6.5, 7.0]
```

### Visualización con [5, 3, 8, 1]

```
Pasada 1:  [3, 5, 8, 1] → [3, 5, 8, 1] → [3, 5, 1, 8]
Pasada 2:  [3, 5, 1, 8] → [3, 1, 5, 8]
Pasada 3:  [1, 3, 5, 8]  ← lista ordenada
```

### Versión optimizada (para si ya está ordenada)

```python
def bubble_sort_opt(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break    # ya está ordenada, no seguir
```

---

## 4. Selection Sort (Ordenamiento por selección)

En cada pasada encuentra el **mínimo** del resto de la lista y lo coloca en su posición correcta.

- **Complejidad:** O(n²)

```python
def selection_sort(lista):
    """Ordena la lista in-place de menor a mayor."""
    n = len(lista)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j
        lista[i], lista[idx_min] = lista[idx_min], lista[i]

nums = [64, 25, 12, 22, 11]
selection_sort(nums)
print(nums)   # [11, 12, 22, 25, 64]
```

### Visualización con [64, 25, 12, 22, 11]

```
i=0: mínimo=11 (idx 4) → [11, 25, 12, 22, 64]
i=1: mínimo=12 (idx 2) → [11, 12, 25, 22, 64]
i=2: mínimo=22 (idx 3) → [11, 12, 22, 25, 64]
i=3: mínimo=25 (idx 3) → [11, 12, 22, 25, 64]
```

---

## 5. Insertion Sort (Ordenamiento por inserción)

Toma cada elemento y lo inserta en la posición correcta dentro de la parte ya ordenada.

- **Complejidad:** O(n²) peor caso, **O(n) mejor caso** (lista casi ordenada).
- Muy eficiente para listas pequeñas o casi ordenadas.

```python
def insertion_sort(lista):
    """Ordena la lista in-place de menor a mayor."""
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]    # desplaza un lugar a la derecha
            j -= 1
        lista[j + 1] = clave           # inserta en la posición correcta

datos = [5, 2, 4, 6, 1, 3]
insertion_sort(datos)
print(datos)   # [1, 2, 3, 4, 5, 6]
```

---

## 6. Comparación de algoritmos

| Algoritmo | Mejor caso | Peor caso | Estable | Cuándo usarlo |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | Sí | Aprender, listas muy pequeñas |
| Selection Sort | O(n²) | O(n²) | No | Simple, pocas escrituras |
| Insertion Sort | O(n) | O(n²) | Sí | Listas casi ordenadas |
| `sorted()` Python | O(n log n) | O(n log n) | Sí | Producción, siempre |

> En la práctica, usa siempre `sorted(lista)` o `lista.sort()`. Los algoritmos manuales sirven para aprender y son tema de examen.

---

## 7. Ordenar con criterio personalizado

```python
alumnos = [("Ana", 6.5), ("Bob", 3.8), ("Carlos", 5.2)]

# Ordenar por nota (segundo elemento de cada tupla)
alumnos.sort(key=lambda x: x[1])
print(alumnos)   # [('Bob', 3.8), ('Carlos', 5.2), ('Ana', 6.5)]

# Descendente
alumnos.sort(key=lambda x: x[1], reverse=True)
```

---

## Ejemplo integrador

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1

# Leer notas, ordenar y buscar
notas = []
n = int(input("¿Cuántas notas? "))
for i in range(n):
    notas.append(float(input(f"Nota {i+1}: ")))

bubble_sort(notas)
print(f"\nNotas ordenadas: {notas}")
print(f"Mínima: {notas[0]}  |  Máxima: {notas[-1]}")

buscar = float(input("\nNota a buscar: "))
idx = busqueda_binaria(notas, buscar)
if idx != -1:
    print(f"Encontrada en posición {idx + 1} de la lista ordenada")
else:
    print("Esa nota no está en la lista")
```