# 🔐 Ayudantía 5 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: funciones (`def`) con parámetros y retorno, iteración sobre strings con `for`, lectura de archivos con `open()` + `readline()`, ciclos `while`, acumuladores y llamada de funciones desde otras funciones.

---

## 🛡️ Ejercicio 1 — Contraseña

Microsoft necesita un sistema que evalúe la fortaleza de una contraseña asignándole un puntaje de seguridad basado en criterios técnicos. Se deben implementar **al menos 3 funciones** antes del programa principal.

**Funciones requeridas**

### `verificar_largo(contraseña)`
- **Entrada:** string con la contraseña.
- **Retorna:** `True` si tiene 10 caracteres o más, `False` si tiene menos.


### `contener_especiales(contraseña)`
- **Entrada:** string con la contraseña.
- **Proceso:** Busca caracteres de la lista permitida: `*, _, !, @, #`
- **Retorna:** la **cantidad** de caracteres especiales encontrados.


### `tiene_numeros(password)`
- **Retorna:** `True` si la contraseña tiene al menos un dígito numérico.


### `analizar_fortaleza(password)`
- **Proceso:** Llama a las tres funciones anteriores y calcula el puntaje total.
- **Retorna:** puntaje entre 0 y 6.

| Criterio | Puntos |
|---|---|
| Largo ≥ 10 caracteres | +2 |
| Por cada carácter especial (máximo 3) | +1 c/u |
| Tiene al menos un número | +1 |

**Programa principal**

1. Solicitar la contraseña al usuario.
2. Llamar a `analizar_fortaleza()`.
3. Mostrar veredicto según puntaje:

| Puntaje | Veredicto |
|---|---|
| 0 – 2 | `"Seguridad Baja: No cumple los estándares"` |
| 3 – 4 | `"Seguridad Media: Aceptable pero mejorable"` |
| 5 – 6 | `"Seguridad Alta: Contraseña robusta"` |

4. **Extra (Opcional):** Si la seguridad es Baja, pedir la contraseña nuevamente hasta que el puntaje sea al menos 3.

**Ejemplo de salida 1**
```
--- BIENVENIDO AL EVALUADOR DE MICROSOFT UCN ---

Ingrese su contraseña para analizar: gladiador_@12
Puntaje: 5
Veredicto: Seguridad Alta: Contraseña robusta.

Gracias por usar nuestro sistema de seguridad.
```

**Ejemplo de salida 2** (con bucle de reintento)
```
--- BIENVENIDO AL EVALUADOR DE MICROSOFT UCN ---

Ingrese su contraseña para analizar: JSJSJS
Puntaje: 0
Veredicto: Seguridad Baja: No cumple los estándares. Intente de nuevo.

Ingrese su contraseña para analizar: HOLAMUN0099
Puntaje: 3
Veredicto: Seguridad Media: Aceptable pero mejorable.

Gracias por usar nuestro sistema de seguridad.
```

---

## ☁️ Ejercicio 2 — Consumo

El equipo de TI de la UCN sospecha que personas ajenas están usando credenciales de los laboratorios para acceder a Microsoft Azure. Se pide desarrollar un sistema que cruce el listado de usuarios autorizados con el registro de consumo de la nube.

**Archivos de datos**

| Archivo | Contenido |
|---|---|
| `alumnos.txt` | Un RUT autorizado por línea |
| `consumo.txt` | Registro de uso con formato `rut,minutos` |

**Ejemplo `alumnos.txt`:**
```
12.345.678-9
20.111.222-3
15.987.654-k
```

**Ejemplo `consumo.txt`:**
```
12.345.678-9,120
99.000.001-k,500
88.123.123-4,410
20.111.222-3,90
```

**Funciones requeridas**

### `es_autorizado(rut_a_buscar)`
- **Entrada:** string con el RUT a verificar.
- **Proceso:** Abre `alumnos.txt` y lo lee línea por línea.
- **Retorna:** `1` si el RUT está en el archivo, `0` si no está. (**No usar** `True`/`False`).

### `calcular_costo_intrusos()`
- **Proceso:** Abre `consumo.txt`, extrae el RUT de cada línea y llama a `es_autorizado()`.
- **Cálculo:** Si retorna `0`, acumula los minutos de esa línea.
- **Retorna:** costo total en USD (cada minuto cuesta **$0.5 USD**).

**Programa principal**

1. Imprimir mensaje de bienvenida.
2. Llamar a `calcular_costo_intrusos()` y guardar resultado.
3. Mostrar por pantalla el costo total detectado:


**Ejemplo de salida**
```
--- INICIANDO AUDITORÍA MICROSOFT-UCN ---
Alerta: El RUT 99.000.001-k no está autorizado.
Alerta: El RUT 88.123.123-4 no está autorizado.
...
---------------------------------------
El costo total de los accesos ilegales es:
$ 1450.5 USD
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `for caracter in string` | Recorre el string carácter por carácter |
| `caracter in lista` | Verifica si un carácter pertenece a una lista |
| Función que llama a función | `analizar_fortaleza()` llama a `verificar_largo()`, etc. |
| Retornar `1` / `0` en vez de `True`/`False` | Válido en Python — `1` y `0` son equivalentes numéricos de `True` y `False` |
| Abrir archivo dentro de función | Cada llamada a `es_autorizado()` abre y cierra `alumnos.txt` |
