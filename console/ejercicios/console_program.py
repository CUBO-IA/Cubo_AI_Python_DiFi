# ============================================================
# SNAKE - el clásico juego de la culebrita, para la Terminal
# ============================================================
# Para jugar:   python3 snake.py
# Controles:    flechas o W A S D para moverte, Q para salir
#
# Usa el módulo "curses", que ya viene con Python en Mac y Linux.
# (En Windows hay que instalarlo antes:  pip install windows-curses)

import curses
import random
import time

# --- Configuración: cambia estos números para modificar el juego ---
ANCHO = 20                  # columnas del tablero
ALTO = 15                   # filas del tablero
VELOCIDAD_INICIAL = 0.15    # segundos entre cada paso (menos = más rápido)
VELOCIDAD_MINIMA = 0.06     # lo más rápido que puede llegar a ir
ACELERACION = 0.005         # cuánto acelera por cada fruta

# Cada dirección es (cambio de fila, cambio de columna)
ARRIBA, ABAJO, IZQUIERDA, DERECHA = (-1, 0), (1, 0), (0, -1), (0, 1)

TECLAS = {
    curses.KEY_UP: ARRIBA, ord("w"): ARRIBA, ord("W"): ARRIBA,
    curses.KEY_DOWN: ABAJO, ord("s"): ABAJO, ord("S"): ABAJO,
    curses.KEY_LEFT: IZQUIERDA, ord("a"): IZQUIERDA, ord("A"): IZQUIERDA,
    curses.KEY_RIGHT: DERECHA, ord("d"): DERECHA, ord("D"): DERECHA,
}


def nueva_fruta(culebra):
    """Elige una casilla libre al azar para la fruta."""
    libres = [(f, c) for f in range(ALTO) for c in range(ANCHO)
              if (f, c) not in culebra]
    return random.choice(libres) if libres else None


def dibujar(tablero, culebra, fruta, estilos):
    """Pinta el tablero. Cada casilla ocupa 2 caracteres de ancho."""
    tablero.erase()
    tablero.border()
    if fruta:
        tablero.addstr(fruta[0] + 1, fruta[1] * 2 + 1, *estilos["fruta"])
    for fila, col in culebra[1:]:
        tablero.addstr(fila + 1, col * 2 + 1, *estilos["cuerpo"])
    cabeza = culebra[0]
    tablero.addstr(cabeza[0] + 1, cabeza[1] * 2 + 1, *estilos["cabeza"])
    tablero.refresh()


def partida(pantalla, tablero, estilos, record):
    """Juega una partida. Devuelve los puntos, o None si se pulsa Q."""
    # La culebra es una lista de casillas (fila, columna); la primera es la cabeza
    centro = ALTO // 2
    culebra = [(centro, ANCHO // 2 - i) for i in range(3)]
    direccion = DERECHA         # hacia dónde se movió por última vez
    proxima = DERECHA           # hacia dónde irá en el siguiente paso
    fruta = nueva_fruta(culebra)
    puntos = 0
    espera = VELOCIDAD_INICIAL
    siguiente_paso = time.monotonic() + espera

    while True:
        pantalla.addstr(0, 0, f" SNAKE   Puntos: {puntos}   Récord: {record} ")
        pantalla.clrtoeol()
        pantalla.refresh()
        dibujar(tablero, culebra, fruta, estilos)

        # Esperar una tecla hasta que toque dar el siguiente paso
        restante = siguiente_paso - time.monotonic()
        if restante > 0:
            tablero.timeout(int(restante * 1000) + 1)
            tecla = tablero.getch()
            if tecla in (ord("q"), ord("Q")):
                return None
            nueva = TECLAS.get(tecla)
            # No se permite dar media vuelta sobre sí misma
            if nueva and nueva != (-direccion[0], -direccion[1]):
                proxima = nueva
            continue

        # --- Dar un paso ---
        siguiente_paso = time.monotonic() + espera
        direccion = proxima
        cabeza = (culebra[0][0] + direccion[0], culebra[0][1] + direccion[1])

        choca_pared = not (0 <= cabeza[0] < ALTO and 0 <= cabeza[1] < ANCHO)
        come = cabeza == fruta
        # Si no come, la punta de la cola se mueve, así que no cuenta como choque
        cuerpo = culebra if come else culebra[:-1]
        if choca_pared or cabeza in cuerpo:
            return puntos

        culebra.insert(0, cabeza)       # la cabeza avanza
        if come:
            puntos += 1                 # se alarga: no se quita la cola
            espera = max(VELOCIDAD_MINIMA, espera - ACELERACION)
            fruta = nueva_fruta(culebra)
            if fruta is None:           # tablero lleno: ¡ganaste!
                return puntos
        else:
            culebra.pop()               # se quita la cola para no crecer


def mensaje_final(tablero, puntos):
    """Muestra el fin de la partida. Devuelve True si se quiere repetir."""
    lineas = ["FIN DEL JUEGO", f"Puntos: {puntos}", "", "R = jugar de nuevo", "Q = salir"]
    ancho_total = ANCHO * 2 + 2
    for i, linea in enumerate(lineas):
        fila = ALTO // 2 - 2 + i + 1
        tablero.addstr(fila, (ancho_total - len(linea)) // 2, linea, curses.A_BOLD)
    tablero.refresh()
    tablero.timeout(-1)                 # esperar sin límite de tiempo
    while True:
        tecla = tablero.getch()
        if tecla in (ord("r"), ord("R")):
            return True
        if tecla in (ord("q"), ord("Q")):
            return False


def main(pantalla):
    try:
        curses.curs_set(0)              # ocultar el cursor
    except curses.error:
        pass

    # Comprobar que la ventana de la Terminal es suficientemente grande
    filas, columnas = pantalla.getmaxyx()
    alto_total, ancho_total = ALTO + 2, ANCHO * 2 + 2
    if filas < alto_total + 2 or columnas < ancho_total:
        pantalla.addstr(0, 0, "Agranda la ventana de la Terminal y vuelve a ejecutar.")
        pantalla.addstr(1, 0, "Pulsa una tecla para salir.")
        pantalla.getch()
        return

    # Colores (si la Terminal no los tiene, se usan letras)
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
        estilos = {
            "cuerpo": ("  ", curses.color_pair(1)),
            "cabeza": ("oo", curses.color_pair(2)),
            "fruta": ("  ", curses.color_pair(3)),
        }
    else:
        estilos = {"cuerpo": ("##", 0), "cabeza": ("@@", 0), "fruta": ("()", 0)}

    # El tablero es una ventana centrada dentro de la Terminal
    tablero = curses.newwin(alto_total, ancho_total, 1, (columnas - ancho_total) // 2)
    tablero.keypad(True)                # para que funcionen las flechas
    pantalla.addstr(alto_total + 1, 0, " Flechas o WASD: mover   Q: salir ")

    record = 0
    while True:
        puntos = partida(pantalla, tablero, estilos, record)
        if puntos is None:
            break
        record = max(record, puntos)
        if not mensaje_final(tablero, puntos):
            break


# curses.wrapper prepara la Terminal y la deja como estaba al terminar
curses.wrapper(main)