# Compilado de Ejercicios: Estructuras de Repetición (Ciclos) Intermedios

## Ejercicio 1: Escaneo de Suministros
### Filtrado de Recursos Especiales
**Contexto:**
Un dron de exploración en CodeVerse escanea una serie de contenedores numerados y solo debe recoger aquellos que tengan un identificador par.

**Historia:**
Martín necesita que su dron recoja suministros de energía. El dron pasará por una secuencia de contenedores (del 1 al número que el usuario indique). El programa debe mostrar el número de cada contenedor, pero solo marcar como "RECOGIDO" aquellos cuyo número sea par.

**Entrada de datos:**
Un número entero que represente el total de contenedores a escanear.

**Formato:**
`Total de contenedores: [cantidad]`

**Requerimientos:**
* Solicitar el número total de contenedores.
* Usar un ciclo `for` con `range()`.
* Dentro del ciclo, usar un condicional `if-else`.
* Si el número es par, imprimir "Contenedor #[n]: RECOGIDO".
* Si es impar, imprimir "Contenedor #[n]: Ignorado".

**Ejemplo de Salida por pantalla:**
```text
Total de contenedores: 4
Contenedor #1: Ignorado
Contenedor #2: RECOGIDO
Contenedor #3: Ignorado
Contenedor #4: RECOGIDO
Escaneo finalizado.
```

---

## Ejercicio 2: Sistema de Despacho de Medicamentos
### Gestión de Stock con Salida Manual
**Contexto:**
El sistema de farmacia de Medisystem permite entregar cajas de insumos una por una hasta que se agote el stock o el encargado cierre el turno.

**Historia:**
Se requiere un script que maneje el stock de "Mascarillas". El programa comienza con 10 unidades. En cada paso, pregunta al usuario si desea "ENTREGAR" una caja o "SALIR". Si entrega, el stock baja. Si el stock llega a 0, el programa termina automáticamente.

**Entrada de datos:**
Comandos de texto ("ENTREGAR" o "SALIR").

**Requerimientos:**
* Iniciar `stock = 10`.
* Usar un ciclo `while` que dependa tanto del stock como de la entrada del usuario.
* Usar `break` para salir si el usuario escribe "SALIR".
* Mostrar el stock restante después de cada entrega.

**Ejemplo de Salida por pantalla:**
```text
Stock inicial: 10 unidades.
¿Qué desea hacer? (ENTREGAR/SALIR): ENTREGAR
Entregando... Stock restante: 9
¿Qué desea hacer? (ENTREGAR/SALIR): ENTREGAR
Entregando... Stock restante: 8
¿Qué desea hacer? (ENTREGAR/SALIR): SALIR
Cierre de turno. Stock final: 8
```

---

## Ejercicio 3: Analizador de Sensores IoT
### Promedio de Lecturas con Centinela
**Contexto:**
Un sensor de temperatura envía lecturas constantes. Para detener la recolección de datos y obtener estadísticas, se envía un valor de control.

**Historia:**
Don Tito necesita calcular la temperatura promedio de un rack de servidores. El script pedirá temperaturas una por una. Para dejar de ingresar datos, el usuario debe ingresar el número `0`. Al final, el programa debe mostrar cuántas lecturas se hicieron y cuál fue el promedio.

**Entrada de datos:**
Números decimales (temperaturas). El número `0` actúa como señal de fin.

**Requerimientos:**
* Usar un ciclo `while`.
* Acumular la suma de las temperaturas y contar cuántas se ingresaron.
* No incluir el `0` en el promedio ni en el conteo.
* Si no se ingresaron datos (el primer valor fue 0), mostrar un mensaje de error.
* Usar f-strings para mostrar el promedio con 2 decimales.

**Ejemplo de Salida por pantalla:**
```text
Ingrese temperatura (0 para finalizar): 25.5
Ingrese temperatura (0 para finalizar): 30.2
Ingrese temperatura (0 para finalizar): 28.4
Ingrese temperatura (0 para finalizar): 0

Lecturas realizadas: 3
Promedio de temperatura: 28.03°C
```
