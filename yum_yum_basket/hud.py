
class HUD:
    def __init__(self, font):
        self.font = font

    def draw(self, screen, gameState):
        self.draw_text(screen, f"Счёт: {gameState.score}", 10, 10, self.WHITE)
        self.draw_text(screen, f"Жизни: {gameState.lives}", self.WIDTH - 100, 10, self.WHITE)

    def draw_text(self, screen, text, x, y, color = (255, 255, 255)):
        surface = self.font.render(text, True, color)
        screen.blit(surface, (x, y))