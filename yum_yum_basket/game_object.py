from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x, y, size, color, speed):
        """
        Эта функция складывает два числа.
        :param x: Координаты
        :param y: Координаты
        :param size: Размер
        :param color: Цвет
        :param speed: Скорость объекта
        :return:
        """
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        """
        Метод для смещения объекта вниз
        :return: bool вышел за пределы или нет
        """
        self.y += self.speed
        return self.y > 800

    @abstractmethod
    def draw(self):
        pass