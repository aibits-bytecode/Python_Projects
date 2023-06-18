import time
import random
import pygame
from pygame.locals import *
import apple
import snake

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


class Game:
    # constructor
    def __init__(self):
        pygame.init()
        # Create the display window
        self.surface = pygame.display.set_mode((1000, 800))
        # fill the screen with color
        self.surface.fill(BACKGROUND_COLOR)
        self.snake = snake.Snake(self.surface, 1)
        self.snake.draw()
        self.apple = apple.Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # check snake ate the apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            print("Collision occured")
            self.apple.move()
            self.snake.increase_length()

        # check snake at him self
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print("game over")
                raise "game over"

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Your score : {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score : {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                            self.snake.direction = 'up'
                        if event.key == K_DOWN:
                            self.snake.move_down()
                            self.snake.direction = 'down'
                        if event.key == K_LEFT:
                            self.snake.move_left()
                            self.snake.direction = 'left'
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                            self.snake.direction = 'right'
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(0.2)

    def reset(self):
        self.snake = snake.Snake(self.surface, 1)
        self.apple = apple.Apple(self.surface)


if __name__ == "__main__":
    game = Game()
    game.run()
