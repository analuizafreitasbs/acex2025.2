import pygame

class EnemySprite(pygame.Rect):
    """
    Classe de inimigo com sprite
    """
    def __init__(self, x, y, size, limit_left, limit_right, speed=3, sprite_path=None):
        super().__init__(x, y, size, size)
        self.color = (255, 0, 255)  # Magenta (fallback)
        self.base_speed = speed  # Velocidade base
        self.speed = speed  # Velocidade atual
        self.limit_left = limit_left  # Limite esquerdo da patrulha
        self.limit_right = limit_right  # Limite direito da patrulha
        
        # Posição inicial para reset
        self.start_x = x
        self.start_y = y
        
        # Sprite
        self.sprite_original = None
        self.current_sprite = None
        self.has_sprite = False
        
        if sprite_path:
            try:
                img = pygame.image.load(sprite_path).convert_alpha()
                self.sprite_original = pygame.transform.scale(img, (size, size))
                self.current_sprite = self.sprite_original
                self.has_sprite = True
            except:
                # Mantém cor magenta se sprite falhar
                pass
    
    def update(self):
        """Atualiza posição do inimigo"""
        self.x += self.speed
        
        # Lógica de patrulha
        if self.left <= self.limit_left and self.speed < 0:
            self.speed *= -1
        elif self.right >= self.limit_right and self.speed > 0:
            self.speed *= -1
        
        # Vira sprite baseado na direção
        if self.has_sprite and self.sprite_original:
            if self.speed > 0:  # Indo para direita
                self.current_sprite = pygame.transform.flip(self.sprite_original, True, False)
            else:  # Indo para esquerda
                self.current_sprite = self.sprite_original
    
    def reset(self):
        """Reseta inimigo para posição inicial"""
        self.x = self.start_x
        self.y = self.start_y
        self.speed = abs(self.base_speed)
    
    def draw(self, screen, camera=None):
        """Desenha inimigo na tela"""
        if camera:
            rect_visible = camera.apply(self)
        else:
            rect_visible = self
        
        if self.has_sprite and self.current_sprite:
            screen.blit(self.current_sprite, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, rect_visible)

