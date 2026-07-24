import pygame

from entities.basket import Basket
from game_state import GameState
from hud import HUD
from product_manager import ProductManager

class Game:
    WIDTH = 800
    HEIGHT = 600

    PRODUCTS = {}
    ENTITIES = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ням Ням Корзинка")
        self.state = GameState()
        self.font = pygame.font.Font(None, 28)
        self.hud = HUD(self.font)
        self.running = True

        self.basket = Basket(self.WIDTH, self.HEIGHT)
        self.ENTITIES.append(self.basket)
        self.product_manager = ProductManager()
        self.next_level_score = 3

    def run(self):

        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()

            delta_time = clock.tick(60)

            self.check_level_up()

            # TODO пока ограничила 1-м яблоком
            self.product_manager.spawn( self.state.level)
            self.product_manager.update(delta_time) # TODO Нужно передать delta_time сколько прошло времени/миллисекунд
            self.basket.update(delta_time)

            self.product_manager.check_collision(self.basket, self.HEIGHT, self.state)

            self.product_manager.cleanup()
            # TODO product_manager.apply_changes(state)

            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.basket.draw(self.screen)
        self.product_manager.draw(self.screen)
        self.hud.draw(self.screen, self.state)
        pygame.display.flip()


    def check_level_up(self):
        if self.state.score >= self.next_level_score:
            self.next_level_score = self.state.level*5
            self.state.level_up()