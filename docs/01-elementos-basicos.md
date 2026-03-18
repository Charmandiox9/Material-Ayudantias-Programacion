# 01 · Elementos Básicos

Tipos de datos, variables, `input`, `print`, condicionales y ciclos.

---

## 1. Tipos de datos primitivos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Número entero | `edad = 20` |
| `float` | Número decimal | `nota = 6.5` |
| `str` | Texto (cadena de caracteres) | `nombre = "Ana"` |
| `bool` | Verdadero o falso | `aprobado = True` |

Puedes verificar el tipo de cualquier variable con `type()`:

```python
x = 42
print(type(x))   # <class 'int'>
```

---

## 2. Variables

Una variable es un nombre que apunta a un valor almacenado en memoria. En Python **no se declara el tipo**, se infiere automáticamente.

```python
# Asignación simple
nombre = "Rick"
edad   = 30
altura = 1.75

# Reasignación (el tipo puede cambiar)
x = 10
x = "ahora soy string"

# Múltiple asignación
a, b, c = 1, 2, 3
```

### Reglas de nomenclatura

- Usar `snake_case`: `monto_total`, `nombre_usuario`
- No empezar con número: ~~`1var`~~
- No usar guion medio: ~~`mi-variable`~~
- Sensible a mayúsculas: `Nombre ≠ nombre`

---

## 3. `input` y conversión de tipos

`input()` **siempre retorna `str`**. Si necesitas operar con números, debes convertir:

```python
nombre = input("¿Cómo te llamas? ")        # str
edad   = int(input("¿Cuántos años tienes? "))    # int
nota   = float(input("Ingresa tu nota: "))       # float
```

| Función | Convierte a |
|---------|-------------|
| `int(x)` | Entero |
| `float(x)` | Decimal |
| `str(x)` | Texto |
| `bool(x)` | Booleano |

---

## 4. `print` y f-strings

```python
nombre = "Mike"
gasto  = 54344.25

# Concatenación con +  (solo str con str)
print("Hola " + nombre)

# Separación con coma  (agrega espacio automático)
print("Gasto:", gasto)

# f-string  (recomendado)
print(f"Hola {nombre}, tu gasto fue {gasto:.2f}")
```

### Especificadores de formato en f-strings

| Especificador | Resultado | Ejemplo |
|---|---|---|
| `:.2f` | 2 decimales | `f"{3.14159:.2f}"` → `"3.14"` |
| `:.0f` | Sin decimales | `f"{6.9:.0f}"` → `"7"` |
| `:,` | Separador de miles | `f"{1000000:,}"` → `"1,000,000"` |
| `:>10` | Alineado a la derecha en 10 chars | |

---

## 5. Operadores

### Aritméticos

| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `3 + 2` | `5` |
| `-` | Resta | `5 - 1` | `4` |
| `*` | Multiplicación | `3 * 4` | `12` |
| `/` | División real | `10 / 3` | `3.333...` |
| `//` | División entera | `10 // 3` | `3` |
| `%` | Módulo (resto) | `10 % 3` | `1` |
| `**` | Potencia | `2 ** 8` | `256` |

> **Truco:** `n % 2 == 0` verifica si `n` es par.

### Comparación (retornan `bool`)

`==`  `!=`  `>`  `<`  `>=`  `<=`

### Lógicos

| Operador | Significado |
|---|---|
| `and` | Ambas condiciones verdaderas |
| `or` | Al menos una verdadera |
| `not` | Niega la condición |

---

## 6. Condicionales

```python
nota = float(input("Nota: "))

if nota >= 6.0:
    print("Excelente")
elif nota >= 4.0:
    print("Aprobado")
elif nota >= 3.0:
    print("Reprobado, cerca")
else:
    print("Reprobado")
```

- Solo puede haber **un `if`** y **un `else`** por bloque.
- Puede haber **cualquier cantidad de `elif`**.
- Python usa **indentación de 4 espacios** para definir bloques (no llaves `{}`).

### Condicional en una línea (ternario)

```python
estado = "Aprobado" if nota >= 4.0 else "Reprobado"
```

---

## 7. Ciclos

### `while` — repite mientras la condición sea verdadera

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### `for` — itera sobre una secuencia

```python
# Rango de números
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Iterar sobre un string
for letra in "Python":
    print(letra)
```

### `break` y `continue`

```python
for i in range(10):
    if i == 5:
        break       # sale del ciclo
    if i % 2 == 0:
        continue    # salta a la siguiente iteración
    print(i)        # imprime 1, 3
```

---

## 8. Funciones útiles

```python
round(3.14159, 2)    # 3.14 — redondea a n decimales
abs(-7)              # 7   — valor absoluto
max(3, 7, 1)         # 7   — máximo
min(3, 7, 1)         # 1   — mínimo
len("Python")        # 6   — largo de un string
```

---

## Ejemplo integrador

```python
# Calculadora de descuento
monto = float(input("Monto disponible: "))
gasto = float(input("Gasto deseado: "))

if gasto > monto:
    print("No tienes dinero suficiente")
else:
    if gasto <= 20000:
        descuento = 0
    elif gasto <= 50000:
        descuento = 0.05
    elif gasto <= 100000:
        descuento = 0.10
    else:
        descuento = 0.15

    if gasto % 2 == 0:
        gasto = gasto * (1 - descuento) * 0.97
        print("Descuento extra del 3% aplicado")
    else:
        gasto = gasto * (1 - descuento)

    print(f"Gasto final: {gasto:.2f}")
    print(f"Dinero restante: {monto - gasto:.2f}")
```