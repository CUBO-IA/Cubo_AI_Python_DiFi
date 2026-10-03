# ============================================================
# DICCIONARIOS (dict)
# ============================================================
# Un diccionario guarda pares  clave: valor.
# En vez de buscar por posición (0, 1, 2...), buscas por un nombre (la clave).
# Se escribe entre llaves { }.
# Para ejecutar:  python3 diccionarios.py

# --- 1. Crear un diccionario ----------------------------------
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "San Salvador",
}

print(persona)
print(type(persona))           # <class 'dict'>
print(len(persona))            # 3 pares

# --- 2. Leer un valor -----------------------------------------
print(persona["nombre"])       # Ana

# Si la clave no existe, los corchetes dan error (KeyError).
# .get() es más seguro: devuelve None o el valor que tú indiques.
print(persona.get("telefono"))                 # None
print(persona.get("telefono", "sin teléfono")) # sin teléfono

# --- 3. Añadir y modificar ------------------------------------
persona["email"] = "ana@correo.com"    # la clave no existía: se añade
persona["edad"] = 26                   # la clave existía: se modifica
print(persona)

persona.update({"edad": 27, "pais": "El Salvador"})   # varios a la vez
print(persona)

# --- 4. Eliminar ----------------------------------------------
del persona["email"]                   # borra el par
ciudad = persona.pop("ciudad")         # borra y devuelve el valor
print("Eliminado:", ciudad)
print(persona)

# --- 5. Comprobar si existe una clave -------------------------
print("nombre" in persona)     # True
print("email" in persona)      # False

# --- 6. Claves, valores y pares -------------------------------
print(list(persona.keys()))    # ['nombre', 'edad', 'pais']
print(list(persona.values()))  # ['Ana', 27, 'El Salvador']
print(list(persona.items()))   # [('nombre', 'Ana'), ('edad', 27), ...]

# --- 7. Recorrer con for --------------------------------------
for clave in persona:
    print(clave)

for clave, valor in persona.items():
    print(clave, "->", valor)

# --- 8. Reglas de las claves ----------------------------------
# - No se repiten: si repites una, se queda con el último valor.
# - Suelen ser textos o números.
# - Los valores pueden ser de cualquier tipo, incluso listas u otros diccionarios.

alumno = {
    "nombre": "Luis",
    "notas": [8, 9, 7],
    "direccion": {"calle": "Av. Central", "numero": 12},
}
print(alumno["notas"][0])              # 8
print(alumno["direccion"]["calle"])    # Av. Central

# --- 9. Lista de diccionarios (muy habitual) ------------------
productos = [
    {"nombre": "Pan", "precio": 1.5},
    {"nombre": "Leche", "precio": 2.0},
]
for producto in productos:
    print(producto["nombre"], "cuesta", producto["precio"])

# --- 10. Ejemplo: contar letras -------------------------------
palabra = "banana"
conteo = {}
for letra in palabra:
    conteo[letra] = conteo.get(letra, 0) + 1
print(conteo)                  # {'b': 1, 'a': 3, 'n': 2}

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea un diccionario con tus datos: nombre, edad y color favorito.
# 2. Añade la clave "hobby" y cambia la edad.
# 3. Recorre el diccionario mostrando "clave: valor" en cada línea.
# 4. Crea un diccionario de 3 productos con su precio y calcula el total.
# 5. Cuenta cuántas veces aparece cada palabra en la frase
#    "el perro y el gato y el loro"  (pista: usa .split()).
