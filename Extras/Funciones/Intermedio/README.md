# Compilado de Ejercicios: Subprogramas y Funciones (Nivel Intermedio)

## Ejercicio 1: Estación de Carga de Drones
### Gestión de Energía en CodeVerse
**Contexto:**
Los drones de exploración necesitan recargar sus baterías en diferentes tipos de estaciones distribuidas por el mapa.

**Historia:**
Martín necesita una función `calcular_recarga(tiempo, tipo_estacion)` que determine cuánta energía se recupera.
* "Solar": 5 unidades por minuto.
* "Electrica": 15 unidades por minuto.
* "Termica": 8 unidades por minuto.
* Cualquier otro tipo: 1 unidad por minuto.

**Requerimientos:**
* La función debe retornar el total de energía (float).
* Usar `if/elif/else` dentro de la función.
* En el programa principal, preguntar el tiempo de carga y el tipo.
* Mostrar el resultado final usando f-strings.

**Ejemplo de Salida por pantalla:**
```text
Minutos en la estación: 10
Tipo de estación: Electrica
Energía recuperada: 150.0 unidades.
```

---

## Ejercicio 2: Clasificador de Signos Vitales
### Módulo de Triaje en Medisystem
**Contexto:**
El sistema de urgencias de la clínica necesita automatizar la clasificación de pacientes basada en su frecuencia cardíaca (pulso).

**Historia:**
Crea una función `clasificar_pulso(latidos)` que retorne un texto con el estado del paciente:
* Menos de 60: "Bradicardia" (Bajo).
* 60 a 100: "Normal".
* Más de 100: "Taquicardia" (Alto).

Además, crea un procedimiento `mostrar_alerta(nombre, estado)` que imprima el nombre del paciente y su clasificación de forma llamativa si el estado no es "Normal".

**Requerimientos:**
* Definir la función y el procedimiento.
* El programa principal debe pedir el nombre y el pulso, obtener el estado con la función y luego usar el procedimiento para mostrar la alerta.

**Ejemplo de Salida por pantalla:**
```text
Nombre del paciente: Ana
Pulso (latidos/min): 120

[ALERTA] El paciente Ana presenta: Taquicardia
```

---

## Ejercicio 3: Calculadora de Aduanas
### Importaciones en la Terminal de Don Tito
**Contexto:**
Don Tito está importando componentes de hardware y necesita un script para calcular el costo total incluyendo impuestos.

**Historia:**
Se requieren dos funciones:
1. `obtener_impuesto(pais)`: Retorna 0.05 si es "China", 0.15 si es "USA", y 0.20 para el resto.
2. `calcular_costo_total(precio_base, pais)`: Esta función debe llamar a `obtener_impuesto` para conseguir el porcentaje, calcular el monto del impuesto y retornar el precio final (`base + impuesto`).

**Requerimientos:**
* Uso de composición de funciones (una llama a la otra).
* Retornar valores numéricos.
* Mostrar el desglose: Precio Base, Impuesto aplicado y Total.

**Ejemplo de Salida por pantalla:**
```text
Precio del producto: 100
País de origen: USA

--- DESGLOSE DE IMPORTACIÓN ---
Precio Base: $100.00
Impuesto (15%): $15.00
Total a Pagar: $115.00
```
