# Snake Game

Juego clásico Snake desarrollado 100% en Python con Pygame y preparado para convertirse en una aplicación macOS.

## Estructura

- `main.py` — punto de entrada.
- `game/game.py` — motor principal.
- `game/snake.py` — serpiente.
- `game/food.py` — comida.
- `game/settings.py` — configuración.
- `game/score.py` — puntuación.
- `assets/` — recursos del juego.
- `build/` — archivos relacionados con el empaquetado.

## Ejecutar en macOS

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Este proyecto es una base inicial. El movimiento, las colisiones, la comida, el crecimiento, el Game Over y el empaquetado como `.app` se implementarán paso a paso.
