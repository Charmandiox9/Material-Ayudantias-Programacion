# 🚀 Ayudantía 4 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: funciones (`def`), procedimientos, parámetros y retorno, lectura de archivos con `open()` + `readline()` + `.split()`, ciclos `while` y `for`, acumuladores y validación.

---

## 🛸 Ejercicio 1 — Sistema de comunicación Artemis II

La NASA necesita un sistema para informar a la tripulación el estado de los módulos de la nave Artemis II. El énfasis está en usar **funciones** para evitar repetir código.

**Estados posibles de un módulo:**

| Estado | Mensaje |
|---|---|
| Operativo | `"todo funcionando correctamente."` |
| En revisión | `"requiere supervisión técnica."` |
| Crítico | `"atención inmediata requerida."` |

**Requerimientos**

1. **Menú**
   - Mostrar `"Bienvenido! ¿Qué módulo desea chequear?"`
   - Opciones: `1) Propulsión` · `2) Navegación` · `3) Soporte vital`
   - Pedir opción por consola.
   - Aceptar `"fin"` para terminar el programa.

2. **Informe de estado del módulo**
   - Solicitar el estado del módulo seleccionado.
   - Mostrar mensaje según estado.
   - Formato de salida: `"Módulo de {nombre}: {mensaje}"`

3. **Consideraciones**
   - El programa se ejecuta en bucle hasta que el usuario ingrese `"fin"`.
   - Validar que la opción ingresada sea válida; si no, pedirla nuevamente.
   - Separar el problema en funciones:
     - Función para desplegar el menú.
     - Función para obtener el mensaje asociado al estado.
     - Función para mostrar el mensaje final.

**Ejemplo de salida**
```
Bienvenido! ¿Qué módulo desea chequear?
1) Propulsión.
2) Navegación.
3) Soporte vital.
Ingrese una opción ('fin' para salir): propulsión
Ingrese el estado del módulo: operativo

Enviando mensaje...
Módulo de propulsión: todo funcionando correctamente.

==============================

¿Desea chequear otro módulo?
1) Propulsión.
2) Navegación.
3) Soporte vital.
Ingrese una opción ('fin' para salir): navegación
Ingrese el estado del módulo: en revisión

Enviando mensaje...
Módulo de navegación: requiere supervisión técnica.

==============================

¿Desea chequear otro módulo?
...
Ingrese una opción ('fin' para salir): fin
Saliendo del programa...
```


---

## 🔐 Ejercicio 2 — Escape Room

Administras un emprendimiento de Escape Rooms y quieres estadísticas sobre el desempeño de tus jugadores. Los datos están en `escape_room.txt`.

**Formato del archivo `escape_room.txt`:**
```
pieza,dificultad,jugador,edad,pistas_usadas,puzzles_resueltos,tiempo_salida
```

**Columnas:**

| Columna | Descripción |
|---|---|
| `pieza` | Nombre del escape room |
| `dificultad` | `fácil`, `intermedio` o `difícil` |
| `jugador` | Nombre del participante |
| `edad` | Edad del jugador |
| `pistas_usadas` | Pistas solicitadas durante la partida |
| `puzzles_resueltos` | Puzzles completados |
| `tiempo_salida` | Segundos para completar la sala (`-1` si no logró salir) |

**Requerimientos**

1. Nombre y edad de los jugadores que **no** lograron completar el escape room (`tiempo_salida == -1`).
2. El jugador **más rápido** en completar un escape room (solo registros con `tiempo_salida != -1`).
3. El **tiempo promedio** de salida para cada nivel de dificultad (solo completados).
4. **Total de pistas** utilizadas en la pieza `"Laboratorio X"`.

**Consideraciones**
- Para los puntos 2 y 3, ignorar registros con `tiempo_salida == -1`.
- Crear una función que solicite el nombre del archivo y lo abra.
- Usar funciones para calcular promedios y mostrarlos.
- Usar `round(promedio)` para redondear.

**Ejemplo de salida**
```
Ingrese el nombre del archivo: escape_room.txt

1) Jugadores que no lograron salir del Escape Room:
- Tomas (23)
- Camila (21)
- Antonia (20)
- Martina (21)
- Agustin (25)
- Paula (26)

2) Ignacia fue el/la jugador/a más rápido/a, demorando 2300 segundos.

3) Promedios:
Promedio de tiempo de dificultad Facil: 2533 segundos
Promedio de tiempo de dificultad Intermedio: 3233 segundos
Promedio de tiempo de dificultad Dificil: 3075 segundos

4) Pistas utilizadas en Laboratorio X: 15
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `def nombre():` | Define un subprograma (función o procedimiento) |
| Función | Subprograma que **retorna** un valor con `return` |
| Procedimiento | Subprograma que **no retorna** valor — solo ejecuta acciones |
| Parámetros | Variables que recibe el subprograma al ser llamado |
| `return` | Entrega el resultado al código que llamó la función |
| `while True` + `break` | Patrón para menús que se repiten hasta condición de salida |
| `tiempo == -1` | Bandera para indicar "no completó" en el escape room |
| `round(val)` | Redondea al entero más cercano (sin decimales) |
