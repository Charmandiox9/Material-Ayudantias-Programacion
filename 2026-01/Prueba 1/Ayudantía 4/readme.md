# Ayudantía 4 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: lectura de archivos con `open()` + `readline()` + `.split()`, ciclos `while`, acumuladores, máximos/mínimos y procesamiento de datos estructurados.

---

## 📋 Ejercicios previos

Práctica guiada de `readline()` y `.split()` con tres archivos de distinta complejidad.

### Archivo `numeros.txt`
```
12
43
52
75
24
11
33
56
```

**Requerimientos**
- A. Imprimir todos los números.
- B. Imprimir solo los múltiplos de 3.
- C. Imprimir la cantidad de números y la suma de todos.
- D. Imprimir el número mayor y el número menor.

---

### Archivo `paises.txt`
Cada país tiene N valores debajo (Chile tiene 5, EE. UU. tiene 2, …):
```
Chile,5
23
46
74
24
78
Estados Unidos,2
44
12
Japón,3
22
46
10
```

**Requerimientos**
- A. Imprimir el nombre de cada país.
- B. Imprimir los valores de cada país.
- C. Contar cuántos países hay en el texto.
- D. Contar cuántos valores en total hay en el texto.
- E. Imprimir el valor mayor y menor del texto, y qué países los tienen.
- F. Imprimir el país cuya suma de valores sea la mayor.

---

### Archivo `temperaturas_regiones.txt`
Cada región tiene N comunas, y cada ciudad tiene varias temperaturas registradas:
```
Región de Coquimbo;6
La Serena,15.5,16.0
Vicuña,25.0,34.5,30.5,12.0,15.0
Ovalle,22.0,28.0,26.5
Illapel,24.0
Los Vilos,14.0,15.5
Monte Patria,20.0,25.0,-2.1,-1.0,10.0
Región de Valparaíso;5
Valparaíso,14.5,15.8
Viña del Mar,15.0,16.3,14.5
Quillota,18.0
San Antonio,13.8,15.0
Los Andes,20.0
```

**Requerimientos**
- A. Imprimir el nombre de cada ciudad y sus temperaturas.
- B. Imprimir el promedio de temperaturas de cada ciudad.
- C. Imprimir la temperatura más alta de cada región y la ciudad donde se registró.
- D. Imprimir la temperatura más baja de todo el texto y la ciudad donde se registró.
- E. Imprimir el promedio total de temperaturas de cada región.
- F. Imprimir la región más fría.

> **TIP:** Como no hay un valor que indique cuántas temperaturas registró una ciudad, usar `len()`:
> ```python
> cantidad_temperaturas = len(partes)
> ```

---

## 🎵 Ejercicio 1 — Spotify Wrapped

Spotify te pide crear un programa que resuma las estadísticas de la playlist de un usuario almacenada en un archivo `.txt`.

**Formato del archivo `playlist.txt`:**
```
ID,Cancion,Álbum,Minutos.Segundos,Rating,Año-Mes-Día,CantidadvecesEscuchada
```

**Ejemplo de línea:**
```
175,El Teléfono,The Bad Boy,3.92,76,2006-01-01,67
```

**Requerimientos**

- a) Cantidad de canciones en la playlist.
- b) La canción de mayor duración.
- c) La canción más escuchada.
- d) El rating promedio de las canciones escuchadas **más de 80 veces**.
- e) La cantidad de veces que se escuchó alguna canción del álbum **"Los Tres"** y el rating promedio de esas canciones.
- f) La canción más antigua.

**Ejemplo de salida**
```
-------Estadísticas--------
a) Cantidad de canciones en la playlist: 137
b) Canción de mayor duración: ACHO PR -> 398 segundos.
c) Canción más escuchada: Mentalité RMX (feat. ASHE 22) -> 120 veces.
d) Rating promedio de las canciones más escuchadas: 57.88
e) Cantidad de veces que se escuchó alguna canción del álbum chileno "Los Tres"
   y el rating promedio de esas canciones.
   ESCUCHAS TOTALES: 382
   PROMEDIO RATING: 48.2
f) La canción más antigua: Have You Ever Seen The Rain: 1970-12-7
```

**Patrón de lectura a usar:**
```python
arch = open("playlist.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
    partes = linea.strip().split(",")
    id_cancion  = partes[0]
    cancion     = partes[1]
    album       = partes[2]
    duracion    = float(partes[3])
    rating      = int(partes[4])
    fecha       = partes[5]
    escuchas    = int(partes[6])
    linea = arch.readline()

arch.close()
```

---

## 🏎️ Ejercicio 2 — ¡Comenzó la F1!

Eres fanático de la F1 y quieres analizar resultados históricos de corredores para informarte antes de la temporada 2026.

**Formato del archivo `f1.txt`:**
```
NombreCorredor,País,CantidadCarreras
AñoCarrera,Circuito,Equipo,Posicion,Puntos
```

**Ejemplo:**
```
Max Verstappen,Países Bajos,4
2023,Circuito de Monza,Red Bull,1,25
```

**Requerimientos**

1. El puntaje promedio de cada corredor.
2. La mejor carrera de **Red Bull** y **McLaren** (con mayor puntaje).
3. El corredor con el mejor puntaje promedio.
4. La mejor carrera del año **2019**.
5. La peor carrera de **España**.
6. El porcentaje de carreras hechas en cada año (2019, 2020, 2022, 2023).

**Ejemplo de salida**
```
Promedio de Max Verstappen -> 19.0
Promedio de Lewis Hamilton -> 16.25
Promedio de Charles Leclerc -> 17.0
Promedio de Fernando Alonso -> 15.75
Promedio de Lando Norris -> 19.33
Promedio de Sergio Pérez -> 15.0
Promedio de Carlos Sainz -> 18.33

2. La mejor carrera de Redbull y McLaren:
   Red Bull -> 2023,Circuito de Monza,Red Bull,1,25
   Mc Laren -> 2023,Circuito de Singapur,McLaren,1,25
3. El corredor con el mejor puntaje promedio:
   Lando Norris -> 19.33 puntaje
4. La mejor carrera del año 2019:
   2019,Circuito de Bakú,Red Bull,2,19
5. La peor carrera de España:
   2019,Circuito de Suzuka,Aston Martin,4,12
6. El porcentaje de carreras hechas en cada año:
   2019 -> 40.0%
   2020 -> 16.0%
   2022 -> 8.0%
   2023 -> 36.0%
```

**Patrón de lectura a usar (archivo con estructura de 2 líneas por bloque):**
```python
arch = open("f1.txt", "r", encoding="utf-8")
linea = arch.readline()

while linea != "":
    partes = linea.strip().split(",")
    nombre    = partes[0]
    pais      = partes[1]
    n_carreras = int(partes[2])

    for _ in range(n_carreras):
        linea = arch.readline()
        partes = linea.strip().split(",")
        año     = partes[0]
        circuito = partes[1]
        equipo  = partes[2]
        posicion = int(partes[3])
        puntos  = int(partes[4])

    linea = arch.readline()

arch.close()
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `open("f","r",encoding="utf-8")` | Abre el archivo en modo lectura con soporte de tildes |
| `readline()` | Lee una sola línea incluyendo `\n` al final |
| `.strip()` | Elimina `\n` y espacios del inicio/final de la línea |
| `.split(",")` | Divide la línea en una lista usando coma como separador |
| `while linea != "":` | Itera hasta que `readline()` devuelva string vacío (fin del archivo) |
| `int()` / `float()` | Convierte el string leído a número para operar |
| `len(partes)` | Cuenta cuántos elementos hay en la línea (útil cuando N es variable) |
| Acumulador | Variable que suma, cuenta o guarda máximos/mínimos línea a línea |
