import pygame
import sys

# ==============================================================================
# CONFIGURAÇÕES
# ==============================================================================

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40  # Tamanho da célula da grid (40x40 pixels)
FPS = 60

# Cores
WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)
TEXT_COLOR = (0, 150, 200)

# ==============================================================================
# FUNÇÕES DE DESENHO
# ==============================================================================

def draw_grid(surface):
    """Desenha a grid com base no TILE_SIZE."""
    # Linhas Verticais
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    
    # Linhas Horizontais
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_mouse_pos(surface, font):
    """Calcula a posição da grid com base no mouse e a desenha na tela."""
    
    # 1. Obter a posição do mouse em pixels
    mouse_x_pixel, mouse_y_pixel = pygame.mouse.get_pos()
    
    # 2. Converter para coordenada da Grid usando divisão inteira
    mouse_grid_x = mouse_x_pixel // TILE_SIZE
    mouse_grid_y = mouse_y_pixel // TILE_SIZE
    
    # 3. Preparar o texto para exibição
    text = f"Pixel: ({mouse_x_pixel}, {mouse_y_pixel}) | Grid: ({mouse_grid_x}, {mouse_grid_y})"
    text_surface = font.render(text, True, TEXT_COLOR)
    
    # 4. Desenhar o texto no canto superior esquerdo
    surface.blit(text_surface, (10, 10))


# ==============================================================================
# LOOP PRINCIPAL DO JOGO
# ==============================================================================

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Grid Viewer")
    clock = pygame.time.Clock()
    
    # Inicializa a fonte uma única vez
    font = pygame.font.Font(None, 30)

    while True:
        # Gerenciamento de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Desenho
        screen.fill(WHITE) 
        
        draw_grid(screen)
        draw_mouse_pos(screen, font)

        # Atualização da Tela
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()