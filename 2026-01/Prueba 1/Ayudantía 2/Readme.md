# Ayudantía 2 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: variables, tipos de datos, condicionales (`if/elif/else`), ciclos (`while`, `for`) y validación de entrada.

---

## 📋 Ejercicios

### 1. Hay que cocinar 🧑‍🍳

Fernando vende chaparritas en la UCN para ganar un dinero extra. Te pide un programa que le ayude a llevar el control de sus ventas y calcular sus ganancias del día.

**Tabla de costos y ganancias**

| Producto | Precio de venta | Costo de producción |
|---|---|---|
| Simple | $1.000 | $400 |
| Napolitana | $1.500 | $900 |
| Vegana | $1.300 | $700 |
| Condimentos | $200 | $50 |

**Requerimientos**

0. **Menú** (se repite hasta que el usuario elija Salir)
   - `1. Agregar venta`
   - `2. Mostrar resumen del día`
   - `3. Salir del programa`
   - Validar que la opción ingresada sea 1, 2 o 3.

1. **Agregar venta**
   - Preguntar tipo de chaparrita: `Simple`, `Napolitana` o `Vegana` (validar entrada).
   - Preguntar si el cliente agrega condimentos: `Si` o `No`.
   - Confirmar con mensaje `"Chaparrita [tipo] agregada!"`.

2. **Mostrar resumen del día**
   - Si no se ha vendido nada → imprimir `"¡Todavía no vendes nada!"`
   - Si hay ventas, mostrar:
     - Cantidad de chaparritas vendidas
     - Ganancia bruta del día
     - Costo total del día
     - Ganancia neta (ganancia − costo)
     - Porcentaje de venta de cada tipo (con `round(pct, 2)`)
     - Tipo de chaparrita con más ventas

3. **Salir** → imprimir `"Adios Fernando, suerte con las ventas!"`

**Ejemplo de salida**
```
● Bienvenido Fernando! ¿Que quieres hacer?
1. Agregar venta.
2. Mostrar resumen del dia.
3. Salir del programa.
Ingresa tu opcion: 1
Ingresa el tipo de chaparra vendida (Simple, Napolitana, Vegana): Simple
Agrega condimentos? (Si, No): Si
Chaparrita Simple agregada!
...
====== RESUMEN DEL DIA ======
Cantidad de chaparritas vendidas: 3
Ganancia: 3700$
Costo total: 1750$
Ganancia total: 1950$
Porcentaje de venta de cada chaparrita:
Chaparrita simple: 66.67%
Chaparrita napolitana: 33.33%
Chaparrita vegana: 0.0%
Chaparrita más vendida: Simple
```

---

### 2. Calculando... 🔢

La Escuela de Ciencias Básicas necesita una herramienta que valide los cálculos matemáticos de sus estudiantes de enseñanza media. Te piden crear un verificador en Python usando ciclos.

**Requerimientos**

Pedir un número `n` entre **1 y 1000** (validar). Calcular y mostrar:

1. **Sumatoria** — suma desde 1 hasta n:

$$\sum_{i=1}^{n} i = 1 + 2 + 3 + \cdots + n$$

2. **Factorial** — multiplicación desde 1 hasta n:

$$n! = 1 \times 2 \times 3 \times \cdots \times n$$

3. **Potencia** — n multiplicado por sí mismo n veces (**sin usar `**`**):

$$n^n = n \times n \times n \times \cdots \times n$$

4. **Primo** — determinar si n es primo (divisible solo por 1 y por sí mismo). El número 1 **no** se considera primo.

Luego preguntar si ingresar otro número o salir (ingresando `-1`).

**Consideraciones**
- Prohibido usar el operador `**` para la potencia → usar ciclo `for` o `while`.
- Validar que `n` esté entre 1 y 1000.
- El número 1 no es primo.
- Usar ciclos para todas las operaciones.

**Ejemplo de salida**
```
● Ingrese el número entero positivo para analizar (0 al 1000): 1000000
Numero fuera de rango, ingrese nuevamente: 7
======== RESULTADOS =========
> Sumatoria: 28
> Factorial: 5040
> Potencia (7^7): 823543
> El número 7 es primo.
=============================
Ingresa otro numero para continuar, para salir ingresa -1: 10
======== RESULTADOS =========
> Sumatoria: 55
> Factorial: 3628800
> Potencia (10^10): 10000000000
> El número 10 no es primo.
=============================
Ingresa otro numero para continuar, para salir ingresa -1: -1
Saliendo del programa...
```

---

## 📋 Ejercicios de Ruteo

### 1. Condicionales

```python
k = 5
p = 2
u = 12
nn = ""

a = False
b = False
c = False
d = False
e = False

if u % p != 0 and k < u // (p + 1):
  a = True

  if (k + u) // u == 1:
    b = True

  elif (k + 3) / u < 0.6 or (k + 1) // u == 0:
    c = True
    p = 4
  else:
    d = True
    if u == 12:
      b = False
      e = True
      k = 6

if p ** 2 == p ** 2 and u / 4 == 3:
  d = not d

else:
  e = True

if (a and b) or (c and not d) or (e and not a):
  nn = nn + "1"
else:
  nn = nn + "0"

print(str((int(nn) + 7) * 3 - 2) + nn)
```

**Requerimientos:**
Anotar como las variables van cambiando (si es que lo hacen) y la salida que tiene al finalizar el programa:

| k | p | u | nn | a | b | c | d | e |
|---|---|---|----|---|---|---|---|---|
|  |  |   |   |
|  |  |   |   |
|  |  |   |   |
|  |  |   |   |

Salida:


### 2. Ciclos

```python
n = 5
resultado = 0
contador = 0

for i in range(1, n + 1):
  if i % 2 != 0:
    resultado += i * 2
    contador += 1
  else:
    resultado -= i

k = contador
while k > 0:
  resultado += k
  k -= 1

limite = resultado // contador

if limite > 10 and resultado % 2 == 0:
  salida = "PAR"
elif limite > 10:
  salida = "IMPAR"
else:
  salida = "BAJO"

print(resultado, contador, salida)
```

**Requerimientos:**
Anotar como las variables van cambiando (si es que lo hacen) y la salida que tiene al finalizar el programa:

| n | resultado | contador | k | limite | salida |
|---|---|---|----|---|---|
|  |  |   |   |
|  |  |   |   |
|  |  |   |   |
|  |  |   |   |

Salida:

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `while` | Repite mientras la condición sea verdadera — útil para menús y validación |
| `for` + `range()` | Itera un número fijo de veces — ideal para sumas, productos, potencias |
| `break` | Sale inmediatamente del ciclo |
| `continue` | Salta a la siguiente iteración sin ejecutar el resto del cuerpo |
| Validación de entrada | Pedir de nuevo si el valor no cumple la condición — patrón `while True` |
| `%` (módulo) | Verificar divisibilidad: `n % i == 0` — clave para detectar primos |
| Acumuladores | Variable que va sumando o multiplicando dentro de un ciclo |
