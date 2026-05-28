# 📦 Ayudantía 8 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: listas paralelas, búsqueda lineal con índice compartido, ordenamiento burbuja (Bubble Sort) aplicado a múltiples listas simultáneas, funciones que calculan mínimo, máximo y promedio **sin usar** `max()`, `min()` ni `sum()`, y cruce de datos entre dos archivos mediante código clave.

---

## 🏪 Ejercicio 1 — Bodeguero: La redención del congelamiento

El encargado de una bodega de electrónicos necesita un sistema para consultar el stock de productos almacenados en `bodega.txt`.

### Formato del archivo `bodega.txt`

```
Teclado,28
Monitor,8
Audifonos,3
Pilas,25
Mouse,12
```

### Listas paralelas obligatorias

```python
componentes = []   # nombres de productos
cantidades   = []  # stock de cada producto (int)
```

> El índice `i` en `componentes[i]` corresponde al mismo producto que `cantidades[i]`.

### Requerimientos

1. Leer `bodega.txt` y poblar ambas listas paralelas.
2. Solicitar al usuario el nombre de un artículo en un bucle (termina cuando el usuario deja vacío el campo).
3. Buscar el artículo recorriendo `componentes` con un `for` o `while` y compartir el índice con `cantidades`:
   - **Encontrado con stock ≥ 5** → mostrar cantidad disponible.
   - **Encontrado con stock < 5** → mostrar cantidad + `"ALERTA: ¡Stock critico en bodega! Se necesitan reponer unidades"`.
   - **No encontrado** → `"El componente no existe en los registros de la bodega"`.

### Ejemplo de salida

```
=== INICIANDO SISTEMA DE OPTIMIZACION DE BODEGA ===
Ingrese el articulo a consultar: monitor

Articulo encontrado: Monitor
Cantidad disponible: 8 unidades

Ingrese el articulo a consultar: audifonos

Articulo encontrado: Audifonos
Cantidad disponible: 3 unidades
ALERTA: ¡Stock critico en bodega! Se necesitan reponer unidades

Ingrese el articulo a consultar:
=== CERRANDO SISTEMA DE OPTIMIZACION DE BODEGA ===
```

---

## 📬 Ejercicio 2 — El Cartero Novato y el procesador de última generación

El cartero novato tiene dos archivos con información desordenada. Necesitas cruzar los datos por código, ordenar las entregas de menor a mayor distancia e imprimir la hoja de ruta.

### Formato de los archivos

**`paquetes.txt`** — información del destinatario:
```
PK-32,Ricardo Bugueño,Set de legos
PK-01,Ana Flores,Procesador i9
PK-15,Mariam Pinto,Audífonos
```

**`rutas.txt`** — información de entrega:
```
PK-32,Calle El Roble 78,8.9
PK-01,Av. Principal 12,1.5
PK-15,Los Pinos 34,7.9
```

### Listas paralelas obligatorias

```python
codigos    = []   # código único del paquete
clientes   = []   # nombre del destinatario
productos  = []   # contenido del paquete
distancias = []   # distancia en KM (float)
```

> El mismo índice `i` en las cuatro listas representa el **mismo paquete**.


### Funciones obligatorias

#### `ordenar_hoja_ruta(codigos, clientes, productos, distancias)`

Bubble Sort sobre `distancias` — **replicar cada intercambio en las otras 3 listas**:



#### `calcular_reporte(distancias)`

Calcula mínimo, máximo y promedio **sin usar** `max()`, `min()` ni `sum()`:


### Ejemplo de salida

```
==========================
HOJA DE RUTA EFICIENTE
==========================
CODIGO   | CLIENTE            | DISTANCIA
PK-02    | Alonso Alarcón     | 0.1  KM
PK-13    | Franco Cárdenas    | 0.9  KM
PK-39    | Vicente Morales    | 1.1  KM
PK-01    | Alana Flores       | 1.5  KM
...
PK-34    | Esteban Troncoso   | 103.3 KM

==========================
REPORTE DE RENDIMIENTO PARA EL JEFE
==========================
Domicilio más cercano: Alonso Alarcón (PK-02) a 0.1 KM
Domicilio más lejano:  Esteban Troncoso (PK-34) a 103.3 KM
Promedio de distancia por envío: 10.80 KM

==========================
MENSAJE AL CARTERO:
==========================
¡Problema resuelto cartero, ahora puedes entregarme mi procesador!
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| **Listas paralelas** | Varias listas donde el índice `i` representa la misma entidad en todas |
| **Búsqueda lineal con índice compartido** | `for i in range(len(lista)):` — el mismo `i` accede a todas las listas paralelas |
| **Bubble Sort en listas paralelas** | Cada intercambio en la lista clave debe replicarse en todas las demás |
| **Cruce por código** | Buscar el código de un archivo en la lista del otro para completar datos |
| **Mínimo manual** | Inicializar en `lista[0]`, iterar y comparar con `if d < minimo` |
| **Máximo manual** | Inicializar en `lista[0]`, iterar y comparar con `if d > maximo` |
| **Promedio manual** | Acumular con `total += d`, luego `total / len(lista)` |
| **Sin `max()` / `min()` / `sum()`** | Restricción explícita del ejercicio — implementar con ciclos |
