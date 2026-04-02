# Compilado de Ejercicios: Estructuras Condicionales Intermedias

## Ejercicio 1: Triaje de Pacientes
### Clasificación de Edad en Medisystem
**Contexto:**
El módulo de atención de Medisystem requiere clasificar a los pacientes ingresados manualmente en recepción para derivarlos al especialista correcto.

**Historia:**
Al diseñar la lógica del sistema médico, el equipo notó que la vista principal necesita mostrar la categoría del paciente basada en su edad. El recepcionista ingresará el ID y la edad del paciente en la terminal.

**Entrada de datos:**
Dos solicitudes por consola: una para el ID (texto) y otra para la edad (entero).

**Formato:**
`ID del paciente: [id_paciente]`
`Edad del paciente: [edad]`

**Ejemplo:**
`ID del paciente: PT-9942`
`Edad del paciente: 15`

**Requerimientos:**
* Capturar ambas entradas con `input()`.
* Usar `if`, `elif` y `else` para clasificar:
  * Menor de 13: Pediatría.
  * 13 a 17: Medicina Adolescente.
  * 18 a 64: Medicina General.
  * 65 o más: Geriatría.

**Ejemplo de Salida por pantalla:**
`Paciente PT-9942 derivado a: Medicina Adolescente.`

---

## Ejercicio 2: Asignación de Recursos
### Facturación de Nodos en PROJEIC
**Contexto:**
El sistema de gestión de proyectos debe calcular el descuento aplicable preguntando por consola la cantidad de horas de servidor contratadas.

**Historia:**
PROJEIC ofrece servidores virtuales para alojar entornos de desarrollo. Para incentivar el uso continuo, se aplican descuentos automáticos según las horas facturadas al mes. El administrador ingresará las horas en la terminal para calcular la factura de un cliente.

**Entrada de datos:**
El programa solicitará el total de horas consumidas mediante consola.

**Formato:**
`Horas consumidas este mes: [horas]`

**Ejemplo:**
`Horas consumidas este mes: 120`

**Requerimientos:**
* Capturar las horas con `input()`.
* Costo base: $2 por hora.
* Aplicar descuentos con `elif`:
  * Menos de 50 horas: 0%.
  * 50 a 100 horas: 10%.
  * Más de 100 horas: 20%.
* Calcular y mostrar el precio total final.

**Ejemplo de Salida por pantalla:**
`Horas: 120 | Descuento: 20% | Total a pagar: $192.0`

---

## Ejercicio 3: Calculadora de Nodos
### Operaciones de Punteros Simuladas
**Contexto:**
Simular el comportamiento de desplazamiento en una estructura de datos personalizada interactuando a través de la consola.

**Historia:**
Mientras repasa conceptos de estructuras de datos (como listas enlazadas), se necesita un pequeño script interactivo en Python que pregunte la posición actual y la acción a tomar (como SIGUIENTE o ANTERIOR) para mover un índice.

**Entrada de datos:**
Dos inputs por consola: la posición numérica y el comando en texto.

**Formato:**
`Posición actual: [posicion]`
`Comando a ejecutar: [comando]`

**Ejemplo:**
`Posición actual: 5`
`Comando a ejecutar: ANTERIOR`

**Requerimientos:**
* Solicitar ambos datos usando `input()`.
* Modificar la posición según el comando usando `elif`.
* SIGUIENTE suma 1, ANTERIOR resta 1, INICIO vuelve a 0, FIN va a 99.
* Evitar que la posición resultante sea menor a 0.

**Ejemplo de Salida por pantalla:**
`Comando ANTERIOR ejecutado. Nueva posición: 4.`