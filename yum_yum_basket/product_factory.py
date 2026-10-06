from random import Random

from fruits.apple import Apple

class ProductFactory:

    def __init__(self):
        self.level = 1

    @classmethod
    def create(self, product_type, x, y, speed):
        random = Random()
        #product = self.PRODUCTS.get(level)[random.randint(0,1)]
        #product = Apple(x, y)
        # weighted_products = random.choices(self.PRODUCTS, weights=[10, 3, 1], k=5)

        product = product_type(x, y)
        product.rect.x = x
        product.rect.y = y
        #product.speed = speed

        return product

