# ============================================================
# CONJUNTOS (set)
# ============================================================
# Un conjunto guarda elementos SIN repetidos y SIN orden.
# Se escribe entre llaves { }, pero sin pares clave: valor.
# Para ejecutar:  python3 conjuntos.py

# --- 1. Crear conjuntos ---------------------------------------
colores = {"rojo", "verde", "azul"}
numeros = {1, 2, 2, 3, 3, 3}       # los repetidos se eliminan solos

print(colores)                 # el orden puede salir distinto cada vez
print(numeros)                 # {1, 2, 3}
print(type(colores))           # <class 'set'>
print(len(numeros))            # 3

# Conjunto vacío: se crea con set(), porque {} es un diccionario vacío
vacio = set()
print(type(vacio))             # <class 'set'>
print(type({}))                # <class 'dict'>

# --- 2. No tienen posiciones ----------------------------------
# colores[0]   <- TypeError: en un conjunto no hay "primero" ni "último"

# --- 3. Añadir y quitar ---------------------------------------
colores.add("amarillo")
colores.add("rojo")            # ya estaba: no pasa nada
print(len(colores))            # 4

colores.remove("verde")        # quita; da error si no existe
colores.discard("morado")      # quita; NO da error si no existe
print(sorted(colores))         # sorted() devuelve una lista ordenada

# --- 4. Comprobar si un elemento está -------------------------
print("rojo" in colores)       # True
print("negro" in colores)      # False

# --- 5. Uso más común: eliminar repetidos de una lista --------
lista = [1, 2, 2, 3, 4, 4, 5]
sin_repetidos = list(set(lista))
print(sorted(sin_repetidos))   # [1, 2, 3, 4, 5]

# --- 6. Operaciones entre conjuntos ---------------------------
futbol = {"Ana", "Luis", "Marta"}
baloncesto = {"Luis", "Marta", "Pedro"}

# Unión: todos los elementos de los dos
print(sorted(futbol | baloncesto))     # ['Ana', 'Luis', 'Marta', 'Pedro']

# Intersección: solo los que están en los dos
print(sorted(futbol & baloncesto))     # ['Luis', 'Marta']

# Diferencia: los del primero que NO están en el segundo
print(sorted(futbol - baloncesto))     # ['Ana']

# Diferencia simétrica: los que están en uno solo de los dos
print(sorted(futbol ^ baloncesto))     # ['Ana', 'Pedro']

# También existen como métodos:
# futbol.union(baloncesto), futbol.intersection(baloncesto),
# futbol.difference(baloncesto)

# --- 7. Subconjuntos ------------------------------------------
print({1, 2}.issubset({1, 2, 3}))      # True  ({1, 2} está dentro)
print({1, 2, 3}.issuperset({1, 2}))    # True

# --- 8. Recorrer con for --------------------------------------
for color in sorted(colores):
    print(color)

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea un conjunto con 5 animales y añade uno más.
# 2. Elimina los repetidos de la lista [5, 3, 5, 1, 3, 9, 1].
# 3. Con los conjuntos {1, 2, 3, 4} y {3, 4, 5, 6}, muestra
#    la unión, la intersección y la diferencia.
# 4. ¿Cuántas letras distintas tiene la palabra "murcielago"?
#    (pista: set("murcielago"))
