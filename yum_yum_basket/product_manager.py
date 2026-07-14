from product_factory import ProductFactory


class ProductManager:
    def __init__(self):
        self.products = []
        self.products_to_remove = []

    def add(self, product):
        self.products.append(product)

    def update(self):
        for product in self.products:
            product.update()

    def draw(self, screen):
        for product in self.products:
            product.draw(screen)

    def spawn(self, x, y):
        product_factory = ProductFactory()
        product = product_factory.create(x, y)
        self.add(product)

    def check_collision(self, basket, state):
        for product in self.products:
            product.rect.colliderect(basket.rect)

    def remove(self, product):
        self.products_to_remove += [product]

    def products_to_remove_clear(self):
        for product in self.products_to_remove:
            product.remove()

    def apply_changes(self, state):
        pass