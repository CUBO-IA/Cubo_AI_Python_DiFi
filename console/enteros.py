# ============================================================
# ENTEROS (int)
# ============================================================
# Un entero es un número SIN decimales: 5, -3, 0, 1000000
# Para ejecutar este archivo en Mac, abre Terminal y escribe:
#     python3 enteros.py

# --- 1. Crear enteros -----------------------------------------
edad = 25
temperatura = -4
poblacion = 6_500_000      # los guiones bajos solo ayudan a leer el número

print("Edad:", edad)
print("Temperatura:", temperatura)
print("Población:", poblacion)

# type() te dice de qué tipo es un dato
print(type(edad))          # <class 'int'>

# --- 2. Operaciones básicas -----------------------------------
a = 7
b = 2

print("Suma:", a + b)              # 9
print("Resta:", a - b)             # 5
print("Multiplicación:", a * b)    # 14
print("División:", a / b)          # 3.5  (¡la división siempre da un decimal!)
print("División entera:", a // b)  # 3    (descarta los decimales)
print("Resto (módulo):", a % b)    # 1    (lo que sobra de dividir 7 entre 2)
print("Potencia:", a ** b)         # 49   (7 elevado a 2)

# --- 3. Orden de las operaciones ------------------------------
# Igual que en matemáticas: primero potencias, luego * y /, luego + y -
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20  (los paréntesis van primero)

# --- 4. Modificar una variable --------------------------------
puntos = 10
puntos = puntos + 5    # forma larga
puntos += 5            # forma corta, hace lo mismo
print("Puntos:", puntos)   # 20

# También existen: -=   *=   //=   %=   **=

# --- 5. Convertir otros datos a entero ------------------------
texto = "42"
numero = int(texto)            # de texto a entero
print(numero + 1)              # 43

print(int(9.99))               # 9  (corta los decimales, NO redondea)
print(round(9.99))             # 10 (round sí redondea)

# --- 6. Funciones útiles --------------------------------------
print(abs(-15))                # 15  valor absoluto
print(max(3, 8, 5))            # 8   el mayor
print(min(3, 8, 5))            # 3   el menor

# --- 7. Truco clásico: ¿par o impar? --------------------------
n = 14
print(n, "es par:", n % 2 == 0)    # True

# ============================================================
# EJERCICIOS (escribe tu código debajo de cada uno)
# ============================================================
# 1. Crea dos variables con números enteros y muestra su suma y su producto.
# 2. Calcula cuántos minutos tiene una semana.
# 3. Tienes 47 caramelos y 5 amigos. ¿Cuántos le tocan a cada uno
#    y cuántos sobran? (usa // y %)
# 4. Convierte el texto "150" en entero y súmale 50.
