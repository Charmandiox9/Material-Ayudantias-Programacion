# 03 · Subprogramas

Funciones, procedimientos y la diferencia entre ambos.

---

## 1. ¿Qué es un subprograma?

Un subprograma es un bloque de código con nombre que realiza una tarea específica y puede ser llamado desde cualquier parte del programa. Permiten:

- **Reutilizar** código sin repetirlo.
- **Organizar** el programa en partes más pequeñas.
- **Facilitar** el mantenimiento y la lectura.

En Python se definen con la palabra clave `def`.

---

## 2. Procedimiento vs Función

| | Procedimiento | Función |
|---|---|---|
| **Retorna valor** | No (`return` ausente o `return None`) | Sí (`return valor`) |
| **Propósito** | Ejecutar acciones (imprimir, modificar) | Calcular y devolver un resultado |
| **Uso** | Se llama solo: `mostrar_menu()` | Se usa en expresión: `x = calcular(5)` |

> En Python no existe una palabra separada para procedimientos; ambos se definen con `def`. La diferencia es si usan `return` o no.

---

## 3. Definir y llamar subprogramas

### Procedimiento (sin `return`)

```python
def mostrar_bienvenida():
    print("Bienvenido forastero, ¿Qué quieres hacer?")
    print("1) Comprar Suministros")
    print("2) Salir")

# Llamada
mostrar_bienvenida()
```

### Función (con `return`)

```python
def calcular_descuento(gasto):
    if gasto <= 20000:
        return 0.0
    elif gasto <= 50000:
        return 0.05
    elif gasto <= 100000:
        return 0.10
    else:
        return 0.15

# Llamada
desc = calcular_descuento(62250)
print(f"Descuento: {desc * 100:.0f}%")   # Descuento: 10%
```

---

## 4. Parámetros y argumentos

```python
# nombre y edad son parámetros (en la definición)
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")

# "Rick" y 30 son argumentos (en la llamada)
saludar("Rick", 30)
```

### Parámetros con valor por defecto

```python
def calcular_tiempo(distancia, velocidad=60.0):
    return distancia / velocidad

print(calcular_tiempo(120))        # usa velocidad=60 → 2.0
print(calcular_tiempo(120, 80))    # usa velocidad=80 → 1.5
```

---

## 5. Scope (alcance de variables)

Las variables definidas **dentro** de una función son **locales** y no existen fuera de ella.

```python
def sumar(a, b):
    resultado = a + b    # variable local
    return resultado

sumar(3, 4)
print(resultado)         # NameError: resultado no existe aquí
```

Para usar una variable global dentro de una función (poco recomendado):

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)   # 1
```

---

## 6. Buenas prácticas

- **Un subprograma = una tarea.** Si hace más de una cosa, divídelo.
- **Nombres en verbo** para procedimientos: `mostrar_menu()`, `leer_datos()`.
- **Nombres descriptivos** para funciones: `calcular_descuento()`, `convertir_millas()`.
- **No usar `print` dentro de funciones** que calculan — retorna el valor y el que llama decide qué hacer con él.

---

## Ejemplo integrador

```python
def leer_nota(mensaje):
    """Lee y retorna una nota válida (1.0 a 7.0)."""
    nota = float(input(mensaje))
    return nota

def calcular_promedio(n1, n2, n3):
    """Retorna el promedio de tres notas."""
    return (n1 + n2 + n3) / 3

def mostrar_resultado(nombre, promedio):
    """Procedimiento: imprime el resultado del alumno."""
    estado = "Aprobado" if promedio >= 4.0 else "Reprobado"
    print(f"\n--- Resultado de {nombre} ---")
    print(f"Promedio : {promedio:.1f}")
    print(f"Estado   : {estado}")

# Programa principal
nombre   = input("Nombre del alumno: ")
n1 = leer_nota("Nota 1: ")
n2 = leer_nota("Nota 2: ")
n3 = leer_nota("Nota 3: ")

prom = calcular_promedio(n1, n2, n3)
mostrar_resultado(nombre, prom)
```