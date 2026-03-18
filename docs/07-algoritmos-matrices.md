# 07 · Algoritmos sobre Matrices

Búsqueda, ordenamiento y operaciones clásicas sobre matrices con NumPy.

---

## 1. Búsqueda en una matriz

### Búsqueda lineal 2D

Recorre fila por fila buscando un valor. Retorna la posición `(fila, columna)`.

```python
import numpy as np

def buscar_en_matriz(matriz, objetivo):
    """
    Busca un valor en la matriz.
    Retorna (fila, col) si lo encuentra, o (-1, -1) si no existe.
    """
    filas, cols = matriz.shape
    for i in range(filas):
        for j in range(cols):
            if matriz[i, j] == objetivo:
                return (i, j)
    return (-1, -1)

m = np.array([
    [10, 25,  3],
    [42,  7, 18],
    [ 5, 33, 11]
])

pos = buscar_en_matriz(m, 18)
print(pos)   # (1, 2)

pos = buscar_en_matriz(m, 99)
print(pos)   # (-1, -1)
```

---


## 2. Ordenar filas y columnas

### Ordenar cada fila

```python
m = np.array([
    [3, 1, 4],
    [9, 2, 7],
    [5, 8, 6]
])

m_ordenado = np.sort(m, axis=1)   # ordena cada fila
print(m_ordenado)
# [[1 3 4]
#  [2 7 9]
#  [5 6 8]]
```

### Ordenar cada columna

```python
m_col = np.sort(m, axis=0)   # ordena cada columna
print(m_col)
# [[3 1 4]
#  [5 2 6]
#  [9 8 7]]
```

### Ordenar manualmente una fila con Bubble Sort

```python
def bubble_sort_fila(matriz, fila):
    """Ordena in-place la fila indicada de la matriz."""
    n = matriz.shape[1]
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[fila, j] > matriz[fila, j + 1]:
                matriz[fila, j], matriz[fila, j + 1] = \
                    matriz[fila, j + 1], matriz[fila, j]

m = np.array([[5, 3, 8, 1, 4]], dtype=float)
bubble_sort_fila(m, 0)
print(m)   # [[1. 3. 4. 5. 8.]]
```

---

## 3. Operaciones clásicas implementadas manualmente

### Suma de matrices

```python
def suma_matrices(a, b):
    """Suma dos matrices del mismo tamaño sin usar NumPy."""
    filas, cols = a.shape
    resultado = np.zeros((filas, cols))
    for i in range(filas):
        for j in range(cols):
            resultado[i, j] = a[i, j] + b[i, j]
    return resultado

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(suma_matrices(a, b))
# [[ 6.  8.]
#  [10. 12.]]
```

### Multiplicación de matrices (producto punto manual)

```python
def multiplicar_matrices(a, b):
    """Multiplica a (m×k) por b (k×n), resultado m×n."""
    m, k = a.shape
    k2, n = b.shape
    if k != k2:
        raise ValueError("Dimensiones incompatibles")
    resultado = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            for p in range(k):
                resultado[i, j] += a[i, p] * b[p, j]
    return resultado

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(multiplicar_matrices(a, b))
# [[19. 22.]
#  [43. 50.]]

# Equivalente con NumPy:
print(a @ b)
```

---

## 4. Guía

| Tarea | Manual (loops) |
|---|---|
| Suma | `resultado[i,j] = a[i,j] + b[i,j]` |
| Máximo | loop comparando |
| Ordenar fila | Bubble Sort manual |
| Buscar valor | doble loop |
| Transponer | loop intercambiando |
| Diagonal | loop `m[i,i]` |

> Los algoritmos manuales sirven para entender la lógica.
