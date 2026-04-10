# Compilado de Ejercicios: Subprogramas y Funciones (Nivel Difícil)

## Ejercicio 1: Procesador de Coordenadas Espaciales
### Análisis de Telemetría en CodeVerse
**Contexto:**
Un satélite envía paquetes de coordenadas en un archivo de texto llamado `telemetria.txt`.

**Historia:**
Se requiere un script modular que procese estos puntos. Debes definir:
1. `obtener_distancia(x, y)`: Retorna la distancia al origen `(0,0)` usando la fórmula `sqrt(x^2 + y^2)`.
2. `procesar_archivo(nombre_archivo)`: Lee el archivo, llama a la función de distancia para cada línea y muestra los resultados.

**Archivo de entrada (`telemetria.txt`):**
```text
10,20
-5,12
0,44
15,-8
```

**Requerimientos:**
* Importar `math` para usar `math.sqrt()`.
* El archivo tiene el formato `X,Y`.
* El programa principal solo debe llamar a `procesar_archivo()`.

---

## Ejercicio 2: Evaluador de Salud Nutricional
### Reporte Automatizado en Medisystem
**Contexto:**
La clínica Medisystem necesita un script para calcular el IMC de los pacientes a partir de un archivo.

**Historia:**
Crea las siguientes funciones:
1. `calcular_imc(peso, altura)`: Retorna `peso / (altura^2)`.
2. `clasificar_imc(valor)`: Retorna "Bajo peso" (< 18.5), "Normal" (18.5 - 24.9), "Sobrepeso" (25 - 29.9) u "Obesidad" (>= 30).
3. `generar_reporte()`: Lee el archivo `pacientes.txt` (formato `Nombre,Peso,Altura`), usa las funciones anteriores e imprime un resumen.

**Archivo de entrada (`pacientes.txt`):**
```text
Juan,70,1.75
Maria,50,1.60
Pedro,95,1.80
```

---

## Ejercicio 3: Firewall de Direcciones IP
### Validación y Seguridad en la Terminal de Don Tito
**Contexto:**
Don Tito necesita filtrar el tráfico de red de IPs sospechosas que intentan acceder a sus servidores.

**Historia:**
Debes implementar:
1. `es_ip_valida(ip)`: Retorna `True` si la cadena contiene exactamente 3 puntos (formato básico `X.X.X.X`).
2. `esta_bloqueada(ip, archivo_lista_negra)`: Lee un archivo con IPs prohibidas y retorna `True` si la IP consultada aparece allí.

**Requerimientos:**
* El programa debe pedir una IP al usuario.
* Primero validar si el formato es correcto.
* Si es válida, verificar si está bloqueada.
* Si no está bloqueada, permitir el acceso.

**Archivo de entrada (`blacklist.txt`):**
```text
192.168.1.50
10.0.0.1
172.16.0.100
```
