import pygame

class Product:
    SIZE = 30
    SPEED = 5
    COLOR = (255, 255, 255)
    POINTS = 0

    def __init__(self, x, y):
        self._rect = pygame.Rect(x, y, self.SIZE, self.SIZE)

    @property
    def rect(self):
        return self._rect

    def update(self):
        self._rect.y += self.SPEED

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.COLOR,
            self._rect
        )

    @property
    def points(self):
        return self.POINTS