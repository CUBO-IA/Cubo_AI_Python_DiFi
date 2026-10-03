# 5. Pedir nombre y edad por consola
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))   # int() convierte el texto a número

es_menor = edad < 18        # True si es menor de 18
tiene_18 = edad == 18       # True solo si tiene exactamente 18

if es_menor:
    print(f"{nombre}, eres menor de edad")

# Mensaje 1
print(f"Hola {nombre}, tienes {edad} años")

# Mensaje 2: ¿la edad es igual a 18?
if tiene_18:
    print("¿Tienes 18 años?: Verdadero")
else:
    print("¿Tienes 18 años?: Falso")