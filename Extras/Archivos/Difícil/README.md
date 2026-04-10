# Compilado de Ejercicios: Lectura de Archivos (Nivel Difícil)

## Ejercicio 1: Monitor de Calidad del Aire
### Análisis de CO2 y Alertas de Salud
**Contexto:**
Una estación meteorológica registra los niveles de CO2 (partes por millón) cada hora en un archivo llamado `calidad_aire.txt`.

**Historia:**
Se necesita un reporte detallado. El programa debe leer el archivo, que tiene el formato `HORA,CO2`, e informar:
1. El nivel máximo de CO2 detectado y a qué hora ocurrió.
2. El promedio diario de CO2.
3. Si el promedio supera los 400 ppm, mostrar un mensaje de "ALERTA DE CONTAMINACIÓN".

**Archivo de entrada (`calidad_aire.txt`):**
```text
08:00,350
09:00,380
10:00,420
11:00,450
12:00,410
13:00,390
```

**Requerimientos:**
* Leer el archivo una sola vez.
* Usar variables para rastrear el valor máximo y su hora correspondiente.
* Realizar los cálculos matemáticos con f-strings (2 decimales).

---

## Ejercicio 2: Explorador de Catálogo Musical
### Filtrado y Recomendación de Artistas
**Contexto:**
Tienes una base de datos de canciones en `catalogo.txt` con el formato: `ARTISTA;CANCION;DURACION_SEG;POPULARIDAD(1-100)`.

**Historia:**
El usuario debe ingresar el nombre de un artista por consola. El programa buscará en el archivo todas las canciones de ese artista y mostrará:
1. Una lista de sus canciones.
2. La duración total de todas sus canciones en minutos y segundos.
3. Cuál es su canción más popular.

**Archivo de entrada (`catalogo.txt`):**
```text
Daft Punk;Get Lucky;248;95
Queen;Bohemian Rhapsody;354;99
Daft Punk;One More Time;320;92
Queen;Don't Stop Me Now;210;96
Imagine Dragons;Believer;204;88
```

**Requerimientos:**
* Solicitar el nombre del artista por `input()`.
* Usar `.split(";")` para separar los 4 datos de cada línea.
* Convertir duraciones y popularidad a enteros.
* Manejar el caso donde el artista no exista en el archivo.

---

## Ejercicio 3: Detector de Críticas en la App Store
### Análisis de Sentimiento Básico
**Contexto:**
Los desarrolladores de una App reciben comentarios de usuarios en `comentarios.txt`.

**Historia:**
Para priorizar el trabajo, necesitan un script que analice los comentarios. Si un comentario contiene las palabras "error", "malo" o "lento", se clasifica como **Negativo**. Si no, es **Positivo**. Al final, el programa debe mostrar el porcentaje de comentarios negativos sobre el total.

**Archivo de entrada (`comentarios.txt`):**
```text
La app es genial pero un poco lenta a veces.
Me encanta el diseño, muy rapida.
Hay un error al iniciar sesion, arreglenlo.
Muy mal servicio, no funciona.
Excelente aplicacion, la mejor.
```

**Requerimientos:**
* Leer cada comentario.
* Convertir el texto a minúsculas (`.lower()`) para facilitar la búsqueda.
* Calcular el porcentaje: `(negativos / total) * 100`.

**Ejemplo de Salida por pantalla:**
```text
Analizando 5 comentarios...
[Negativo] La app es genial pero un poco lenta a veces.
[Positivo] Me encanta el diseño, muy rapida.
[Negativo] Hay un error al iniciar sesion, arreglenlo.
[Negativo] Muy mal servicio, no funciona.
[Positivo] Excelente aplicacion, la mejor.

--- RESULTADOS ---
Total comentarios: 5
Comentarios Negativos: 3
Índice de insatisfacción: 60.0%
```
