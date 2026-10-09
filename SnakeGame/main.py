import pygame
from game.game import SnakeGame

def main():
    pygame.init()
    game = SnakeGame()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
