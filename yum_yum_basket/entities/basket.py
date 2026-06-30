from entity import Entity

class Basket(Entity):
    def __init__(self):
        super().__init__(100, 0, 10, 'Brown', 1)

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self):
        pass
