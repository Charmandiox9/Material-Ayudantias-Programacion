# Compilado de Ejercicios: Subprogramas y Funciones (Nivel Fácil)

## Ejercicio 1: Cálculo de Daño Crítico
### Lógica de Combate en CodeVerse
**Contexto:**
En el desarrollo de un videojuego, es crucial separar la lógica de cálculo del daño de la visualización en pantalla.

**Historia:**
Martín necesita una función llamada `calcular_danio` que reciba dos parámetros: `base` (daño base del arma) y `critico` (un valor booleano). Si `critico` es `True`, el daño se duplica. La función debe **retornar** el daño final.

**Requerimientos:**
* Definir la función `calcular_danio(base, es_critico)`.
* Retornar `base * 2` si es crítico, de lo contrario retornar `base`.
* En el programa principal, solicitar los datos al usuario y llamar a la función.
* Mostrar el resultado con un mensaje descriptivo.

**Ejemplo de Salida por pantalla:**
```text
Ataque base: 50
¿Fue crítico? (S/N): S
El daño total infligido es: 100.0
```

---

## Ejercicio 2: Conversor de Peso Médico
### Recetas de Medisystem
**Contexto:**
Algunos equipos médicos antiguos en la clínica entregan el peso en libras, pero el sistema central requiere kilos.

**Historia:**
Se necesita una función `libras_a_kilos` que reciba el peso en libras y retorne el valor convertido a kilogramos (1 libra = 0.453 kg).

**Requerimientos:**
* Definir la función `libras_a_kilos(peso_lb)`.
* Usar la constante de conversión `0.453`.
* Retornar el valor calculado.
* Solicitar el peso en libras por consola y mostrar el resultado en kilos con 2 decimales.

**Ejemplo de Salida por pantalla:**
```text
Ingrese peso en libras: 150
Peso equivalente: 67.95 kg
```

---

## Ejercicio 3: Panel de Control de Don Tito
### Procedimiento de Menú y Validación
**Contexto:**
Don Tito quiere estandarizar cómo se muestran las opciones en su terminal para que todos sus scripts se vean iguales.

**Historia:**
Crea un procedimiento llamado `mostrar_menu()` que imprima 3 opciones (1. Escanear, 2. Limpiar, 3. Salir). Luego, crea una función `validar_opcion(opc)` que reciba la opción ingresada y retorne `True` si es válida (1, 2 o 3) o `False` si no lo es.

**Requerimientos:**
* Definir el procedimiento `mostrar_menu()`.
* Definir la función `validar_opcion(opc)`.
* El programa principal debe llamar al menú, pedir la opción y usar la función para decir si el acceso fue correcto o si la opción es inválida.

**Ejemplo de Salida por pantalla:**
```text
--- PANEL DE CONTROL ---
1. Escanear sistema
2. Limpiar registros
3. Salir
------------------------
Seleccione una opción: 5
Opción inválida. Reintente.
```
