import pygame

class Camera:
    """
    Classe de câmera - gerencia rolagem e conversão de coordenadas mundo-para-tela
    """
    def __init__(self, world_width, world_height, screen_width):
        """
        Inicializa câmera
        
        Args:
            world_width: Largura total do mundo
            world_height: Altura total do mundo
            screen_width: Largura da tela
        """
        self.camera_rect = pygame.Rect(0, 0, world_width, world_height)
        self.width = world_width
        self.height = world_height
        self.screen_width = screen_width
        self.x = 0  # Posição X da câmera
    
    def update(self, target_rect, offset_ratio=3):
        """
        Atualiza câmera para seguir alvo
        
        Args:
            target_rect: Alvo para seguir (geralmente jogador)
            offset_ratio: Divisor (ex: 3 para jogador a 1/3 da tela)
        """
        target_x = target_rect.x - (self.screen_width // offset_ratio)
        
        # Limitar câmera (não sair do mundo)
        self.x = max(0, min(target_x, self.width - self.screen_width))
        self.camera_rect.x = self.x
    
    def apply(self, entity_rect):
        """
        Converte coordenadas do mundo para coordenadas da tela
        
        Args:
            entity_rect: Retângulo da entidade em coordenadas do mundo
            
        Returns:
            Novo Rect deslocado pela câmera para desenhar
        """
        return entity_rect.move(-self.x, 0)
