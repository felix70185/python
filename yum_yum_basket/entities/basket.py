import pygame
from entity import Entity

class Basket(Entity):
    WIDTH = 90
    HEIGHT = 25
    SPEED = 600

    def __init__(self, screen_width, screen_height):
        x = (screen_width - Basket.WIDTH) // 2
        y = screen_height - 60
        self.screen_width = screen_width
        self.screen_height = screen_height

        super().__init__(x, y, self.WIDTH, self.HEIGHT)

    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.SPEED * delta_time / 1000

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.SPEED * delta_time / 1000

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (30,170,255),
            self.rect
        )