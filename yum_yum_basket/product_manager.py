from product_factory import ProductFactory
import random
from product import Product

class ProductManager:
    LEVEL_CONFIG = {
        1: {
            "spawn_interval": 3500,
            "speed": 200,
        },
        2: {
            "spawn_interval": 2500,
            "speed": 240,
        },
        3: {
            "spawn_interval": 1500,
            "speed": 280,
        },
    }

    def __init__(self):
        self.products = []
        self._spawn_timer = 0
        self.product_factory = ProductFactory()

    def update(self, delta_time, state):
        self._spawn_timer += delta_time

        level_config = self.get_level_config(state.level)

        if self._spawn_timer >= level_config["spawn_interval"]:
            self.spawn(level_config["speed"])
            self._spawn_timer = 0

        for product in self.products:
            product.update(delta_time)

    def draw(self, screen):
        for product in self.products:
            if product.is_alive:
                product.draw(screen)

    def spawn(self, speed):

        # Разделил на 4 секции
        number = random.randint(1, 4)
        x = number * 200 - 200 + Product.SIZE
        y = 0

        product = self.product_factory.create(x, y, speed)
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

    def get_level_config(self, level):
        max_lvl = max(self.LEVEL_CONFIG.keys())
        lvl = max_lvl if level > max_lvl else level
        return self.LEVEL_CONFIG[lvl]