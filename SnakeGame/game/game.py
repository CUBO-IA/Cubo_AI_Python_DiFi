import pygame

from .settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    BACKGROUND_COLOR,
    GRID_COLOR,
    SNAKE_COLOR,
    SNAKE_HEAD_COLOR,
    FOOD_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT_COLOR,
    GAME_OVER_COLOR,
    CELL_SIZE,
    FPS,
    SNAKE_SPEED,
)

from .snake import Snake
from .food import Food
from .score import Score


class SnakeGame:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()
        self.score = Score()

        self.running = True

        self.game_started = False
        self.game_over = False

        self.move_timer = 0

        self.food.respawn(self.snake.body)

    # --------------------------------------------------
    # EVENTS
    # --------------------------------------------------

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False

                # Start / restart
                if event.key == pygame.K_RETURN:

                    if not self.game_started:
                        self.start_game()

                    elif self.game_over:
                        self.start_game()

                # Restart with R
                if event.key == pygame.K_r:

                    if self.game_over:
                        self.start_game()

                if self.game_started and not self.game_over:

                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.snake.change_direction((0, -1))

                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.snake.change_direction((0, 1))

                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.snake.change_direction((-1, 0))

                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.snake.change_direction((1, 0))

    # --------------------------------------------------
    # GAME CONTROL
    # --------------------------------------------------

    def start_game(self):

        self.snake.reset()

        self.score.value = 0

        self.food.respawn(self.snake.body)

        self.game_started = True
        self.game_over = False

        self.move_timer = 0

    # --------------------------------------------------
    # UPDATE
    # --------------------------------------------------

    def update(self):

        if not self.game_started:
            return

        if self.game_over:
            return

        self.move_timer += 1

        if self.move_timer < FPS // SNAKE_SPEED:
            return

        self.move_timer = 0

        next_x = (
            self.snake.body[0][0]
            + self.snake.next_direction[0]
        )

        next_y = (
            self.snake.body[0][1]
            + self.snake.next_direction[1]
        )

        next_position = (next_x, next_y)

        eating = next_position == self.food.position

        self.snake.move(grow=eating)

        # Wall collision
        if self.snake.has_collided_with_wall():

            self.game_over = True
            return

        # Self collision
        if self.snake.has_collided_with_self():

            self.game_over = True
            return

        # Food
        if eating:

            self.score.add()

            self.food.respawn(self.snake.body)

    # --------------------------------------------------
    # DRAW
    # --------------------------------------------------

    def draw_grid(self):

        for x in range(
            0,
            WINDOW_WIDTH,
            CELL_SIZE
        ):

            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (x, 0),
                (x, WINDOW_HEIGHT)
            )

        for y in range(
            0,
            WINDOW_HEIGHT,
            CELL_SIZE
        ):

            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (0, y),
                (WINDOW_WIDTH, y)
            )

    def draw_snake(self):

        for index, (x, y) in enumerate(
            self.snake.body
        ):

            rectangle = pygame.Rect(
                x * CELL_SIZE + 1,
                y * CELL_SIZE + 1,
                CELL_SIZE - 2,
                CELL_SIZE - 2
            )

            if index == 0:

                pygame.draw.rect(
                    self.screen,
                    SNAKE_HEAD_COLOR,
                    rectangle,
                    border_radius=4
                )

            else:

                pygame.draw.rect(
                    self.screen,
                    SNAKE_COLOR,
                    rectangle,
                    border_radius=3
                )

    def draw_food(self):

        x, y = self.food.position

        center = (
            x * CELL_SIZE + CELL_SIZE // 2,
            y * CELL_SIZE + CELL_SIZE // 2
        )

        pygame.draw.circle(
            self.screen,
            FOOD_COLOR,
            center,
            CELL_SIZE // 2 - 3
        )

    # --------------------------------------------------
    # TEXT
    # --------------------------------------------------

    def draw_centered_text(
        self,
        text,
        font,
        color,
        y
    ):

        surface = font.render(
            text,
            True,
            color
        )

        rectangle = surface.get_rect(
            center=(WINDOW_WIDTH // 2, y)
        )

        self.screen.blit(
            surface,
            rectangle
        )

    def draw_score(self):

        font = pygame.font.Font(None, 32)

        score_text = font.render(
            f"Score: {self.score.value}",
            True,
            TEXT_COLOR
        )

        high_text = font.render(
            f"Best: {self.score.high_score}",
            True,
            TEXT_COLOR
        )

        self.screen.blit(
            score_text,
            (12, 10)
        )

        self.screen.blit(
            high_text,
            (
                WINDOW_WIDTH - high_text.get_width() - 12,
                10
            )
        )

    # --------------------------------------------------
    # MENUS
    # --------------------------------------------------

    def draw_start_screen(self):

        title_font = pygame.font.Font(None, 80)
        subtitle_font = pygame.font.Font(None, 34)
        small_font = pygame.font.Font(None, 26)

        self.draw_centered_text(
            "SNAKE",
            title_font,
            SNAKE_HEAD_COLOR,
            150
        )

        self.draw_centered_text(
            "Press ENTER to start",
            subtitle_font,
            TEXT_COLOR,
            240
        )

        self.draw_centered_text(
            "Arrow keys or WASD to move",
            small_font,
            SECONDARY_TEXT_COLOR,
            290
        )

        self.draw_centered_text(
            "ESC to quit",
            small_font,
            SECONDARY_TEXT_COLOR,
            325
        )

    def draw_game_over(self):

        overlay = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 170)
        )

        self.screen.blit(
            overlay,
            (0, 0)
        )

        title_font = pygame.font.Font(None, 70)
        score_font = pygame.font.Font(None, 38)
        small_font = pygame.font.Font(None, 28)

        self.draw_centered_text(
            "GAME OVER",
            title_font,
            GAME_OVER_COLOR,
            170
        )

        self.draw_centered_text(
            f"Score: {self.score.value}",
            score_font,
            TEXT_COLOR,
            240
        )

        self.draw_centered_text(
            "Press R to restart",
            small_font,
            TEXT_COLOR,
            300
        )

        self.draw_centered_text(
            "Press ESC to quit",
            small_font,
            SECONDARY_TEXT_COLOR,
            340
        )

    # --------------------------------------------------
    # MAIN DRAW
    # --------------------------------------------------

    def draw(self):

        self.screen.fill(
            BACKGROUND_COLOR
        )

        self.draw_grid()

        if not self.game_started:

            self.draw_start_screen()

        else:

            self.draw_snake()
            self.draw_food()
            self.draw_score()

            if self.game_over:
                self.draw_game_over()

    # --------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            pygame.display.flip()

            self.clock.tick(FPS)