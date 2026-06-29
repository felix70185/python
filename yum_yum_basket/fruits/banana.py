from game_object import GameObject

class Banana(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 'yellow', 5)

    def draw(self):
        print(__name__)