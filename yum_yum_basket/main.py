# This is a sample Python script.
from fruits.apple import Apple
from game_object import GameObject

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Яблоня с которой падают яблоки и червячки или яблоко из кот выходит червяк ), бомобочки
# Курицы с кот падают яйца
# Ням Ням Корзинка

import pygame

def main():
    print('Ням Ням Корзинка')
    print(__name__)  # Press Ctrl+F8 to toggle the breakpoint.
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ням Ням Корзинка")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
