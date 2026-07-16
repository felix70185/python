import pygame

from entities.basket import Basket
from game_state import GameState
from hud import HUD
from product import Product
from product_manager import ProductManager

class Game:
    WIDTH = 800
    HEIGHT = 600

    PRODUCTS = {}
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
        product_manager = ProductManager()

        clock = pygame.time.Clock()
        while self.running:
            delta_time = clock.tick(60)

            self.handle_events()

            product_manager.spawn(self.WIDTH - Product.SIZE, 0) # create new Obj
            product_manager.update(delta_time) # TODO Нужно передать delta_time сколько прошло времени/миллисекунд
            product_manager.check_collision(self.basket, self.state)
            # TODO Собрали яблоки для удаления
            # TODO product_manager.apply_changes(state)

            # TODO Повышаем уровень каждые 30 очков

            # product.on_catch(self.state)

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