import pygame

class SpikeSprite(pygame.Rect):
    """
    Classe de espinho com sprite/textura
    """
    def __init__(self, x, y, width, tileset_path=None):
        # Altura 25px para caber o sprite
        super().__init__(x, y, width, 25)
        
        self.image = pygame.Surface((width, 26), pygame.SRCALPHA)
        
        if tileset_path:
            try:
                tileset = pygame.image.load(tileset_path).convert_alpha()
                # Extrai tile de espinho do tileset
                tile_spike = tileset.subsurface((64, 105, 23, 12))
                
                # Repete tile de espinho
                quantity = (width // 16) + 1
                for i in range(quantity):
                    self.image.blit(tile_spike, (i * 16, 0))
            except:
                # Fallback para cor vermelha
                self.image.fill((255, 0, 0))
        else:
            # Cor vermelha padrão
            self.image.fill((255, 0, 0))
    
    def draw(self, screen, camera=None):
        """Desenha espinho na tela"""
        if camera:
            rect_visible = camera.apply(self)
            screen.blit(self.image, rect_visible)
        else:
            screen.blit(self.image, self)

