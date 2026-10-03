# ============================================================
# NÚMEROS COMPLEJOS (complex)
# ============================================================
# Un número complejo tiene parte real y parte imaginaria: 3 + 4j
# Se usan en matemáticas avanzadas, física e ingeniería.
# Si estás empezando, puedes leer este archivo al final.
# Para ejecutar:  python3 complejos.py

# --- 1. Crear complejos ---------------------------------------
z = 3 + 4j                 # en Python la unidad imaginaria se escribe j
w = complex(1, -2)         # otra forma: complex(real, imaginaria)

print(z, w)
print(type(z))             # <class 'complex'>

# --- 2. Sus partes --------------------------------------------
print(z.real)              # 3.0  parte real
print(z.imag)              # 4.0  parte imaginaria

# --- 3. Operaciones -------------------------------------------
print(z + w)               # (4+2j)
print(z - w)               # (2+6j)
print(z * w)               # (11-2j)

# --- 4. Funciones útiles --------------------------------------
print(abs(z))              # 5.0     módulo (distancia al origen)
print(z.conjugate())       # (3-4j)  conjugado

# --- 5. La definición de j ------------------------------------
print(1j ** 2)             # (-1+0j)  j al cuadrado es -1

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Crea el complejo 2 + 5j y muestra su parte real e imaginaria.
# 2. Suma (1 + 2j) y (3 - 1j).
# 3. Calcula el módulo de 6 + 8j.
