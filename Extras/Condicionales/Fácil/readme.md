# Compilado de Ejercicios: Estructuras Condicionales Básicas

## Ejercicio 1: Daño Crítico
### Verificación de Paridad en CodeVerse
**Contexto:**
El motor de físicas necesita determinar si un ataque genera daño crítico o normal basado en el número de combo ingresado por teclado.

**Historia:**
Durante el desarrollo del videojuego CodeVerse en Godot 4, Martín necesita implementar una lógica en el script de combate. Si el número de combo ingresado por el jugador es par, el ataque será un "Crítico". Si es impar, será un "Ataque Normal". 

**Entrada de datos:**
El programa debe solicitar un número entero por consola.

**Formato:**
`Ingrese el numero de combo: [numero]`

**Ejemplo:**
`Ingrese el numero de combo: 14`

**Requerimientos:**
* Solicitar el número usando `input()` y convertirlo a entero.
* Utilizar la operación módulo (`%`) y un condicional `if-else` para determinar la paridad.
* Imprimir el tipo de ataque resultante.

**Ejemplo de Salida por pantalla:**
`El combo 14 genera un Ataque Crítico.`

---

## Ejercicio 2: Acceso a la Consola
### Validación de Edad para Servidores
**Contexto:**
Se requiere restringir el acceso a la terminal de administración de un servidor de pruebas pidiendo la edad al momento de ejecutar el script.

**Historia:**
Para evitar que usuarios no autorizados modifiquen los contenedores de Podman, se ha establecido que solo el personal mayor de edad pueda ejecutar comandos. Don Tito te pide un script en Python que actúe como filtro inicial, solicitando la edad por consola antes de pedir la contraseña.

**Entrada de datos:**
Una solicitud por consola pidiendo la edad del usuario.

**Formato:**
`Ingrese su edad: [edad]`

**Ejemplo:**
`Ingrese su edad: 17`

**Requerimientos:**
* Capturar el valor con `input()` y convertirlo a entero.
* Usar `if-else` para verificar si la edad es mayor o igual a 18.
* Mostrar un mensaje de acceso concedido o denegado.

**Ejemplo de Salida por pantalla:**
`Acceso Denegado: El usuario es menor de edad.`

---

## Ejercicio 3: Estado del Sensor
### Monitoreo IoT de Temperatura
**Contexto:**
Un simulador de microcontrolador ESP32 requiere que ingreses manualmente la temperatura para probar las alertas de sobrecalentamiento.

**Historia:**
En un proyecto de IoT, se están calibrando las alertas de temperatura de la placa principal. El script pedirá la temperatura actual. Si la temperatura supera los 45 grados, el sistema debe marcar el estado como "Peligro". Si es 45 o menos, el estado es "Estable".

**Entrada de datos:**
El programa pedirá ingresar un valor decimal por consola.

**Formato:**
`Temperatura actual (C): [temperatura]`

**Ejemplo:**
`Temperatura actual (C): 48.5`

**Requerimientos:**
* Leer el valor con `input()` y convertirlo a `float`.
* Validar la temperatura con un condicional simple `if-else`.

**Ejemplo de Salida por pantalla:**
`Alerta: Estado en Peligro por alta temperatura (48.5°C).`