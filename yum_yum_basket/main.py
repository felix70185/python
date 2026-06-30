# This is a sample Python script.
from fruits.apple import Apple
from entity import GameObject

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Яблоня с которой падают яблоки и червячки или яблоко из кот выходит червяк ), бомобочки
# Курицы с кот падают яйца
# Ням Ням Корзинка
from game import Game

def main():
    print('Ням Ням Корзинка')
    print(__name__)  # Press Ctrl+F8 to toggle the breakpoint.
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
