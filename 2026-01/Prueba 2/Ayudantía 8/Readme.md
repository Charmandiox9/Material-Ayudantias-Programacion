# 🎱 Ayudantía 9 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: matrices con NumPy (`np.zeros`, `shape`, recorrido con doble `for`), carga de matriz desde archivo, funciones que operan sobre matrices, búsqueda de máximo/mínimo por columna y suma por fila/columna.

---

## 🎰 Ejercicio 1 — Bingo APC UCN

Los centros de alumnos organizan un bingo benéfico para financiar la Academia de Programación Competitiva. El sistema debe cargar un cartón, gestionar el juego número a número y detectar automáticamente al ganador.

### Formato del archivo `carton.txt`

Matriz 5×5, números del 1 al 90 sin repetición, separados por espacios:

```
7 25 44 57 62
15 22 40 50 70
11 30 32 46 74
2 28 37 55 68
10 27 39 59 75
```

### Funciones requeridas

- `cargar_matriz(nombre_archivo)`: Lee el archivo y retorna una matriz NumPy 5×5:
- `imprimir_matriz(matriz)`: Imprime el cartón, mostrando `0` donde el número ya fue marcado:
- `marcar_numero(matriz, numero)`: Reemplaza el número por `0` si lo encuentra en la matriz:
- `verificar_ganador(matriz)`: Retorna `True` si **todos** los valores son `0`:


### Flujo del programa principal

1. Cargar el cartón desde `carton.txt`.
2. Imprimir el cartón inicial.
3. Solicitar números en bucle (`-1` para terminar sin ganador).
4. Validar que el número esté entre 1 y 90.
5. Marcar el número e imprimir el cartón actualizado.
6. Si todos los valores son `0` → anunciar ganador y terminar.

### Ejemplo de salida

```
Bingo a beneficio del APC UCN
-------------------------
5 17 32 48 61
9 23 41 55 72
3 14 38 60 88
7 29 45 63 80
11 36 52 69 90
-------------------------
Ingrese el numero (-1 para terminar): 5
-------------------------
0 17 32 48 61
9 23 41 55 72
...
```

---

## 🏆 Ejercicio 2 — Academia de Programación Competitiva UCN

La APC-UCN realizó una competencia interna. Cada equipo intentó resolver 7 ejercicios (A–G). Los resultados están en `resultados_apc.txt` y se pide generar un reporte de rendimiento.

### Formato del archivo `resultados_apc.txt`

```
NombreEquipo;resultado_A;resultado_B;resultado_C;resultado_D;resultado_E;resultado_F;resultado_G
EmpanadaDeQueso;1;0;1;1;0;1;1
Choripanes;0;1;1;0;1;1;1
RuntimeError;1;1;0;1;1;0;1
```

- `1` = ejercicio resuelto · `0` = no resuelto
- Siempre 7 ejercicios (columnas 0–6 = A–G)
- Número de equipos variable

### Funciones requeridas

- `cargar_nombres(nombre_archivo)`: Retorna lista con los nombres de los equipos:
- `cargar_matriz(nombre_archivo)`: Retorna matriz NumPy con los resultados (filas = equipos, columnas = ejercicios):
- `total_por_equipo(nombres, matriz)`: Imprime cuántos ejercicios resolvió cada equipo:
- `ejercicio_mas_resuelto(matriz)`: Retorna la letra del ejercicio con más equipos que lo resolvieron:
- `ejercicio_menos_resuelto(matriz)`: Igual que el anterior pero buscando el mínimo:
- `equipos_destacados(nombres, matriz)`: Imprime equipos que resolvieron **más de 3** ejercicios:

### Ejemplo de salida

```
--------------------------
Total de ejercicios resueltos por equipo
EmpanadaDeQueso: 5
Choripanes: 4
Foo: 5
EmpanadaDePollo: 4
TimeLimitExceeded: 1
CPlusPlus: 3
Pythons: 2
JavaCoders: 6
--------------------------
Ejercicio mas resuelto: G
Ejercicio menos resuelto: E
--------------------------
Equipos que resolvieron mas de 3 ejercicios
EmpanadaDeQueso (5 ejercicios)
Choripanes (4 ejercicios)
Foo (5 ejercicios)
EmpanadaDePollo (4 ejercicios)
JavaCoders (6 ejercicios)
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `np.zeros((f, c))` | Crea matriz de `f` filas × `c` columnas rellena con ceros |
| `matriz.shape[0]` | Número de filas de la matriz |
| `matriz.shape[1]` | Número de columnas de la matriz |
| `matriz[i][j]` | Accede al elemento en fila `i`, columna `j` |
| `int(matriz[i][j])` | Convierte el float de NumPy a entero para imprimir/comparar |
| Recorrido doble `for` | `for i in range(shape[0])` + `for j in range(shape[1])` |
| Suma por fila | Acumular `matriz[i][j]` fijando `i`, variando `j` |
| Suma por columna | Acumular `matriz[i][j]` fijando `j`, variando `i` |
| Máximo por columna | Inicializar en `0`, comparar con `if total > max_total` |
| Mínimo por columna | Inicializar en `n_filas`, comparar con `if total < min_total` |
