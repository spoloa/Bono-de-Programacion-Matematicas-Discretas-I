# =============================================================
# TÍTULO: Coeficientes multinomiales y palabras con letras repetidas
# Matemáticas Discretas I — Universidad Nacional de Colombia
# =============================================================
 
# -------------------------------------------------------------
# DESCRIPCIÓN MATEMÁTICA
# Dado un grupo de n objetos donde algunos se repiten,
# el coeficiente multinomial cuenta cuántos arreglos distintos
# se pueden formar. Si todos fueran distintos habría n!
# posibilidades, pero las repeticiones reducen ese número
# porque intercambiar copias del mismo objeto no da un
# arreglo nuevo.
# Ejemplo: con BANANA hay 6 letras pero A se repite 3 veces
# y N se repite 2 veces, entonces no son 6! = 720 sino 60.
# -------------------------------------------------------------
 
# -------------------------------------------------------------
# FÓRMULA USADA
# n! / (n1! * n2! * ... * nk!)
# donde n1, n2, ..., nk son las frecuencias de cada símbolo
# y n = n1 + n2 + ... + nk.
# Casos especiales:
#   - Todos iguales (ej: AAAA):    resultado = 1
#   - Todos distintos (ej: ABC):   resultado = n!
# -------------------------------------------------------------
 
# -------------------------------------------------------------
# EXPLICACIÓN DEL ALGORITMO
# 1. Se obtienen los símbolos únicos de la entrada.
# 2. Se cuenta la frecuencia de cada uno.
# 3. Se calcula n! y se divide entre el producto de los
#    factoriales de cada frecuencia.
# 4. Para listar palabras (extensión opcional) se generan
#    todas las permutaciones y se eliminan duplicados con set.
# -------------------------------------------------------------
 
from math import factorial
from itertools import permutations
 
# --- CÓDIGO ---
 
def contar_palabras(palabra):
    # Calcula n! / (n1! * n2! * ... * nk!)
    n = len(palabra)
    den = 1
    for letra in set(palabra):
        den *= factorial(palabra.count(letra))
    return factorial(n) // den
 
def listar_palabras(palabra):
    # Extensión opcional: lista todas las palabras distintas
    # Solo se usa para palabras de 8 letras o menos
    todas = sorted(set(permutations(palabra)))
    print(f"\n  Todas las palabras distintas ({len(todas)} en total):")
    for i, p in enumerate(todas, 1):
        print(f"  {i:3}. {''.join(p)}")
 
 
# --- PRUEBAS ---
# Se verifican 5 casos con resultado conocido
 
print("=" * 45)
print("  PRUEBAS")
print("=" * 45)
 
casos = [
    ("BANANA",      60,    "6!/(1!*3!*2!)"),
    ("AABB",         6,    "4!/(2!*2!)"),
    ("ABC",          6,    "3! todos distintos"),
    ("AAAA",         1,    "todos iguales"),
    ("MISSISSIPPI", 34650, "11!/(1!*4!*4!*2!)"),
]
 
for palabra, esperado, nota in casos:
    res = contar_palabras(palabra)
    estado = "OK" if res == esperado else "FALLA"
    print(f"  [{estado}] {palabra} = {res}   ({nota})")
 
 
# --- CALCULADORA INTERACTIVA ---
 
print("\n" + "=" * 45)
print("  CALCULADORA")
print("=" * 45)
print("Modo 1: ingresar una palabra  (ej: BANANA)")
print("Modo 2: ingresar frecuencias  (ej: 4 de A, 3 de B)")
modo = input("Escoja modo (1 o 2): ")
 
if modo == '1':
    palabra = input("Ingrese la palabra: ").upper().strip()
    if not palabra.isalpha():
        print("Error: solo letras por favor.")
    else:
        res = contar_palabras(palabra)
        n = len(palabra)
 
        print(f"\nPalabra: {palabra}  (n = {n})")
        for letra in sorted(set(palabra)):
            print(f"  {letra}: {palabra.count(letra)} vez/veces")
 
        den_str = " * ".join(f"{palabra.count(l)}!" for l in sorted(set(palabra)))
        print(f"\nFormula: {n}! / ({den_str}) = {res}")
        print(f"Palabras distintas: {res}")
 
        # Casos especiales
        if len(set(palabra)) == 1:
            print("  (Caso especial: todas las letras son iguales → 1 arreglo)")
        elif len(set(palabra)) == len(palabra):
            print(f"  (Caso especial: todas distintas → {n}! = {res})")
 
        # Extension opcional
        if len(palabra) <= 8:
            resp = input("\n¿Listar todas las palabras? (s/n): ")
            if resp == 's':
                listar_palabras(palabra)
        else:
            print("(Listado no disponible para palabras de más de 8 letras)")
 
elif modo == '2':
    k = int(input("Cuantos tipos distintos: "))
    frecuencias = []
    for i in range(k):
        f = int(input(f"  Cantidad del tipo {i+1}: "))
        frecuencias.append(f)
 
    n = sum(frecuencias)
    den = 1
    for f in frecuencias:
        den *= factorial(f)
    res = factorial(n) // den
 
    den_str = " * ".join(f"{f}!" for f in frecuencias)
    print(f"\nFormula: {n}! / ({den_str}) = {factorial(n)} / {den} = {res}")
    print(f"Arreglos distintos: {res}")
 
    # Extension opcional con letras genericas A, B, C...
    if n <= 8:
        resp = input("\n¿Listar todos los arreglos? (s/n): ")
        if resp == 's':
            cadena = ""
            for i, f in enumerate(frecuencias):
                cadena += chr(65 + i) * f
            listar_palabras(cadena)
else:
    print("Opcion no valida")
 
 
# -------------------------------------------------------------
# COMENTARIOS FINALES
# El cálculo de la fórmula es O(n), donde n es la longitud
# de la entrada, ya que solo recorre los símbolos una vez
# para contar frecuencias y calcula un factorial por tipo.
# El listado de palabras tiene costo O(resultado) porque
# genera todas las permutaciones; por eso se limita a n <= 8.
# Para entradas grandes la fórmula sigue siendo eficiente
# mientras que la enumeración se vuelve imprácticable.
# -------------------------------------------------------------
