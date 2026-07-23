import pygame

class Product:
    SIZE = 30
    SPEED = 5
    COLOR = (255, 255, 255)
    POINTS = 0

    def __init__(self, x, y, speed = 0):
        self._rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self._is_alive = True
        self.SPEED = self.SPEED if speed == 0 else speed

    @property
    def rect(self):
        return self._rect

    @property
    def points(self):
        return self.POINTS

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def speed(self):
        return self.SPEED

    def update(self):
        self._rect.y += self.SPEED

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.COLOR,
            self._rect
        )

    def on_catch(self, state):
        state.add_score(self.POINTS)

    def on_miss(self, state):
        state.lose_lives()

    def destroy(self):
        self._is_alive = False