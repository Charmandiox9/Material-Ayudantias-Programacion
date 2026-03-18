# 02 · Lectura de Archivos

Apertura, lectura y cierre de archivos de texto con `open()`.

---

## 1. Abrir un archivo

```python
archivo = open("datos.txt", "r", encoding="utf-8")
```

### Modos de apertura

| Modo | Descripción |
|------|-------------|
| `"r"` | Lectura (error si no existe) |
| `"w"` | Escritura (crea o sobreescribe) |
| `"a"` | Agregar al final (append) |
| `"r+"` | Lectura y escritura |

> Siempre usar `encoding="utf-8"` para evitar problemas con tildes y ñ.

---

## 2. Métodos de lectura

```python
arch = open("notas.txt", "r", encoding="utf-8")

# Leer todo el contenido como un solo string
contenido = arch.read()

# Leer una sola línea (incluye el \n al final)
linea = arch.readline()

# Leer todas las líneas como lista de strings
lineas = arch.readlines()

arch.close()
```

### `.strip()` — eliminar espacios y saltos de línea

`readline()` incluye `\n` al final. Usar `.strip()` para limpiar:

```python
arch = open("datos.txt", "r", encoding="utf-8")
linea = arch.readline().strip()   # quita espacios y \n
print(linea)
arch.close()
```

---


## 3. Leer línea por línea con `readline()`


```python
arch = open("alumnos.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    nombre = partes[0]
    nota   = float(partes[1])
    print(f"{nombre}: {nota}")
    linea = arch.readline().strip()
```

---

## 4. Separar datos en una línea (split)

Si una línea contiene varios valores separados por coma, espacio u otro carácter:

```python
# Archivo: "Ana,6.5,True"
arch = open("datos.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")        # ["Ana", "6.5", "True"]
    nombre    = partes[0]
    nota      = float(partes[1])
    aprobado  = partes[2] == "True"
    print(f"{nombre} — {nota:.1f} — {aprobado}")
    linea = arch.readline().strip()
```

---

## Ejemplo integrador

```python
# Lee un archivo con nombres y notas, calcula el promedio

total = 0
cantidad = 0

arch = open("notas.txt", "r", encoding="utf-8")
linea = arch.readline().split()

while linea != "":
    partes = linea.split(",")
    nombre   = partes[0]
    nota     = float(partes[1])
    total   += nota
    cantidad += 1
    estado   = "Aprobado" if nota >= 4.0 else "Reprobado"
    print(f"{nombre}: {nota:.1f} — {estado}")
    linea = arch.readline().strip()

if cantidad > 0:
    print(f"\nPromedio del curso: {total / cantidad:.2f}")
```

Contenido de `notas.txt`:
```
Ana,6.5
Bob,3.8
Carlos,5.2
Diana,4.0
```