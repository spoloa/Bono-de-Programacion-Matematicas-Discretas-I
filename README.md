# Bono de Programación — Matemáticas Discretas I
**Universidad Nacional de Colombia**  
Estudiante: Sebastian Polo Alvarez -
Docente: Jhoan Sebastian Tenjo García 

---
## Descripcion general

En este repositorio se presentan las soluciones a dos ejercicios de combinatoria y conteo, desarrollados como bono programable de la asignatura Matemáticas Discretas I. Cada ejercicio cuenta con documentación del razonamiento matemático empleado, así como con una interfaz visual interactiva.

---
## Cómo ejecutar

Necesitas Python 3.7 o superior. No requiere instalar nada extra.

```bash
python problema8.py
python problema9.py
```

---

## Cómo descargar los archivos

**Opción 1 — Clonar el repositorio (si tienes Git):**
```bash
git clone <url-del-repositorio>
cd <nombre-de-la-carpeta>
```

**Opción 2 — Descargar manualmente:**  
En la página del repositorio haz clic en `Code → Download ZIP`, descomprime la carpeta y entra a ella.

---

## Cómo ejecutar los programas

1. Abre una terminal (en Windows: `cmd` o `PowerShell`, en Mac/Linux: `Terminal`).
2. Navega hasta la carpeta donde están los archivos:

```bash
cd ruta/a/la/carpeta
```

3. Ejecuta el programa que quieras:

```bash
python problema8.py
python problema9.py
```

> En algunos sistemas puede ser necesario escribir `python3` en lugar de `python`.

Cada programa primero corre sus pruebas automáticas y luego entra en modo interactivo donde te pide los datos.

---

## Problema 8 — Caminos mínimos en una grilla

### 1. Descripción del problema
Se quiere contar cuántos caminos distintos existen desde el punto (0,0) hasta el punto (a,b)
en una grilla rectangular, moviéndose únicamente hacia la derecha o hacia arriba.
Cada camino usa exactamente (a+b) pasos, por lo que contar los caminos es equivalente
a elegir en qué posiciones del recorrido van los pasos hacia la derecha.

### 2. Fórmula combinatoria

$$C(a+b,\ a) = \frac{(a+b)!}{a! \cdot b!}$$

### 3. Algoritmo implementado
- Para el cálculo directo se usa la fórmula C(a+b, a).
- Para puntos obligatorios se divide el camino en segmentos y se multiplican los resultados (regla del producto).
- Para puntos bloqueados se usa **programación dinámica**: se construye una tabla donde cada celda guarda la cantidad de caminos que llegan a ella, sumando los que vienen desde la izquierda y desde abajo. Las celdas bloqueadas se fijan en 0.

### 4. Código

Archivo: `problema8.py`

### Instrucciones de ejecución

Corre el programa con:

```bash
python problema8.py
```

El programa primero ejecuta las pruebas automáticas y luego te pide los datos uno por uno:

```
Ingrese a (columnas): 4
Ingrese b (filas):    3
```

Luego te pregunta si quieres agregar restricciones opcionales:

```
¿Agregar punto obligatorio? (s/n):
```
→ Si escribes `s`, te pide las coordenadas `x` e `y` del punto por el que debe pasar el camino.

```
¿Agregar puntos bloqueados? (s/n):
```
→ Si escribes `s`, te pregunta cuántos puntos bloqueados quieres y las coordenadas de cada uno.

```
¿Dibujar la grilla? (s/n):
```
→ Si escribes `s`, imprime una tabla visual con el número de caminos que llegan a cada celda:

```
   1    4   10   20  [*]
   1    3    6   10   15
   1    2    3    4    5
  [O]   1    1    1    1

[O]=origen  [*]=destino  [X]=bloqueado
Caminos totales hasta destino: 35
```

> Escribe siempre `s` o `n` cuando el programa lo pida, y números enteros no negativos para `a` y `b`.

### 5. Pruebas

| a  | b | Resultado esperado | Verificación     |
|----|---|--------------------|------------------|
| 2  | 2 | 6                  | C(4,2) = 6       |
| 3  | 2 | 10                 | C(5,2) = 10      |
| 4  | 3 | 35                 | C(7,3) = 35      |
| 10 | 5 | 3003               | C(15,5) = 3003   |
| 0  | 5 | 1                  | C(5,0) = 1       |
| 5  | 0 | 1                  | C(5,5) = 1       |

### 6. Casos especiales validados
- `a = 0` o `b = 0`: solo existe un camino (solo se puede ir en una dirección). Resultado: 1.
- `a = b`: verifica la simetría C(a+b, a) = C(a+b, b).
- Punto obligatorio fuera de la grilla: el programa lo detecta y avisa.
- Celda bloqueada: la tabla dinámica la pone en 0 y recalcula todo.

### 7. Eficiencia
El cálculo con la fórmula directa es **O(n)** donde n = a+b, ya que solo calcula tres factoriales.
La programación dinámica para puntos bloqueados es **O(a·b)**, pues recorre cada celda de la grilla una sola vez.

---

## Problema 9 — Coeficientes multinomiales

### 1. Descripción del problema
Dado un conjunto de n objetos donde algunos se repiten (por ejemplo las letras de una palabra),
el coeficiente multinomial cuenta cuántos arreglos o palabras distintas se pueden formar.
Si todos los objetos fueran distintos habría n! arreglos, pero como hay repetidos,
se divide entre los factoriales de cada frecuencia para no contar duplicados.

### 2. Fórmula combinatoria

$$\frac{n!}{n_1! \cdot n_2! \cdots n_k!}$$

donde $n_1, n_2, \ldots, n_k$ son las frecuencias de cada símbolo distinto y $n = n_1 + n_2 + \cdots + n_k$.

### 3. Algoritmo implementado
1. Se obtienen los símbolos únicos de la entrada.
2. Se cuenta la frecuencia de cada uno con `.count()`.
3. Se calcula n! y se divide entre el producto de los factoriales de cada frecuencia.
4. Para listar las palabras (extensión opcional) se usan permutaciones y se eliminan duplicados con `set`.

### 4. Código

Archivo: `problema9.py`

### Instrucciones de ejecución

Corre el programa con:

```bash
python problema9.py
```

El programa primero ejecuta las pruebas automáticas y luego te pregunta el modo de entrada:

```
Modo 1: ingresar una palabra  (ej: BANANA)
Modo 2: ingresar frecuencias  (ej: 4 letras A, 3 letras B)
Escoja modo (1 o 2):
```

**Modo 1 — palabra:**
```
Ingrese la palabra: BANANA
```
→ El programa muestra la frecuencia de cada letra, la fórmula con los valores reales y el resultado:
```
Palabra: BANANA
  A: 3 vez/veces
  B: 1 vez/veces
  N: 2 vez/veces

Formula: 6! / (3! * 1! * 2!) = 60
Palabras distintas: 60
```
→ Si la palabra tiene 8 letras o menos, pregunta si quieres listar todas las palabras distintas.

**Modo 2 — frecuencias manuales:**
```
Cuantos tipos de letra/objeto distintos: 3
  Cantidad del tipo 1: 4
  Cantidad del tipo 2: 3
  Cantidad del tipo 3: 2
```
→ Calcula y muestra el resultado. Si n ≤ 8 también ofrece listar los arreglos.

> La palabra debe contener solo letras (sin números ni espacios). El programa avisa si la entrada no es válida.

### 5. Pruebas

| Entrada     | Resultado esperado | Fórmula                        |
|-------------|--------------------|--------------------------------|
| BANANA      | 60                 | 6! / (1! · 3! · 2!)            |
| AABB        | 6                  | 4! / (2! · 2!)                 |
| ABC         | 6                  | 3! / (1! · 1! · 1!)            |
| AAAA        | 1                  | 4! / 4!                        |
| MISSISSIPPI | 34650              | 11! / (1! · 4! · 4! · 2!)      |
| [4, 3, 2]   | 1260               | 9! / (4! · 3! · 2!)            |
| [1,1,1,1]   | 24                 | 4! / (1!·1!·1!·1!) = 4!        |

### 6. Casos especiales validados
- Todos los objetos iguales (ej: `AAAA`): resultado = 1, solo hay un arreglo posible.
- Todos los objetos distintos (ej: `ABC`): resultado = n!, ninguna repetición reduce el conteo.
- Palabra de una sola letra: resultado = 1.
- Entrada con caracteres no alfabéticos: el programa avisa y no continúa.

### 7. Eficiencia
El cálculo de la fórmula es **O(n)** donde n es la longitud de la palabra, ya que recorre los caracteres una vez para contar frecuencias y calcula un factorial por cada tipo distinto.
El listado exhaustivo de palabras (extensión opcional) tiene complejidad **O(n!/n1!·...·nk!)** y solo se activa para palabras con 8 letras o menos.

---

## Estructura del repositorio

```
/
├── README.md 
├── problema8.py
└── problema9.py
```

---

## Nota sobre el uso de IA

Durante el desarrollo de este trabajo se utilizó inteligencia artificial (Claude de Anthropic)
como apoyo puntual en la implementación, dado que Python no es un lenguaje con el que
tenga experiencia previa.

El uso se limitó a:
- Ayuda con sintaxis específica de Python (formato de strings, manejo de listas, funciones de `itertools`).
- Corrección de errores puntuales en el código.
- Sugerencias sobre cómo estructurar la salida en consola.
- Ayuda para algunas redacciones

La comprensión matemática de los problemas, la elección de las fórmulas, la lógica del
algoritmo y la verificación de los resultados fueron desarrolladas de forma propia a partir
de los temas vistos en clase.
