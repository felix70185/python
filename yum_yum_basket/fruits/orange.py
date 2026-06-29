from game_object import GameObject

class Orange(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 'orange', 10)

    def draw(self):
        print(__name__)