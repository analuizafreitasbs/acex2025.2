import pygame

class Door(pygame.Rect):
    """
    Classe de porta - objetivo/saída do nível
    """
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.color = (0, 0, 0)  # Preto
    
    def draw(self, screen, camera=None):
        """Desenha porta na tela"""
        if camera:
            rect_visible = camera.apply(self)
            pygame.draw.rect(screen, self.color, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, self)

