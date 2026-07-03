class ProductManager:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def update(self):
        for product in self.products:
            product.update()

    def draw(self, screen):
        for product in self.products:
            product.draw(screen)

    def spawn(self):
        # product = ProductFactory.create()
        # self.add(product)
        self.add(self)