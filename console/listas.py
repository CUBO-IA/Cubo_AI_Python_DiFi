# ============================================================
# LISTAS (list)
# ============================================================
# Una lista guarda VARIOS datos en orden, y se puede modificar.
# Se escribe entre corchetes [ ] con los elementos separados por comas.
# Para ejecutar:  python3 listas.py

# --- 1. Crear listas ------------------------------------------
frutas = ["manzana", "pera", "uva"]
numeros = [10, 20, 30, 40]
mezcla = ["Ana", 25, True, 1.70]     # puede mezclar tipos
vacia = []

print(frutas)
print(type(frutas))            # <class 'list'>
print(len(frutas))             # 3 elementos

# --- 2. Acceder por posición (empieza en 0) -------------------
print(frutas[0])               # manzana  (primero)
print(frutas[1])               # pera
print(frutas[-1])              # uva      (último)

# --- 3. Rebanadas ---------------------------------------------
print(numeros[1:3])            # [20, 30]
print(numeros[:2])             # [10, 20]
print(numeros[2:])             # [30, 40]

# --- 4. Modificar un elemento ---------------------------------
frutas[1] = "mango"
print(frutas)                  # ['manzana', 'mango', 'uva']

# --- 5. Añadir elementos --------------------------------------
frutas.append("kiwi")          # añade al final
frutas.insert(0, "fresa")      # añade en la posición 0
frutas.extend(["piña", "coco"])  # añade varios de golpe
print(frutas)

# --- 6. Quitar elementos --------------------------------------
frutas.remove("uva")           # quita por valor
ultimo = frutas.pop()          # quita el último y lo devuelve
print("Quitado:", ultimo)      # coco
del frutas[0]                  # quita por posición
print(frutas)                  # ['manzana', 'mango', 'kiwi', 'piña']

# --- 7. Buscar ------------------------------------------------
print("mango" in frutas)       # True
print(frutas.index("kiwi"))    # 2  (su posición)
print([1, 2, 2, 3].count(2))   # 2  (cuántas veces aparece)

# --- 8. Ordenar -----------------------------------------------
notas = [7, 3, 9, 5]
notas.sort()                   # ordena la lista original
print(notas)                   # [3, 5, 7, 9]
notas.reverse()                # le da la vuelta
print(notas)                   # [9, 7, 5, 3]

print(sorted([4, 1, 3]))       # [1, 3, 4]  devuelve una copia ordenada

# --- 9. Funciones con listas de números -----------------------
print(sum(notas))              # 24
print(max(notas))              # 9
print(min(notas))              # 3
print(sum(notas) / len(notas)) # 6.0  (el promedio)

# --- 10. Recorrer una lista con for ---------------------------
for fruta in frutas:
    print("Me gusta la", fruta)

# Con la posición incluida:
for posicion, fruta in enumerate(frutas):
    print(posicion, fruta)

# --- 11. Crear listas rápido (comprensión de listas) ----------
cuadrados = [n ** 2 for n in range(1, 6)]
print(cuadrados)               # [1, 4, 9, 16, 25]

pares = [n for n in range(10) if n % 2 == 0]
print(pares)                   # [0, 2, 4, 6, 8]

# --- 12. Cuidado al copiar ------------------------------------
a = [1, 2, 3]
b = a                  # b NO es una copia: es la MISMA lista
b.append(4)
print(a)               # [1, 2, 3, 4]  ¡a también cambió!

c = a.copy()           # así sí se crea una copia independiente
c.append(5)
print(a)               # [1, 2, 3, 4]
print(c)               # [1, 2, 3, 4, 5]

# --- 13. Listas dentro de listas ------------------------------
tablero = [
    [1, 2, 3],
    [4, 5, 6],
]
print(tablero[1][0])   # 4  (fila 1, columna 0)

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea una lista con 5 películas y muestra la primera y la última.
# 2. Añade una película más y elimina la segunda.
# 3. Crea una lista de 5 números y muestra su suma y su promedio.
# 4. Recorre la lista de películas con for y muéstralas en mayúsculas.
# 5. Crea con una comprensión la lista de los números del 1 al 10
#    multiplicados por 3.
