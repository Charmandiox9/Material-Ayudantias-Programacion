# Compilado de Ejercicios: Estructuras Condicionales Complejas

## Ejercicio 1: Validación de Malla de Colisión
### Detección de Triángulos en Motores Gráficos
**Contexto:**
Verificación matemática de vértices leyendo coordenadas exportadas en un archivo para la generación de terreno en 3D.

**Historia:**
Al exportar modelos para un entorno interactivo, el motor necesita leer un log del sistema para confirmar que tres distancias dadas pueden formar un polígono cerrado (un triángulo válido) antes de renderizar la malla de colisión. Si es válido, debe clasificar qué tipo de polígono es.

**Formato del archivo txt:**
Las longitudes de los tres lados separadas por comas en una única línea.

**Formato:**
`lado_a,lado_b,lado_c`

**Ejemplo:**
`5,5,8`

**Requerimientos:**
* Leer los datos desde un archivo de texto.
* Verificar la desigualdad triangular: La suma de dos lados siempre debe ser estrictamente mayor que el tercer lado. Si no lo es, imprimir "Malla Inválida".
* Si es válido, usar `if-elif-else` anidados para clasificarlo en Equilátero, Isósceles o Escaleno.

**Ejemplo de Salida por pantalla:**
`Malla Válida: Generando colisión para polígono Isósceles.`

---

## Ejercicio 2: Pipeline de CI/CD
### Análisis de Logs en Jenkins
**Contexto:**
Un script de validación que lee un reporte automatizado para determinar si un "build" debe ser desplegado a producción basándose en múltiples métricas de calidad.

**Historia:**
El proceso de integración continua con Jenkins evalúa el código de una aplicación NestJS y arroja un archivo `.txt` con los resultados. Para que el código pase a la rama principal, el script debe procesar el archivo y asegurar que cumpla con ciertas métricas de pruebas, con una excepción si es un parche de emergencia.

**Formato del archivo txt:**
Porcentaje de cobertura de código, cantidad de tests fallidos y un booleano (1 o 0) indicando si es un parche de emergencia (`hotfix`), separados por comas.

**Formato:**
`cobertura,tests_fallidos,es_hotfix`

**Ejemplo:**
`75,0,1`

**Requerimientos:**
* Leer y procesar el archivo `.txt`.
* El despliegue se aprueba si: (Cobertura >= 80% `AND` Tests fallidos == 0).
* `OR` si es un parche de emergencia (`es_hotfix == 1`) `AND` Tests fallidos == 0 (sin importar la cobertura).
* Si hay 1 o más tests fallidos, se rechaza inmediatamente bajo cualquier circunstancia.

**Ejemplo de Salida por pantalla:**
`Despliegue Aprobado: Parche de emergencia detectado sin errores en los tests.`

---

## Ejercicio 3: La Máquina de Turing
### Validador de Transiciones de Estado
**Contexto:**
Simulación de las reglas lógicas de una cinta de procesamiento matemático leyendo las instrucciones iniciales desde un archivo de configuración.

**Historia:**
Se está diseñando un simulador lógico para una Máquina de Turing que procesa números unarios. El programa debe cargar el estado actual y el símbolo desde un documento de texto para decidir la próxima acción (escribir un '1', escribir un '0' o detenerse) en su ciclo de evaluación.

**Formato del archivo txt:**
El estado actual (A, B, C) y el símbolo leído de la cinta (0, 1) separados por una coma.

**Formato:**
`estado,simbolo`

**Ejemplo:**
`B,1`

**Requerimientos:**
* Leer los valores iniciales desde un archivo de texto.
* Implementar la siguiente tabla de verdad usando condicionales anidados:
  * Si Estado es A y símbolo es 1 -> Escribir 0, pasar a Estado B.
  * Si Estado es A y símbolo es 0 -> Detener.
  * Si Estado es B y símbolo es 1 -> Escribir 1, pasar a Estado A.
  * Si Estado es B y símbolo es 0 -> Escribir 1, pasar a Estado C.
  * Si Estado es C -> Detener incondicionalmente.

**Ejemplo de Salida por pantalla:**
`Transición: Escribiendo '1' en la cinta. Nuevo estado interno: A.`