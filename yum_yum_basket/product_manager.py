from product import Product
from product_factory import ProductFactory

class ProductManager:
    def __init__(self):
        self.products = []
        self.products_to_remove = []
        self._spawn_timer = 0
        self._spawn_interval = 1500 # ms

    def update(self, delta_time):
        self._spawn_timer += delta_time

        if self._spawn_timer >= self._spawn_interval:
            #self.spawn()
            self._spawn_timer = 0

        for product in self.products:
            product.update()

    def draw(self, screen):
        for product in self.products:
            if product.is_alive:
                product.draw(screen)

    def spawn(self, x, y, level):
        product_factory = ProductFactory()

        if len(self.products) == 0:
            product = product_factory.create(x, y, level) #level нужен что бы назначить скорость объекта
            self.products.append(product)

    def check_collision(self, basket, state):
        for product in self.products:
            if product.rect.colliderect(basket.rect) and product.is_alive:
                product.on_catch(state)
                product.destroy()

    def check_screen_collision(self, screen_height, state):
        for product in self.products:
            if product.rect.bottom > screen_height and product.is_alive:
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