import random

from .settings import COLUMNS, ROWS


class Food:

    def __init__(self):
        self.position = (0, 0)

    def respawn(self, snake_body):

        available_positions = [
            (x, y)
            for x in range(COLUMNS)
            for y in range(ROWS)
            if (x, y) not in snake_body
        ]

        if available_positions:
            self.position = random.choice(available_positions)