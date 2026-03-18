# 05 · Matrices con NumPy

Creación, acceso y operaciones sobre matrices usando la librería NumPy.

---

## 1. ¿Qué es NumPy?

NumPy es la librería estándar de Python para cálculo numérico. Permite trabajar con arreglos y matrices de forma eficiente.

```python
import numpy as np
```

> Si no está instalada: `pip install numpy`

---

## 2. Crear matrices

### Matriz de ceros

```python
# np.zeros((filas, columnas))
matriz = np.zeros((3, 4))
print(matriz)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
```

### Matriz de unos

```python
matriz = np.ones((2, 3))
```

### Matriz desde una lista

```python
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

### Matriz con valores aleatorios

```python
aleatoria = np.random.randint(0, 10, (3, 3))   # enteros entre 0 y 9
aleatoria = np.random.rand(3, 3)                # decimales entre 0 y 1
```

---

## 3. Dimensiones y forma

```python
matriz = np.zeros((3, 4))

print(matriz.shape)    # (3, 4) — filas, columnas
print(matriz.ndim)     # 2      — número de dimensiones
print(matriz.size)     # 12     — total de elementos
print(matriz.dtype)    # float64 — tipo de dato
```

---

## 4. Acceder a elementos

```python
m = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(m[0][1])    # 20  — fila 0, columna 1
print(m[1, 2])    # 60  — notación directa (recomendada)
print(m[2, -1])   # 90  — última columna de la fila 2
```

---

## 5. Modificar elementos

```python
m = np.zeros((3, 3))

m[0, 0] = 5       # asignar un valor
```

---

## 6. Recorrer una matriz

```python
m = np.array([[1, 2, 3], [4, 5, 6]])

# Por filas y columnas
for i in range(m.shape[0]):          # filas
    for j in range(m.shape[1]):      # columnas
        print(f"m[{i},{j}] = {m[i,j]}")

# Iterar elemento por elemento
for fila in m:
    for elemento in fila:
        print(elemento)
```

---

## 7. Operaciones matemáticas

NumPy aplica las operaciones **elemento a elemento**:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

a + b          # suma elemento a elemento
a * b          # multiplicación elemento a elemento
a + 10         # suma escalar (a cada elemento)
a * 2          # multiplicación escalar
a ** 2         # potencia elemento a elemento
```

### Multiplicación matricial (producto punto)

```python
np.dot(a, b)   # o bien: a @ b
```

---

## 8. Funciones estadísticas

```python
m = np.array([[3, 7, 1], [4, 5, 6]])

np.sum(m)           # suma de todos los elementos
np.sum(m, axis=0)   # suma por columnas  → [7, 12, 7]
np.sum(m, axis=1)   # suma por filas     → [11, 15]

np.mean(m)          # promedio global
np.max(m)           # máximo global
np.min(m)           # mínimo
np.std(m)           # desviación estándar
```

---

## Ejemplo integrador

```python
import numpy as np

def crear_tabla_notas(n_alumnos, n_pruebas):
    """Crea y llena una matriz de notas n_alumnos x n_pruebas."""
    notas = np.zeros((n_alumnos, n_pruebas))
    for i in range(n_alumnos):
        for j in range(n_pruebas):
            notas[i, j] = float(input(f"Alumno {i+1}, Prueba {j+1}: "))
    return notas

def reporte(notas):
    """Imprime promedios por alumno y por prueba."""
    print("\n--- Promedios por alumno ---")
    promedios = np.mean(notas, axis=1)
    for i, prom in enumerate(promedios):
        estado = "Aprobado" if prom >= 4.0 else "Reprobado"
        print(f"  Alumno {i+1}: {prom:.2f} — {estado}")

    print("\n--- Promedios por prueba ---")
    for j, prom in enumerate(np.mean(notas, axis=0)):
        print(f"  Prueba {j+1}: {prom:.2f}")

    print(f"\nNota más alta : {np.max(notas):.1f}")
    print(f"Nota más baja : {np.min(notas):.1f}")
    print(f"Promedio gral : {np.mean(notas):.2f}")

# Programa principal
n_alumnos = int(input("Número de alumnos: "))
n_pruebas = int(input("Número de pruebas: "))
tabla = crear_tabla_notas(n_alumnos, n_pruebas)
reporte(tabla)
```

### Salida de ejemplo

```
Número de alumnos: 3
Número de pruebas: 2
Alumno 1, Prueba 1: 6.5
Alumno 1, Prueba 2: 5.0
...

--- Promedios por alumno ---
  Alumno 1: 5.75 — Aprobado
  Alumno 2: 3.90 — Reprobado
  Alumno 3: 6.00 — Aprobado

--- Promedios por prueba ---
  Prueba 1: 5.33
  Prueba 2: 5.17

Nota más alta : 7.0
Nota más baja : 2.8
Promedio gral : 5.25
```