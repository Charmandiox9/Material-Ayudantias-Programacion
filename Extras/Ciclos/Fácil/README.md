# Compilado de Ejercicios: Estructuras de Repetición (Ciclos) Básicos

## Ejercicio 1: Transmisión de Paquetes
### Conteo de Envío en CodeVerse
**Contexto:**
El motor de red necesita simular el envío secuencial de paquetes de datos hacia el servidor de juegos.

**Historia:**
Martín está depurando la conexión entre el cliente y el servidor en Godot 4. Para verificar que los paquetes lleguen en orden, necesita un script que imprima el número de cada paquete enviado, desde el 1 hasta la cantidad total que el usuario indique.

**Entrada de datos:**
Un número entero que represente la cantidad total de paquetes a enviar.

**Formato:**
`Cantidad de paquetes: [cantidad]`

**Ejemplo:**
`Cantidad de paquetes: 5`

**Requerimientos:**
* Solicitar el número usando `input()` y convertirlo a entero.
* Utilizar un ciclo `for` con `range()` para iterar.
* Imprimir el número de paquete actual en cada iteración.

**Ejemplo de Salida por pantalla:**
```text
Iniciando transmisión...
Enviando paquete #1
Enviando paquete #2
Enviando paquete #3
Enviando paquete #4
Enviando paquete #5
Transmisión completada.
```

---

## Ejercicio 2: Meta de Ahorro
### Acumulador de Saldo en Medisystem
**Contexto:**
El sistema de finanzas personal de la clínica requiere sumar aportes diarios hasta alcanzar una meta específica de inversión.

**Historia:**
Para comprar un nuevo escáner de resonancia, la administración de Medisystem ha decidido registrar depósitos diarios. El programa debe pedir el monto de cada depósito y sumarlo a un total. El proceso se detiene cuando el total ahorrado sea mayor o igual a la meta establecida de $1000.

**Entrada de datos:**
Múltiples montos decimales ingresados por consola uno a uno.

**Formato:**
`Ingrese monto del depósito: [monto]`

**Requerimientos:**
* Inicializar una variable `total` en 0.
* Usar un ciclo `while` que continúe mientras `total < 1000`.
* En cada iteración, solicitar un nuevo monto y sumarlo al `total`.
* Al finalizar, mostrar el saldo total obtenido.

**Ejemplo de Salida por pantalla:**
```text
Meta: $1000
Ingrese monto del depósito: 400
Saldo actual: $400.0
Ingrese monto del depósito: 350
Saldo actual: $750.0
Ingrese monto del depósito: 300
Saldo actual: $1050.0
¡Meta alcanzada! Saldo final: $1050.0
```

---

## Ejercicio 3: Reintento de Conexión
### Validación de Credenciales en la Terminal
**Contexto:**
Se requiere que un usuario ingrese una palabra clave específica para desbloquear el acceso a la terminal de administración.

**Historia:**
Don Tito necesita un filtro de seguridad simple. El script debe pedir repetidamente la "Palabra Secreta". Si el usuario ingresa algo distinto a "python123", el programa debe decir "Acceso Denegado" y volver a preguntar. Solo se detiene cuando la palabra sea correcta.

**Entrada de datos:**
Cadenas de texto ingresadas por el usuario.

**Formato:**
`Palabra Secreta: [texto]`

**Requerimientos:**
* Usar un ciclo `while` para repetir la solicitud.
* Comparar el texto ingresado con la cadena `"python123"`.
* Mostrar un mensaje de éxito al salir del bucle.

**Ejemplo de Salida por pantalla:**
```text
Palabra Secreta: hola
Acceso Denegado.
Palabra Secreta: admin
Acceso Denegado.
Palabra Secreta: python123
Acceso Concedido. Bienvenido al sistema.
```
