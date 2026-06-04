# =============================================================
# TÍTULO: Caminos mínimos en una grilla rectangular
# Matemáticas Discretas I — Universidad Nacional de Colombia
# =============================================================
 
# -------------------------------------------------------------
# DESCRIPCIÓN MATEMÁTICA
# Se quiere contar cuántos caminos distintos hay desde (0,0)
# hasta (a,b) moviéndose solo hacia la derecha o hacia arriba.
# Todo camino usa exactamente (a+b) pasos: 'a' a la derecha
# y 'b' hacia arriba. Contar los caminos equivale a elegir
# en qué posiciones van los pasos a la derecha.
# -------------------------------------------------------------
 
# -------------------------------------------------------------
# FÓRMULA USADA
# C(a+b, a) = (a+b)! / (a! * b!)
# Caso especial: si a=0 o b=0 solo hay 1 camino posible.
# Verificación de simetría: C(a+b, a) = C(a+b, b)
# -------------------------------------------------------------
 
# -------------------------------------------------------------
# EXPLICACIÓN DEL ALGORITMO
# 1. Se calcula C(a+b, a) con la fórmula combinatoria directa.
# 2. Para puntos obligatorios se divide en segmentos y se
#    multiplican los caminos de cada tramo (regla del producto).
# 3. Para puntos bloqueados se usa programación dinámica:
#    dp[i][j] = caminos desde (0,0) hasta (i,j).
#    Cada celda suma los caminos que llegan desde la izquierda
#    y desde abajo. Las celdas bloqueadas se fijan en 0.
# -------------------------------------------------------------
 
from math import factorial
 
# --- CÓDIGO ---
 
def combinaciones(n, r):
    # C(n, r) = n! / (r! * (n-r)!)
    # Retorna 0 si r es invalido
    if r < 0 or r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))
 
def caminos(a, b):
    # Aplica la formula C(a+b, a)
    return combinaciones(a + b, a)
 
def dibujar_grilla(a, b, bloqueados=[]):
    # Extensión opcional: tabla con caminos acumulados por celda
    # Usa programacion dinamica para construir la tabla
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[0][0] = 1
    for i in range(a + 1):
        for j in range(b + 1):
            if (i, j) in bloqueados:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                continue
            desde_izq   = dp[i-1][j] if i > 0 else 0
            desde_abajo = dp[i][j-1] if j > 0 else 0
            dp[i][j] = desde_izq + desde_abajo
 
    print(f"\n  Grilla {a}x{b} — caminos acumulados por celda")
    print("  (origen abajo-izquierda [O], destino arriba-derecha [*])\n")
    for j in range(b, -1, -1):
        fila = ""
        for i in range(a + 1):
            if (i, j) in bloqueados:
                fila += "  [X]"
            elif i == 0 and j == 0:
                fila += "  [O]"
            elif i == a and j == b:
                fila += "  [*]"
            else:
                fila += f"  {dp[i][j]:3}"
        print(" " + fila)
    print(f"\n  [O]=origen  [*]=destino  [X]=bloqueado")
    print(f"  Caminos totales: {dp[a][b]}")
    return dp[a][b]
 
 
# --- PRUEBAS ---
# Se verifican 6 casos con resultado conocido
 
print("=" * 45)
print("  PRUEBAS")
print("=" * 45)
 
casos = [
    (2, 2,    6,  "C(4,2)  = 6"),
    (3, 2,   10,  "C(5,2)  = 10"),
    (4, 3,   35,  "C(7,3)  = 35"),
    (10, 5, 3003, "C(15,5) = 3003"),
    (0, 5,    1,  "solo sube, 1 camino"),
    (5, 0,    1,  "solo derecha, 1 camino"),
]
 
for a, b, esperado, nota in casos:
    res = caminos(a, b)
    estado = "OK" if res == esperado else "FALLA"
    print(f"  [{estado}] caminos({a},{b}) = {res}   ({nota})")
 
# Validacion de simetria: C(a+b,a) debe ser igual a C(a+b,b)
print(f"\n  [Simetria] C(7,3) = {combinaciones(7,3)}  ==  C(7,4) = {combinaciones(7,4)}")
 
 
# --- CALCULADORA INTERACTIVA ---
 
print("\n" + "=" * 45)
print("  CALCULADORA")
print("=" * 45)
 
a = int(input("Ingrese a (columnas): "))
b = int(input("Ingrese b (filas):    "))
 
if a < 0 or b < 0:
    print("Error: los valores deben ser >= 0")
else:
    print(f"\nCaminos de (0,0) a ({a},{b}): C({a+b},{a}) = {caminos(a, b)}")
 
    # Punto obligatorio
    resp = input("\n¿Agregar punto obligatorio? (s/n): ")
    if resp == 's':
        px = int(input("  x del punto: "))
        py = int(input("  y del punto: "))
        if px < 0 or py < 0 or px > a or py > b:
            print("  Punto fuera de la grilla, se ignora.")
        else:
            seg1 = caminos(px, py)
            seg2 = caminos(a - px, b - py)
            print(f"  Segmento 1: C({px+py},{px}) = {seg1}")
            print(f"  Segmento 2: C({(a-px)+(b-py)},{a-px}) = {seg2}")
            print(f"  Total (regla del producto): {seg1} * {seg2} = {seg1*seg2}")
 
    # Puntos bloqueados
    bloqueados = []
    resp2 = input("\n¿Agregar puntos bloqueados? (s/n): ")
    if resp2 == 's':
        n_bl = int(input("  Cuantos puntos bloqueados: "))
        for _ in range(n_bl):
            px = int(input("  x: "))
            py = int(input("  y: "))
            bloqueados.append((px, py))
 
    # Extension opcional: dibujar grilla
    resp3 = input("\n¿Dibujar la grilla? (s/n): ")
    if resp3 == 's':
        dibujar_grilla(a, b, bloqueados)
    elif bloqueados:
        dp = [[0]*(b+1) for _ in range(a+1)]
        dp[0][0] = 1
        for i in range(a+1):
            for j in range(b+1):
                if (i, j) in bloqueados:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)
        print(f"  Caminos evitando los puntos bloqueados: {dp[a][b]}")
 
 
# -------------------------------------------------------------
# COMENTARIOS FINALES
# El cálculo directo con la fórmula es O(n), donde n = a+b,
# ya que solo se calculan tres factoriales.
# La programación dinámica para puntos bloqueados es O(a*b),
# pues recorre cada celda de la grilla exactamente una vez.
# Para grillas grandes sin bloqueos, la fórmula directa
# es mucho más eficiente que cualquier método de enumeración.
# -------------------------------------------------------------