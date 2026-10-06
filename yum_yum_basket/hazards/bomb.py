from product import Product

class Bomb(Product):
    COLOR = (0, 0, 0)

    def on_catch(self, state):
        state.lose_lives()

    def on_miss(self, state):
        pass