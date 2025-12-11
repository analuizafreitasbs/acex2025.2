import pygame

class EnemyNoSprite(pygame.Rect):
    """
    Classe de inimigo sem sprite - usa retângulo colorido simples
    """
    def __init__(self, x, y, size, limit_left, limit_right, speed=3):
        super().__init__(x, y, size, size)
        self.color = (255, 0, 255)  # Magenta
        self.base_speed = speed  # Velocidade base
        self.speed = speed  # Velocidade atual
        self.limit_left = limit_left  # Limite esquerdo da patrulha
        self.limit_right = limit_right  # Limite direito da patrulha
        
        # Posição inicial para reset
        self.start_x = x
        self.start_y = y
    
    def update(self):
        """Atualiza posição do inimigo"""
        self.x += self.speed
        
        # Lógica de patrulha
        if self.left <= self.limit_left and self.speed < 0:
            self.speed *= -1
        elif self.right >= self.limit_right and self.speed > 0:
            self.speed *= -1
    
    def reset(self):
        """Reseta inimigo para posição inicial"""
        self.x = self.start_x
        self.y = self.start_y
        self.speed = abs(self.base_speed)
    
    def draw(self, screen, camera=None):
        """Desenha inimigo na tela"""
        if camera:
            rect_visible = camera.apply(self)
            pygame.draw.rect(screen, self.color, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, self)

