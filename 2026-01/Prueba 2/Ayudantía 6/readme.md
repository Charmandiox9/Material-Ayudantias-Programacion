# 💊 Ayudantía 7 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: listas (`append`, `pop`, índices), lectura de archivos por bloques, funciones con parámetros, ciclos `for` y `while`, clasificación por rangos, ordenamiento manual (sin `sort()`/`sorted()`), búsqueda en listas y cálculo de cobros.

---

## 🏥 Ejercicio 1 — Sistema de control de recetas en una farmacia

La farmacia **Turno de Invierno** recibe un inventario desde un archivo y necesita revisar recetas automáticamente, entregando medicamentos solo si hay stock disponible. Cada unidad entregada **debe retirarse** de la lista (inventario finito).

### Clasificación de medicamentos por código

| Rango de código | Grupo |
|---|---|
| 100 – 199 | `"analgésico"` |
| 200 – 299 | `"antibiótico"` |
| 300 – 399 | `"vitamina"` |
| Fuera de rango | `"inválido"` |

### Formato del archivo `inventario.txt`

Bloques con encabezado `grupo,minimo,maximo` seguidos de códigos, uno por línea:

```
vitamina,300,399
301
305
410
399
analgesico,100,199
101
105
109
230
199
antibiotico,200,299
201
205
299
100
```

> **Nota:** el archivo puede contener códigos fuera del rango del grupo (ej: `410` en el bloque vitamina, `230` en analgésico). Deben ignorarse al clasificar.

### Formato del archivo `receta_n.txt`

Un código por línea:
```
101
105
201
301
305
```

### Listas obligatorias

```python
analgésicos    = []
antibióticos   = []
vitaminas      = []
receta         = []
entregados     = []
no_disponibles = []
inválidos      = []
```

### Flujo del programa

1. Leer `inventario.txt` y clasificar cada código en su lista correspondiente según rango. Ignorar códigos fuera del rango del grupo declarado.
2. Pedir al usuario qué receta revisar (`receta_1`, `receta_2` o `receta_3`). Validar la entrada — si es inválida, mostrar `"Opción inválida"` y pedir de nuevo.
3. Leer el archivo de la receta seleccionada y guardar los códigos en `receta`.
4. Recorrer `receta` código por código:
   - Si el código **no pertenece a ningún rango válido** → agregar a `inválidos`.
   - Si pertenece a un grupo válido y **está en el inventario** → usar `.pop()` para retirarlo y agregarlo a `entregados`.
   - Si pertenece a un grupo válido pero **no está en el inventario** → agregar a `no_disponibles`.
5. El inventario **persiste durante toda la ejecución**: lo entregado en una receta ya no está disponible para las siguientes.
6. Mostrar el resumen y preguntar si revisar otra receta (`Si` / `No`). Validar la respuesta.

### Ejemplo de salida

```
Bienvenido al sistema de Farmacia Turno de Invierno

Ingrese receta a revisar: receta_2

Medicamentos solicitados: 6
Códigos válidos solicitados: 5
Medicamentos entregados: 4
Medicamentos no disponibles: 1
Códigos inválidos: 1

Lista de entregados: [101, 109, 205, 399]
Lista de no disponibles: [109]
Lista de inválidos: [410]

Grupo más entregado: analgesico
Estado: Receta incompleta

¿Desea revisar otra receta? (Si - No): no
Sistema finalizado
```

---

## 🚗 Ejercicio 2 — Control de estacionamiento de un centro médico

Un centro médico registra entrada y salida de vehículos. El sistema debe calcular cobros, detectar estadías excesivas, ordenar registros y mostrar morosos.

### Tipos de vehículos y tarifas

| Tipo | Cobro |
|---|---|
| `paciente` | Tarifa completa |
| `funcionario` | 50% de descuento |
| `emergencia` | $0 (no paga, pero se registra) |

### Tarifa base

- **$1.000** por cada 30 minutos o fracción.
- Si permanece **más de 180 minutos** → multa fija de **$5.000 adicionales**.

### Ejemplo de cálculo

```
Minutos: 115 → fracciones de 30: ceil(115/30) = 4 → $4.000 base
115 ≤ 180 → sin multa
Tipo paciente → cobro final: $4.000

Minutos: 515 → ceil(515/30) = 18 → $18.000 base
515 > 180 → +$5.000 multa
Tipo funcionario → (18.000 + 5.000) * 0.5 = $11.500
```

### Formato de archivos

**`estacionamiento.txt`** — separado por `;`:
```
patente;tipo;hora_entrada;hora_salida;fecha
AA*BB*10;paciente;08:10;10:05;15-01-2026
CC*DD*20;funcionario;07:40;16:15;15-01-2026
EE*FF*30;emergencia;09:00;09:50;15-01-2026
```

**`pagos.txt`** — separado por `;`:
```
patente;estado
AA*BB*10;PAGADO
CC*DD*20;PAGADO
II*JJ*50;PENDIENTE
```
> Los vehículos de emergencia **no aparecen** en `pagos.txt`.

### Menú del programa

```
MENÚ - Control de estacionamiento
1. Mostrar los 5 vehículos con mayor tiempo de permanencia
2. Mostrar promedios y porcentajes por tipo de vehículo
3. Ordenar registros por mes
4. Buscar una patente
5. Mostrar morosos
6. Cerrar programa
```

> ⚠️ **No usar `sort()` ni `sorted()`** — ordenar manualmente con ciclos.

### Detalle de cada opción

**Opción 1 — Top 5 permanencia:**
Mostrar las 5 patentes con más minutos, con tipo y cobro.

**Opción 2 — Promedios y porcentajes:**
- Promedio de permanencia de pacientes y funcionarios.
- Porcentaje de pacientes/funcionarios con más de 180 minutos.
- Total no cobrado por vehículos de emergencia.

**Opción 3 — Ordenar por mes:**
Extraer mes desde la fecha (`fecha.split("-")[1]`) y ordenar de enero a diciembre.

**Opción 4 — Buscar patente:**
Mostrar: posición en archivo, tipo, minutos, cobro y turno de entrada:
- **Mañana:** 07:01 – 12:00
- **Tarde:** 12:01 – 21:00
- **Noche:** 21:01 – 07:00

**Opción 5 — Morosos:**
- Lista de patentes con estado `PENDIENTE`.
- Monto total pendiente.
- Porcentaje recaudado respecto al total.
- Patente con mayor deuda.

**Opción 6 — Cerrar:**
Mostrar resumen final: total vehículos, vehículos cobrables, recaudación efectiva y monto pendiente.

### Ejemplo de salida (opción 4)

```
Ingrese patente a buscar: AA*BB*10

Patente encontrada
Posición dentro del archivo: 1
Tipo de vehículo: paciente
Minutos de permanencia: 115
Cobro asociado: $ 4000
Momento de entrada: Mañana
```

---

## 🔐 Ejercicio 3 — Mensaje secreto con listas

Un ayudante dejó un mensaje codificado. Cada número en `codigo` es un índice de `abecedario`.

```python
abecedario = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
              "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
              "t", "u", "v", "w", "x", "y", "z"]

codigo = [6, 5, 12, 9, 3, 9, 4, 1, 4, 5, 19, 0,
          22, 1, 19, 0, 2, 9, 5, 14, 0, 5, 14, 3,
          1, 13, 9, 14, 1, 4, 15]
```

**Restricciones:**
- No puedes escribir el mensaje directamente en un `print`.
- Debes usar obligatoriamente: `listas`, `for`, `append` o concatenación, índices, `len`, `print`.

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `lista.append(x)` | Agrega `x` al final de la lista |
| `lista.pop(i)` | Elimina y retorna el elemento en posición `i` |
| `lista.index(x)` | Retorna el índice de la primera ocurrencia de `x` |
| `x in lista` | Verifica si `x` está en la lista (`True`/`False`) |
| `len(lista)` | Cantidad de elementos de la lista |
| `lista[i]` | Accede al elemento en posición `i` |
| Ordenamiento manual | Ciclos anidados para ordenar sin `sort()`/`sorted()` |
| `ceil(n/30)` vía `//` y `%` | Calcular fracciones de 30 minutos sin `math.ceil` |
| `fecha.split("-")[1]` | Extraer el mes desde una fecha `DD-MM-YYYY` |
| `hora.split(":")[0]` | Extraer la hora desde un string `HH:MM` |

