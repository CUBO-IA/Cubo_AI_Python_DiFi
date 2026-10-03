# ============================================================
# BOOLEANOS (bool)
# ============================================================
# Un booleano solo puede tener dos valores: True (verdadero) o False (falso).
# Sirven para tomar decisiones en un programa.
# Para ejecutar:  python3 booleanos.py

# --- 1. Crear booleanos ---------------------------------------
# Importante: la primera letra va en MAYÚSCULA y sin comillas.
esta_lloviendo = True
tiene_licencia = False

print(esta_lloviendo, tiene_licencia)
print(type(esta_lloviendo))    # <class 'bool'>

# --- 2. Comparaciones: producen un booleano -------------------
print(5 > 3)       # True    mayor que
print(5 < 3)       # False   menor que
print(5 >= 5)      # True    mayor o igual
print(5 <= 4)      # False   menor o igual
print(5 == 5)      # True    igual a   (dos signos =)
print(5 != 5)      # False   distinto de

# Cuidado:  =  guarda un valor      ==  compara dos valores

print("hola" == "hola")    # True
print("Hola" == "hola")    # False (distingue mayúsculas)

# --- 3. Operadores lógicos: and, or, not ----------------------
# and -> True solo si LOS DOS son True
print(True and True)       # True
print(True and False)      # False

# or -> True si AL MENOS UNO es True
print(True or False)       # True
print(False or False)      # False

# not -> invierte el valor
print(not True)            # False
print(not False)           # True

# --- 4. Ejemplo real ------------------------------------------
edad = 20
tiene_entrada = True

puede_entrar = edad >= 18 and tiene_entrada
print("¿Puede entrar?", puede_entrar)      # True

# --- 5. Usarlos con if ----------------------------------------
if puede_entrar:
    print("Bienvenido")
else:
    print("No puedes pasar")

# --- 6. Valores que cuentan como False ------------------------
# bool() convierte cualquier dato a booleano.
# Cuentan como False: 0, 0.0, "" (texto vacío), [] (lista vacía), None
print(bool(0))         # False
print(bool(""))        # False
print(bool([]))        # False
print(bool(None))      # False

# Todo lo demás cuenta como True
print(bool(7))         # True
print(bool("hola"))    # True
print(bool([1, 2]))    # True

# Esto permite escribir cosas como:
nombre = ""
if not nombre:
    print("No escribiste ningún nombre")

# --- 7. Curiosidad: True vale 1 y False vale 0 ----------------
print(True + True)     # 2
print(sum([True, False, True]))   # 2  (útil para contar cuántos son True)

# --- 8. El operador in ----------------------------------------
print("a" in "casa")           # True
print(5 in [1, 2, 3])          # False

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea una variable con un número y comprueba si es mayor que 100.
# 2. Comprueba si un número está entre 10 y 20 (usa and).
# 3. Crea dos variables: es_fin_de_semana y es_feriado.
#    Crea una tercera, puedo_descansar, que sea True si alguna lo es.
# 4. ¿Qué imprime  not (5 > 3 and 2 > 4) ?  Piénsalo y luego compruébalo.
