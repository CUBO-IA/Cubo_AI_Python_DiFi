from .settings import COLUMNS, ROWS


class Snake:

    def __init__(self):
        self.reset()

    def reset(self):
        center_x = COLUMNS // 2
        center_y = ROWS // 2

        self.body = [
            (center_x, center_y),
            (center_x - 1, center_y),
            (center_x - 2, center_y),
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

    def change_direction(self, direction):

        opposite = (
            -self.direction[0],
            -self.direction[1]
        )

        if direction != opposite:
            self.next_direction = direction

    def move(self, grow=False):

        self.direction = self.next_direction

        head_x, head_y = self.body[0]

        direction_x, direction_y = self.direction

        new_head = (
            head_x + direction_x,
            head_y + direction_y
        )

        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

    def has_collided_with_wall(self):

        head_x, head_y = self.body[0]

        return (
            head_x < 0
            or head_x >= COLUMNS
            or head_y < 0
            or head_y >= ROWS
        )

    def has_collided_with_self(self):

        head = self.body[0]

        return head in self.body[1:]