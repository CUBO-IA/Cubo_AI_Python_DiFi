# ============================================================
# FLOTANTES (float)
# ============================================================
# Un flotante es un número CON decimales: 3.14, -0.5, 2.0
# Para ejecutar:  python3 flotantes.py

# --- 1. Crear flotantes ---------------------------------------
precio = 19.99
altura = 1.75
entero_como_float = 5.0        # tiene punto, así que es float

print(precio, altura, entero_como_float)
print(type(precio))            # <class 'float'>

# Ojo: en Python el separador decimal es el PUNTO, no la coma.

# --- 2. Operaciones -------------------------------------------
print(10.5 + 2.5)      # 13.0
print(10.5 - 2.5)      # 8.0
print(2.5 * 4)         # 10.0  (float con int da float)
print(7 / 2)           # 3.5   (la división / siempre da float)

# --- 3. Redondear ---------------------------------------------
pi = 3.14159265
print(round(pi, 2))    # 3.14  (2 decimales)
print(round(pi))       # 3     (sin decimales devuelve un entero)

# --- 4. La sorpresa de los decimales --------------------------
# El ordenador guarda los decimales en binario y algunos no son exactos.
print(0.1 + 0.2)               # 0.30000000000000004  (¡no es un error tuyo!)
print(0.1 + 0.2 == 0.3)        # False

# Solución: redondear antes de comparar
print(round(0.1 + 0.2, 2) == 0.3)   # True

# --- 5. Mostrar decimales con formato -------------------------
total = 1234.5
print(f"Total: {total:.2f}")   # Total: 1234.50  (siempre 2 decimales)

# --- 6. Conversiones ------------------------------------------
print(float(7))        # 7.0    de entero a float
print(float("3.5"))    # 3.5    de texto a float
print(int(3.9))        # 3      de float a entero (corta, no redondea)

# --- 7. Notación científica -----------------------------------
grande = 1.5e6         # 1.5 x 10^6
print(grande)          # 1500000.0

# --- 8. Más matemáticas con el módulo math --------------------
import math

print(math.sqrt(16))   # 4.0   raíz cuadrada
print(math.floor(3.7)) # 3     redondea hacia abajo
print(math.ceil(3.2))  # 4     redondea hacia arriba
print(math.pi)         # 3.141592653589793

# ============================================================
# EJERCICIOS
# ============================================================
# 1. Calcula el precio final de un producto de 80.50 con un 13% de impuesto.
# 2. Calcula el área de un círculo de radio 5 (área = pi * radio ** 2).
# 3. Muestra el resultado de 10 / 3 con solo 2 decimales.
# 4. Convierte 25.5 grados Celsius a Fahrenheit (F = C * 9 / 5 + 32).
