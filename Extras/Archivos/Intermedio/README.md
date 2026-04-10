# Compilado de Ejercicios: Lectura de Archivos (Nivel Intermedio)

## Ejercicio 1: Censo de Biodiversidad
### Monitoreo de Especies en el Amazonas
**Contexto:**
Una ONG ambientalista registra la población de diversas especies en el Amazonas en un archivo llamado `especies.txt`.

**Historia:**
Se requiere un programa que analice los datos para identificar qué especies están en "Estado Crítico" (menos de 500 individuos) y calcule el promedio general de población de todas las especies registradas.

**Archivo de entrada (`especies.txt`):**
```text
Jaguar,1200
Delfin Rosado,450
Guacamayo Azul,300
Oso Hormiguero,800
Tapiro,150
```

**Requerimientos:**
* Leer el archivo línea por línea.
* Separar el nombre de la especie y la población (`split(",")`).
* Listar por pantalla solo las especies con población < 500.
* Mostrar el promedio total de población al final.

**Ejemplo de Salida por pantalla:**
```text
--- ESPECIES EN ESTADO CRÍTICO ---
- Delfin Rosado (450 individuos)
- Guacamayo Azul (300 individuos)
- Tapiro (150 individuos)
----------------------------------
Promedio de población general: 580.0
```

---

## Ejercicio 2: Telemetría de Drones
### Análisis de Rendimiento de Vuelo
**Contexto:**
Una empresa de delivery usa drones para entregar paquetes. Los datos de cada vuelo se guardan en `vuelos.txt` con el formato: `ID_DRON,DISTANCIA_KM,TIEMPO_MINUTOS`.

**Historia:**
El jefe de mantenimiento quiere saber la velocidad promedio (en km/min) de cada dron y determinar cuál fue el dron que alcanzó la mayor velocidad.

**Archivo de entrada (`vuelos.txt`):**
```text
Dron-A,10,15
Dron-B,15,20
Dron-C,8,10
Dron-D,20,30
```

**Requerimientos:**
* Leer los datos y convertirlos a los tipos numéricos correspondientes.
* Calcular `velocidad = distancia / tiempo` para cada línea.
* Imprimir la velocidad de cada dron con 2 decimales.
* Identificar y mostrar el ID del dron con la velocidad máxima.

**Ejemplo de Salida por pantalla:**
```text
Dron-A: 0.67 km/min
Dron-B: 0.75 km/min
Dron-C: 0.80 km/min
Dron-D: 0.67 km/min

El dron más rápido fue: Dron-C
```

---

## Ejercicio 3: Firewall de Seguridad
### Detección de Accesos Sospechosos
**Contexto:**
El servidor de una empresa guarda un registro de intentos de conexión en `access_log.txt`. Cada línea indica: `IP,ESTADO,HORA`.

**Historia:**
Hubo una alerta de seguridad. Necesitas filtrar todas las conexiones que tengan el estado "FALLIDO" y mostrar cuántos intentos hizo cada IP sospechosa que aparece en el log.

**Archivo de entrada (`access_log.txt`):**
```text
192.168.1.1,EXITOSO,08:30
10.0.0.5,FALLIDO,08:31
192.168.1.10,EXITOSO,08:32
10.0.0.5,FALLIDO,08:35
172.16.0.1,FALLIDO,08:40
10.0.0.5,FALLIDO,08:45
```

**Requerimientos:**
* Leer el archivo y filtrar solo las líneas con "FALLIDO".
* Contar cuántas veces aparece cada IP con estado fallido.
* Nota: Si aún no manejas diccionarios (no están en `docs/`), puedes simplemente imprimir cada línea fallida y mostrar el total de intentos fallidos detectados.

**Ejemplo de Salida por pantalla:**
```text
--- ALERTA DE SEGURIDAD: INTENTOS FALLIDOS ---
[08:31] IP Sospechosa: 10.0.0.5
[08:35] IP Sospechosa: 10.0.0.5
[08:40] IP Sospechosa: 172.16.0.1
[08:45] IP Sospechosa: 10.0.0.5
----------------------------------------------
Total de intentos fallidos bloqueados: 4
```
