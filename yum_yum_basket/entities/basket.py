import pygame
from entity import Entity

class Basket(Entity):
    WIDTH = 120
    HEIGHT = 25
    SPEED = 7

    def __init__(self, screen_width, screen_height):
        x = (screen_width - Basket.WIDTH) // 2
        y = screen_height - 60

        super().__init__(x, y, self.WIDTH, self.HEIGHT)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.SPEED

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (30,170,255),
            self.rect
        )