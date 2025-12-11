import pygame

class SpikeNoSprite(pygame.Rect):
    """
    Classe de espinho sem sprite - usa retângulo colorido simples
    """
    def __init__(self, x, y, width):
        # Altura padrão
        super().__init__(x, y, width, 25)
        self.color = (255, 0, 0)  # Vermelho
    
    def draw(self, screen, camera=None):
        """Desenha espinho na tela"""
        if camera:
            rect_visible = camera.apply(self)
            pygame.draw.rect(screen, self.color, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, self)

