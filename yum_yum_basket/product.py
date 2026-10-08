import pygame

class Product:
    SIZE = 30
    DEFAULT_SPEED = 200
    POINTS = 0
    IMAGE = 'apple.png'

    def __init__(self, x, y, speed, resource_manager):
        self._rect = pygame.Rect(x, y, self.SIZE, self.SIZE)
        self._is_alive = True
        self._speed = self.DEFAULT_SPEED if speed == 0 else speed
        self._img = resource_manager.load_image(self.IMAGE)

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
    def is_dead(self):
        return not self._is_alive

    @property
    def speed(self):
        return self._speed

    def update(self, delta_time):
        self._rect.y += self._speed*delta_time/1000

    def draw(self, screen):
        screen.blit(self._img, self._rect)

    def on_catch(self, state):
        state.add_score(self.POINTS)

    def on_miss(self, state):
        state.lose_lives()

    def destroy(self):
        self._is_alive = False