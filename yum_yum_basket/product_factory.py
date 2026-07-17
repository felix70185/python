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
    def create(self, x, y, level):

        random = Random()
        product = self.PRODUCTS.get(random.randint(1,2))
        # weighted_products = random.choices(self.PRODUCTS, weights=[10, 3, 1], k=5)

        product.x = x
        product.y = y
        speed = product.speed + level
        product.speed = speed

        return product

