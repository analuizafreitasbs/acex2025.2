import pygame
import os

def import_cut_graphics(path, tile_size=32):
    """
    Carrega e corta um tileset em tiles individuais
    
    Args:
        path: Caminho para o arquivo do tileset
        tile_size: Tamanho de cada tile (largura e altura)
    
    Returns:
        Lista de superfícies, cada uma representando um tile
    """
    full_path = path
    
    try:
        # Tenta carregar a imagem principal
        surface = pygame.image.load(full_path).convert_alpha()
    except pygame.error as e:
        # Se falhar, imprime erro e retorna lista vazia
        print(f"ERRO CRÍTICO DE CARREGAMENTO! Verifique se o arquivo existe no caminho: {os.path.abspath(full_path)}")
        return []

    # Define as dimensões do corte
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    
    # Corta o tileset
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            
            # Cria uma nova superfície para cada tile
            new_surface = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            
            # Copia a área do tile da superfície principal para a nova superfície
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            
            cut_tiles.append(new_surface)

    return cut_tiles

