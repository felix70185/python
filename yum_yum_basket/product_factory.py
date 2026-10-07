
class ProductFactory:
    def __init__(self, resource_manager):
        self.level = 1
        self.resource_manager = resource_manager

    def create(self, product_type, x, y, speed):
        product = product_type(x, y, speed, self.resource_manager)
        product.rect.x = x
        product.rect.y = y

        return product

