# Apple object
# functions: move, finish, build,

from game_object import GameObject

class Apple(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 'Green', 10)

    def draw(self):
        """
        Метод для смещения объекта вниз
        :return: bool вышел за пределы границ или нет
        """
        print("Apple displayed")
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)