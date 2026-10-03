# ============================================================
# NONE (NoneType)
# ============================================================
# None significa "nada", "sin valor", "vacío".
# No es 0, no es "" y no es False: es la AUSENCIA de un valor.
# Para ejecutar:  python3 none.py

# --- 1. Crear una variable sin valor --------------------------
# Se escribe con N mayúscula y sin comillas.
resultado = None

print(resultado)               # None
print(type(resultado))         # <class 'NoneType'>

# --- 2. Para qué sirve ----------------------------------------
# Para decir "todavía no hay dato". Por ejemplo, un jugador sin puntuación:
puntuacion = None      # aún no ha jugado (distinto de 0, que sería jugar y sacar cero)

# --- 3. Comprobar si algo es None: usa "is" -------------------
if puntuacion is None:
    print("Todavía no hay puntuación")

puntuacion = 85
if puntuacion is not None:
    print("Puntuación:", puntuacion)

# --- 4. None no es lo mismo que 0, "" o False -----------------
print(None == 0)       # False
print(None == "")      # False
print(None == False)   # False

# Aunque en un if cuenta como falso:
print(bool(None))      # False

# --- 5. Funciones que no devuelven nada -----------------------
# Si una función no tiene return, devuelve None automáticamente.
def saludar(nombre):
    print("Hola,", nombre)

valor = saludar("Ana")
print(valor)           # None

# Error típico: print() también devuelve None
x = print("esto se muestra")
print(x)               # None

# Otro error típico: sort() ordena la lista pero devuelve None
numeros = [3, 1, 2]
ordenados = numeros.sort()
print(ordenados)       # None   (la lista ordenada está en "numeros")
print(numeros)         # [1, 2, 3]

# --- 6. None como "no encontrado" -----------------------------
def buscar_precio(producto):
    precios = {"pan": 1.5, "leche": 2.0}
    return precios.get(producto)       # devuelve None si no existe

precio = buscar_precio("queso")
if precio is None:
    print("Ese producto no existe")
else:
    print("Cuesta", precio)

# --- 7. None como valor por defecto en una función ------------
def presentar(nombre, apodo=None):
    if apodo is None:
        print("Me llamo", nombre)
    else:
        print("Me llamo", nombre, "pero me dicen", apodo)

presentar("Roberto")
presentar("Roberto", "Beto")

# --- 8. No se puede operar con None ---------------------------
# None + 5        <- TypeError
# Por eso conviene comprobar con "is None" antes de usar el valor.

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea una variable con None y comprueba con if si es None.
# 2. Escribe una función sin return, guarda su resultado y muéstralo.
# 3. Crea un diccionario de 3 países con su capital. Busca con .get()
#    un país que no esté y muestra "No lo conozco" si devuelve None.
