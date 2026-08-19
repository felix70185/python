from random import Random

from fruits.apple import Apple
from fruits.banana import Banana
from hazards.bomb import Bomb

class ProductFactory:
    PRODUCTS = {
        1: [
            (Apple, 90),
            (Banana, 10)
        ],
        2: [
            (Apple, 60),
            (Banana, 30),
            (Bomb, 10)
        ],
    }

    def __init__(self):
        self.level = 1

    @classmethod
    def create(self, x, y, speed):
        random = Random()
        #product = self.PRODUCTS.get(level)[random.randint(0,1)]
        product = Apple(x, y)
        # weighted_products = random.choices(self.PRODUCTS, weights=[10, 3, 1], k=5)

        product.rect.x = x
        product.rect.y = y
        #product.speed = speed

        return product

