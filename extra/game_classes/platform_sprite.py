import pygame

class PlatformSprite(pygame.Rect):
    """
    Classe de plataforma com textura/sprite
    """
    def __init__(self, x, y, width, height, color, texture_path=None, tileset_path=None):
        super().__init__(x, y, width, height)
        self.color = color  # Cor base
        
        # Cria superfície para textura
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.has_texture = False
        
        # Carrega textura se fornecida
        if texture_path:
            try:
                texture = pygame.image.load(texture_path).convert_alpha()
                self.image = pygame.transform.scale(texture, (width, height))
                self.has_texture = True
            except:
                self.image.fill(color)
        
        # Lógica especial para plataformas baseadas em tileset
        elif tileset_path:
            try:
                # Plataformas verdes (chão)
                if color == (0, 255, 0):
                    tileset = pygame.image.load(tileset_path).convert_alpha()
                    # Extrai tile de grama
                    tile_grass = tileset.subsurface((68, 184, 27, 7))
                    tile_grass = pygame.transform.scale(tile_grass, (height, height))
                    
                    # Repete tile de grama
                    quantity = (width // height) + 1
                    for i in range(quantity):
                        self.image.blit(tile_grass, (i * height, 0))
                    self.has_texture = True
                
                # Plataformas amarelas (voadoras)
                elif color == (255, 255, 0):
                    try:
                        sprites_amb = pygame.image.load("extra/assets/sprites-ambiente.png").convert_alpha()
                        # Extrai galho
                        branch = sprites_amb.subsurface((155, 28, 21, 7))
                        self.image = pygame.transform.scale(branch, (width, height))
                        self.has_texture = True
                    except:
                        self.image.fill(color)
            except:
                self.image.fill(color)
        
        if not self.has_texture:
            self.image.fill(color)
    
    def draw(self, screen, camera=None):
        """Desenha plataforma na tela"""
        if camera:
            rect_visible = camera.apply(self)
            screen.blit(self.image, rect_visible)
        else:
            screen.blit(self.image, self)

