# Compilado de Ejercicios: Estructuras de Repetición (Ciclos) Avanzados

## Ejercicio 1: Radar de Coordenadas
### Visualización de Grilla en CodeVerse
**Contexto:**
Para implementar un mini-mapa en la consola, se necesita generar una representación visual de una grilla de coordenadas (X, Y).

**Historia:**
Martín está trabajando en el sistema de posicionamiento. El script debe pedir el tamaño de una grilla cuadrada (por ejemplo, 3x3) y luego imprimir todas las coordenadas. Además, el usuario ingresará su posición actual (X, Y) y el radar deberá marcar ese punto con una `[X]` en lugar de la coordenada normal.

**Entrada de datos:**
1. Tamaño de la grilla (entero).
2. Posición X del jugador (entero).
3. Posición Y del jugador (entero).

**Requerimientos:**
* Usar ciclos `for` anidados (uno para filas `Y` y otro para columnas `X`).
* Si la coordenada actual coincide con la del jugador, imprimir `[X]`.
* De lo contrario, imprimir la coordenada como `(X,Y)`.
* Usar el parámetro `end=" "` en `print()` para mantener la línea.

**Ejemplo de Salida por pantalla:**
```text
Tamaño de la grilla: 3
Tu posición X: 1
Tu posición Y: 0

(0,0) [X]   (2,0) 
(0,1) (1,1) (2,1) 
(0,2) (1,2) (2,2) 
```

---

## Ejercicio 2: Monitor de Triaje Médico
### Estadísticas de Emergencias en Medisystem
**Contexto:**
El área de urgencias necesita procesar una fila de pacientes y generar un reporte de cuántos casos críticos se atendieron antes de cerrar el sistema.

**Historia:**
El script debe solicitar el nombre del paciente y su nivel de gravedad (1 al 5, donde 5 es crítico). El ciclo se repite hasta que el usuario escriba "FIN" en el nombre. Al terminar, el programa debe mostrar:
1. Total de pacientes atendidos.
2. Cuántos fueron "Críticos" (gravedad 4 o 5).
3. El promedio de gravedad de todos los pacientes.

**Entrada de datos:**
Nombres (texto) y Niveles de Gravedad (enteros).

**Requerimientos:**
* Usar `while True` y `break`.
* Validar que la gravedad esté entre 1 y 5 (usar un ciclo interno para re-pedir si es inválida).
* Realizar los cálculos matemáticos al final.

**Ejemplo de Salida por pantalla:**
```text
Nombre del paciente (o FIN): Ana
Gravedad (1-5): 5
Nombre del paciente (o FIN): Luis
Gravedad (1-5): 2
Nombre del paciente (o FIN): FIN

--- REPORTE FINAL ---
Total pacientes: 2
Casos Críticos: 1
Promedio de gravedad: 3.5
```

---

## Ejercicio 3: Proyección de Inversión Tecnológica
### Cálculo de Interés con Bonus en la Terminal
**Contexto:**
Don Tito quiere proyectar cuánto dinero tendrá el fondo de mantenimiento de servidores tras varios años, considerando una tasa de interés anual.

**Historia:**
El usuario ingresa un monto inicial y la cantidad de años a proyectar. Cada año, el monto aumenta un 5% fijo. Sin embargo, si el año es par, se recibe un "Bono de Estabilidad" adicional del 2% sobre el monto de ese año. El programa debe mostrar el saldo año por año.

**Entrada de datos:**
Monto inicial (float) y Años (int).

**Requerimientos:**
* Usar un ciclo `for` con `range(1, años + 1)`.
* Aplicar las fórmulas de aumento porcentual.
* Usar condicionales para detectar años pares (`año % 2 == 0`).
* Mostrar los resultados formateados con f-strings.

**Ejemplo de Salida por pantalla:**
```text
Monto inicial: 1000
Años a proyectar: 3

Año 1: $1050.00
Año 2: $1123.50 (¡Bono par aplicado!)
Año 3: $1179.68
```
