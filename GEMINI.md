# Reglas y Convenciones del Proyecto (GEMINI.md)

Este repositorio contiene material educativo para la enseñanza de programación (Python). Gemini debe seguir estas reglas estrictamente para mantener la consistencia y la progresión pedagógica del curso.

## 1. Restricción de Contenidos (CRÍTICO)
- **Alineación con `docs/`:** Al generar enunciados de ejercicios y sus soluciones, Gemini **DEBE** basarse únicamente en los temas y herramientas explicados en la carpeta `docs/`. 
- **Prohibición de conceptos avanzados:** No se pueden utilizar librerías, estructuras de datos o sintaxis que no estén documentadas en `docs/`. Por ejemplo, no usar `list comprehensions` si solo se han cubierto listas y ciclos básicos, ni `pandas` si solo se ha visto `numpy`.
- **Evolución:** El contenido de cada ejercicio debe limitarse a lo permitido por la materia vista hasta ese punto.

## 2. Idioma y Tono
- **Idioma:** Toda la comunicación, comentarios en el código, documentación y nombres de archivos deben ser en **Español**.
- **Tono:** Educativo, claro y profesional. Las explicaciones deben ser sencillas pero técnicamente precisas, adecuadas para estudiantes principiantes.

## 3. Estándares de Código (Python)
- **Estilo:** Seguir PEP 8 (nombres de variables descriptivos en español).
- **Naming:** Usar `snake_case` para variables y funciones.
- **Indentación:** 4 espacios.
- **Formateo de texto:** Preferir siempre **f-strings** para el formateo de cadenas (ej. `f"Resultado: {valor:.2f}"`).
- **Simplicidad:** Priorizar soluciones legibles y didácticas sobre trucos avanzados o "one-liners" crípticos.

## 4. Estructura de Archivos y Nomenclatura
- **Ejercicios:** Las soluciones deben seguir el patrón `ej1.py`, `ej2.py`, etc., y ubicarse dentro de carpetas `Solve/`.
- **Documentación:** Los archivos en `docs/` deben seguir el patrón numérico `0X-nombre-del-tema.md`.
- **READMEs:** Estandarizar el nombre a `README.md` (todo en mayúsculas).
- **Carpetas:** Usar Mayúsculas Iniciales para categorías (ej. `Extras`, `Condicionales`, `Fácil`).

## 5. Flujo de Trabajo
- Al crear un ejercicio nuevo:
    1. El archivo `.py` con la solución.
    2. Un archivo `.txt` opcional con ejemplos de entrada/salida.
    3. Actualizar el `README.md` de la carpeta para incluir el nuevo ejercicio.
- Al modificar `docs/`, mantener el estilo de tablas y bloques de código con resaltado de sintaxis.

## 6. Validación
- Gemini debe verificar que el script corre sin errores y que respeta estrictamente las limitaciones de contenido impuestas por los documentos de referencia.
