# ============================================================
# CADENAS DE TEXTO (str)
# ============================================================
# Una cadena (string) es texto: letras, palabras, frases.
# Siempre va entre comillas.
# Para ejecutar:  python3 cadenas.py

# --- 1. Crear cadenas -----------------------------------------
nombre = "Ana"
ciudad = 'San Salvador'        # comillas simples o dobles, da igual
parrafo = """Este texto
ocupa varias
líneas."""                     # triples comillas para varias líneas

print(nombre)
print(ciudad)
print(parrafo)
print(type(nombre))            # <class 'str'>

# --- 2. Unir y repetir ----------------------------------------
saludo = "Hola, " + nombre     # + une cadenas
print(saludo)                  # Hola, Ana
print("ja" * 3)                # jajaja

# --- 3. f-strings: meter variables dentro del texto -----------
edad = 20
print(f"{nombre} tiene {edad} años")           # Ana tiene 20 años
print(f"El año que viene tendrá {edad + 1}")   # se puede calcular dentro

# --- 4. Longitud ----------------------------------------------
print(len("Python"))           # 6 caracteres

# --- 5. Índices: acceder a una letra --------------------------
# Las posiciones empiezan en 0:
#   P  y  t  h  o  n
#   0  1  2  3  4  5
palabra = "Python"
print(palabra[0])              # P   primera letra
print(palabra[1])              # y
print(palabra[-1])             # n   última letra

# --- 6. Rebanadas (slicing): sacar un trozo -------------------
# cadena[inicio:fin]  -> incluye inicio, NO incluye fin
print(palabra[0:3])            # Pyt
print(palabra[2:])             # thon  (desde 2 hasta el final)
print(palabra[:2])             # Py    (desde el principio hasta 2)
print(palabra[::-1])           # nohtyP  (al revés)

# --- 7. Métodos más usados ------------------------------------
frase = "  Aprender Python es divertido  "

print(frase.upper())           # todo en MAYÚSCULAS
print(frase.lower())           # todo en minúsculas
print(frase.strip())           # quita espacios de los extremos
print(frase.replace("divertido", "fácil"))   # cambia un texto por otro
print(frase.strip().split(" "))  # separa en una lista de palabras
print("hola mundo".title())    # Hola Mundo
print("hola".capitalize())     # Hola

# --- 8. Buscar dentro de una cadena ---------------------------
print("Python" in frase)       # True   ¿está dentro?
print(frase.find("Python"))    # 11     posición donde empieza (-1 si no está)
print(frase.count("e"))        # 4      cuántas veces aparece
print("hola".startswith("ho")) # True
print("foto.png".endswith(".png"))  # True

# --- 9. Las cadenas NO se pueden modificar (son inmutables) ---
# palabra[0] = "J"   <- esto da error
# Lo correcto es crear una cadena nueva:
nueva = "J" + palabra[1:]
print(nueva)                   # Jython

# --- 10. Texto y números --------------------------------------
# "Tengo " + 20        <- error: no se puede sumar texto con número
print("Tengo " + str(20) + " años")    # convertir con str()
print(int("5") + 3)                    # 8  (de texto a número)

# --- 11. Caracteres especiales --------------------------------
print("Línea 1\nLínea 2")      # \n = salto de línea
print("Columna1\tColumna2")    # \t = tabulación
print("Dijo: \"hola\"")        # \" = comillas dentro del texto

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Guarda tu nombre en una variable y muéstralo en mayúsculas.
# 2. Muestra la primera y la última letra de tu nombre.
# 3. Cuenta cuántas veces aparece la letra "a" en "manzana".
# 4. Con un f-string, muestra: "Me llamo ___ y tengo ___ años".
# 5. Invierte la palabra "programar".
