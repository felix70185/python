import pygame

from entities.basket import Basket


class Game:
    WIDTH = 800
    HEIGHT = 600
    # Цвета
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ням Ням Корзинка")
        self.font = pygame.font.Font(None, 28)
        self.score = 0
        self.lives = 3
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.draw_text(f"Счёт: {self.score}", 10, 10, self.WHITE)
        self.draw_text(f"Жизни: {self.lives}", self.WIDTH - 100, 10, self.WHITE)
        pygame.display.flip()

    def draw_text(self, text, x, y, color = (255, 255, 255)):
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x, y))