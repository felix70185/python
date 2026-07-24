from product_factory import ProductFactory
import random
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        self.products_to_remove = []
        self._spawn_timer = 0
        self._spawn_interval = 1500 # ms
        self.product_factory = ProductFactory()

    def update(self, delta_time):
        self._spawn_timer += delta_time

        if self._spawn_timer >= self._spawn_interval:
            self._spawn_timer = 0

        for product in self.products:
            product.update(delta_time)

    def draw(self, screen):
        for product in self.products:
            if product.is_alive:
                product.draw(screen)

    def spawn(self, level):

        # Разделил на 4 секции
        number = random.randint(1, 4)
        x = number * 200 - 200 + Product.SIZE
        y = 0

        if len(self.products) == 0:
            product = self.product_factory.create(x, y, level) #level нужен что бы назначить скорость объекта
            self.products.append(product)

    def check_collision(self, basket, screen_height, state):
        for product in self.products:
            if product.is_dead:
                continue

            if product.rect.colliderect(basket.rect):
                product.on_catch(state)
                product.destroy()
            elif product.rect.bottom > screen_height:
                product.on_miss(state)
                product.destroy()

    def cleanup(self):
        alive_product = []
        for product in self.products:
            if product.is_alive:
                alive_product.append(product)

        self.products = alive_product

    def apply_changes(self, state):
        pass

    def product_count(self):
        return len(self.products)