import pygame

class Entity():
    def __init__(self, x, y, width, height):
        self._rect = pygame.Rect(x, y, width, height)

    @property
    def rect(self):
        return self._rect

    def update(self):
        pass

    def draw(self, screen):
        raise NotImplementedError()
