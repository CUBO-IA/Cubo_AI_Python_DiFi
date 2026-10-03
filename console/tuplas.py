# ============================================================
# TUPLAS (tuple)
# ============================================================
# Una tupla es como una lista, pero NO se puede modificar después de crearla.
# Se escribe entre paréntesis ( ).
# Úsala para datos que no deben cambiar: coordenadas, fechas, colores...
# Para ejecutar:  python3 tuplas.py

# --- 1. Crear tuplas ------------------------------------------
punto = (3, 5)
color_rojo = (255, 0, 0)
persona = ("Ana", 25, "El Salvador")

print(punto)
print(type(punto))             # <class 'tuple'>
print(len(persona))            # 3

# Tupla de UN solo elemento: necesita una coma al final
uno = (5,)
no_es_tupla = (5)              # esto es solo el número 5
print(type(uno))               # <class 'tuple'>
print(type(no_es_tupla))       # <class 'int'>

# --- 2. Acceder (igual que en las listas) ---------------------
print(persona[0])              # Ana
print(persona[-1])             # El Salvador
print(persona[0:2])            # ('Ana', 25)

# --- 3. No se pueden modificar --------------------------------
# persona[1] = 26       <- TypeError
# persona.append("x")   <- las tuplas no tienen append

# Si necesitas cambiarla, conviértela en lista y vuelve a tupla:
lista = list(persona)
lista[1] = 26
persona = tuple(lista)
print(persona)                 # ('Ana', 26, 'El Salvador')

# --- 4. Desempaquetar: repartir los valores en variables ------
x, y = punto
print("x =", x, " y =", y)     # x = 3  y = 5

nombre, edad, pais = persona
print(nombre, edad, pais)

# Truco: intercambiar dos variables en una línea
a = 1
b = 2
a, b = b, a
print(a, b)                    # 2 1

# --- 5. Métodos (solo tiene dos) ------------------------------
numeros = (1, 2, 2, 3, 2)
print(numeros.count(2))        # 3  cuántas veces aparece
print(numeros.index(3))        # 3  en qué posición está

# --- 6. Otras operaciones -------------------------------------
print(2 in numeros)            # True
print((1, 2) + (3, 4))         # (1, 2, 3, 4)  unir crea una tupla nueva
print(max(numeros), min(numeros), sum(numeros))

# --- 7. Recorrer con for --------------------------------------
for dato in persona:
    print(dato)

# --- 8. Funciones que devuelven varios valores ----------------
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto     # en realidad devuelve una tupla

c, r = dividir(17, 5)
print("Cociente:", c, "Resto:", r)     # Cociente: 3 Resto: 2

# --- 9. ¿Lista o tupla? ---------------------------------------
# Lista  [ ] -> los datos van a cambiar (carrito de compras, puntuaciones)
# Tupla  ( ) -> los datos son fijos (días de la semana, coordenadas)

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea una tupla con los 7 días de la semana y muestra el tercero.
# 2. Crea una tupla (nombre, apellido, edad) y desempaquétala en 3 variables.
# 3. Intenta cambiar un elemento de la tupla y lee el error que aparece.
# 4. Crea una función que reciba una lista de números y devuelva
#    el menor y el mayor.
# 5. Lista de tuplas con fullname y edad
personas = []

cantidad = int(input("¿Cuántas personas vas a registrar? "))

for i in range(cantidad):
    fullname = input("Nombre completo: ")
    edad = int(input("Edad: "))

    if type(fullname) == str:
        print("La variable fullname tiene un texto (str)")

    if type(edad) == int:
        print("La variable edad tiene un entero (int)")

    personas.append((fullname, edad))     # guarda la tupla en la lista

print("\n--- Personas registradas ---")
for fullname, edad in personas:
    print(f"{fullname} tiene {edad} años")

print(personas)
print(type(10))           # <class 'int'>
print(type(3.5))          # <class 'float'>
print(type("hola"))       # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2]))       # <class 'list'>
print(type((1, 2)))       # <class 'tuple'>
print(type({1, 2}))       # <class 'set'>
print(type({"a": 1}))     # <class 'dict'>
print(type(None))         # <class 'NoneType'>
