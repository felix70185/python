
# Интерфейс игрока
class HUD:
    # Цвета
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    def __init__(self, font):
        self.font = font

    def draw(self, screen, game_state):
        self.draw_text(screen, f"Счёт: {game_state.score}", 10, 10, self.WHITE)
        self.draw_text(screen, f"Жизни: {game_state.lives}", 10, 40, self.WHITE)
        self.draw_text(screen, f"Уровень: {game_state.level}", 10, 70, self.WHITE)

    def draw_text(self, screen, text, x, y, color = (255, 255, 255)):
        surface = self.font.render(text, True, color)
        screen.blit(surface, (x, y))
