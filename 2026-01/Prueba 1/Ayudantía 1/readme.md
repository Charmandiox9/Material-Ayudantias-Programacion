# Ayudantía 1 — Programación Python
**I Semestre 2026 · ITI – ICCI – ICI**

> Temas evaluados: variables, tipos de datos, operadores aritméticos, condicionales (`if/elif/else`) y salida por consola (`print` / `input`).

---

## 📋 Ejercicios

### 1. Sobreviviendo 🔫

Mike está atrapado en un mundo postapocalíptico. Tras escapar de una horda de zombis se refugia en un búnker donde un mercader vende suministros. Te pide ayuda para calcular cuánto gastará y cuánto le quedará de dinero, considerando los descuentos del mercader.

**Requerimientos**

1. **Menú**
   - Mostrar `"Bienvenido forastero, ¿Qué quieres hacer?"`
   - Opciones: `1) Comprar Suministros` / `2) Salir`
   - Pedir opción por consola.

2. **Comprar Suministros**
   - Pedir monto total disponible.
   - Pedir gasto deseado en suministros.
   - Si el gasto > monto disponible → imprimir `"No tienes dinero suficiente"`.

3. **Lógica de descuentos**

   | Gasto ingresado | Descuento |
   |---|---|
   | ≤ 20.000 | 0% |
   | 20.001 – 50.000 | 5% |
   | 50.001 – 100.000 | 10% |
   | > 100.000 | 15% |

   - Si el gasto es **número par** → descuento adicional del **3%** sobre el monto ya descontado.
   - En ese caso imprimir: `"El mercader del refugio te dio un descuento extra del 3%"`

4. **Resultados de compra**
   - Monto inicial ingresado
   - Gasto original ingresado
   - Gasto final después de descuentos
   - Dinero restante (monto inicial − gasto final)

5. **Salir**
   - Imprimir `"Buena suerte sobreviviendo"`

**Ejemplo de salida**
```
Bienvenido forastero, ¿Qué quieres hacer?
1) Comprar Suministros
2) Salir
Ingrese una opcion: 1

Ingresa el monto disponible: 120000
Ingresa el monto que deseas gastar: 62250
El mercader del refugio te dio un descuento extra del 3%

===RESUMEN DE LA COMPRA===
Monto inicial: 120000.0
Gasto original: 62250.0
Gasto con descuento: 54344.25
Dinero restante: 65655.75
```

---

### 2. Cuanto Falta 🚗

Rick viaja a Estados Unidos y arrienda un auto, pero los carteles y el velocímetro usan millas y mph. Su hijo, estudiante de la UCN, crea un conversor para ayudarlo.

**Requerimientos**

1. **Ingreso de datos**
   - Pedir millas a recorrer.
   - Pedir velocidad en mph.
   - Si la velocidad en km/h supera los **140**, imprimir:
     `"Rick conduciendo a (X) km/h está superando el límite permitido en carretera"`

2. **Resumen por consola**
   - Millas ingresadas → equivalente en km.
   - Velocidad en mph → equivalente en km/h.
   - Tiempo de viaje en **horas** y en **minutos** (2 decimales).

**Consideraciones**
- 1 milla = 1.61 km
- 1 mph = 1.609 km/h
- Tiempo = Distancia / Velocidad
- Usar `round(valor, 2)` para todos los resultados.

**Ejemplo de salida**
```
Calculadora de viaje
Ingrese la cantidad de millas: 140
Velocidad a la que irán (mph): 92

Rick conduciendo a 148.03 km/h está superando el límite permitido en carretera

===RESULTADOS OBTENIDOS===
140 millas equivalen a 225.4 kilómetros
92 mph equivalen a 148.03 km/h
Con los datos ingresados el viaje tardará aproximadamente 1.52 horas lo que también equivale a 91.2 minutos
```

---

### 3. Cuidado con la Plata 💸

Un grupo de amigos viaja por el mundo y necesita convertir entre pesos chilenos (CLP), dólares (USD) y euros (EUR).

**Requerimientos**

1. **Menú de conversiones**
   ```
   1) CLP a USD
   2) CLP a EUR
   3) USD a CLP
   4) USD a EUR
   5) EUR a CLP
   6) EUR a USD
   ```
   - Pedir opción y monto a convertir.

2. **Resumen de conversión**
   - Imprimir monto origen y monto destino con su moneda.
   - Si la moneda destino es **USD** y el monto convertido es **< 5000** → imprimir `"Puede que vayan con muy poca plata"`

**Tasas de cambio**
| Conversión | Tasa |
|---|---|
| 1 USD | 920 CLP |
| 1 USD | 1.14 EUR |
| 1 EUR | 1070 CLP |
| 1 EUR | 0.88 USD |

- Usar `round(valor, 2)` para todos los resultados.

**Ejemplo de salida**
```
Conversor de dinero
1) CLP a USD
2) CLP a EUR
3) USD a CLP
4) USD a EUR
5) EUR a CLP
6) EUR a USD
Selecciona una opción: 1
Ingresa el monto a convertir: 125500

===CONVERSION REALIZADA===
125500.0 CLP equivalen a 136.41 USD
Puede que vayan con muy poca plata
```

---

## 🧠 Conceptos clave

| Concepto | Descripción breve |
|---|---|
| `input()` | Lee texto desde consola, siempre devuelve `str` |
| `int()` / `float()` | Convierte string a número entero o decimal |
| `print()` | Muestra texto o variables en consola |
| `if / elif / else` | Ejecuta bloques de código según condición |
| `%` (módulo) | Resto de la división — útil para detectar pares (`n % 2 == 0`) |
| `round(val, n)` | Redondea `val` a `n` decimales |
| f-strings | `f"Resultado: {variable:.2f}"` — formato inline de variables |
