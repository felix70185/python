import pygame

from entities.basket import Basket
from game_state import GameState
from hud import HUD
from product import Product
from product_manager import ProductManager

class Game:
    WIDTH = 800
    HEIGHT = 600
    entities = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ням Ням Корзинка")
        self.state = GameState()
        self.font = pygame.font.Font(None, 28)
        self.hud = HUD(self.font)
        self.running = True

        self.basket = Basket(self.WIDTH, self.HEIGHT)
        self.entities.append(self.basket)

    def run(self):
        while self.running:
            self.handle_events()

            product_manager = ProductManager()

            product_manager.spawn(self.WIDTH - Product.SIZE, 0) # create new Obj
            product_manager.update()


            # Если продукт попал в корзину
            # product.rect.colliderect(self.basket.rect)
            # product_manager.remove(product)

            # Если продукт попал за линию
            # product_manager.remove(product)
            
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.hud.draw(self.screen, self.state)
        pygame.display.flip()