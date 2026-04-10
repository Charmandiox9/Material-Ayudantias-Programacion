# Compilado de Ejercicios: Lectura de Archivos (Nivel Fácil)

## Ejercicio 1: Diario de Marte
### Conteo de Menciones del Día Solar
**Contexto:**
El comando de control en la Tierra ha recibido un archivo de texto con las notas de campo del astronauta en Marte. Para medir el avance de la misión, se necesita contar cuántas entradas (líneas) tiene el diario y cuántas veces se menciona la palabra "SOL".

**Historia:**
El archivo `diario_marte.txt` contiene notas diarias. Cada línea corresponde a una entrada. Tu tarea es abrir el archivo, leerlo línea por línea y reportar las estadísticas básicas para el equipo de control.

**Archivo de entrada (`diario_marte.txt`):**
```text
SOL 1: Llegada exitosa al cráter Jezero.
SOL 2: Recolección de muestras de suelo.
El clima hoy fue frío, pero el SOL 3 brilló.
SOL 4: Fallo en el sensor de humedad.
Revisión de paneles solares durante el SOL 5.
```

**Requerimientos:**
* Abrir el archivo `diario_marte.txt` en modo lectura.
* Contar el total de líneas (entradas).
* Contar cuántas veces aparece la palabra "SOL"
* Cerrar el archivo al finalizar.

**Ejemplo de Salida por pantalla:**
```text
Leyendo diario marciano...
Total de entradas registradas: 5
Menciones de la palabra 'SOL': 5
Análisis de misión completado.
```

---

## Ejercicio 2: Inventario de Oxígeno
### Verificación de Tanques Disponibles
**Contexto:**
En la estación espacial, los tanques de oxígeno se registran en un archivo. Cada línea contiene el ID del tanque y su porcentaje de carga.

**Historia:**
El sistema de soporte vital necesita saber cuántos tanques tienen menos del 20% de carga para solicitar una recarga inmediata.

**Archivo de entrada (`oxigeno.txt`):**
```text
T-001,85.5
T-002,12.0
T-003,90.2
T-004,15.7
T-005,45.0
```

**Requerimientos:**
* Leer el archivo línea por línea usando `.strip()` y `.split(",")`.
* Convertir el porcentaje a `float`.
* Si la carga es menor a 20.0, mostrar un mensaje de "ALERTA: Tanque [ID] bajo".
* Mostrar el total de tanques en estado crítico al final.

**Ejemplo de Salida por pantalla:**
```text
Verificando niveles de oxígeno...
ALERTA: Tanque T-002 bajo (12.0%)
ALERTA: Tanque T-004 bajo (15.7%)
Total tanques críticos encontrados: 2
```

---

## Ejercicio 3: Bitácora de Radio
### Limpieza de Ruido en Señales
**Contexto:**
Un radiotelescopio capta señales del espacio profundo. Muchas líneas en el archivo son "ruido" representado por puntos suspensivos o líneas en blanco.

**Historia:**
Se requiere un programa que lea el archivo `senales.txt` y solo imprima las líneas que contengan caracteres válidos (letras o números), ignorando las líneas que solo tienen puntos o están vacías.

**Archivo de entrada (`senales.txt`):**
```text
.....
MENSAJE RECIBIDO
.....
......
COORDENADAS_SET_01
.....
```

**Requerimientos:**
* Leer todas las líneas.
* Usar un condicional para verificar si la línea es distinta de `.....` y no está vacía tras usar `.strip()`.
* Imprimir solo los mensajes útiles.

**Ejemplo de Salida por pantalla:**
```text
--- MENSAJES DECODIFICADOS ---
MENSAJE RECIBIDO
COORDENADAS_SET_01
------------------------------
```
