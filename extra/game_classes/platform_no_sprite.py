import pygame

class PlatformNoSprite(pygame.Rect):
    """
    Classe de plataforma sem sprite - usa retângulo colorido simples
    """
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
    
    def draw(self, screen, camera=None):
        """Desenha plataforma na tela"""
        if camera:
            rect_visible = camera.apply(self)
            pygame.draw.rect(screen, self.color, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, self)

