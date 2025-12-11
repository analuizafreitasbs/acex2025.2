import pygame
try:
    from .support import import_cut_graphics
except ImportError:
    # Fallback se import relativo falhar
    from support import import_cut_graphics

class Tile(pygame.Rect):
    """
    Classe de tile - elemento básico de construção de níveis usando tileset
    """
    def __init__(self, x, y, tile_size, tile_index, tileset_path, tiles_list=None):
        """
        Inicializa um tile
        
        Args:
            x: Posição X no mundo
            y: Posição Y no mundo
            tile_size: Tamanho do tile (largura e altura)
            tile_index: Índice do tile no tileset (qual tile usar)
            tileset_path: Caminho para o arquivo do tileset
            tiles_list: Lista opcional de tiles já carregados (para reutilização)
        """
        super().__init__(x, y, tile_size, tile_size)
        self.tile_size = tile_size
        self.tile_index = tile_index
        
        # Carrega o tile
        if tiles_list is not None:
            # Usa lista de tiles já carregada
            if 0 <= tile_index < len(tiles_list):
                self.tile_surface = tiles_list[tile_index]
            else:
                # Tile inválido, cria superfície vermelha de erro
                self.tile_surface = pygame.Surface((tile_size, tile_size))
                self.tile_surface.fill((255, 0, 0))
        else:
            # Carrega tileset e extrai o tile específico
            tiles = import_cut_graphics(tileset_path, tile_size)
            if 0 <= tile_index < len(tiles):
                self.tile_surface = tiles[tile_index]
            else:
                # Tile inválido, cria superfície vermelha de erro
                self.tile_surface = pygame.Surface((tile_size, tile_size))
                self.tile_surface.fill((255, 0, 0))
    
    def draw(self, screen, camera=None):
        """Desenha o tile na tela"""
        if camera:
            rect_visible = camera.apply(self)
            screen.blit(self.tile_surface, rect_visible)
        else:
            screen.blit(self.tile_surface, self)


class TileMap:
    """
    Classe para gerenciar um mapa de tiles completo
    """
    def __init__(self, tileset_path, tile_size=32):
        """
        Inicializa um mapa de tiles
        
        Args:
            tileset_path: Caminho para o arquivo do tileset
            tile_size: Tamanho de cada tile
        """
        self.tileset_path = tileset_path
        self.tile_size = tile_size
        self.tiles = import_cut_graphics(tileset_path, tile_size)
        self.tile_map = {}  # Dicionário: (x, y) -> tile_index
    
    def set_tile(self, x, y, tile_index):
        """
        Define um tile em uma posição específica
        
        Args:
            x: Posição X no grid
            y: Posição Y no grid
            tile_index: Índice do tile a usar
        """
        self.tile_map[(x, y)] = tile_index
    
    def get_tile_objects(self):
        """
        Retorna lista de objetos Tile para desenhar
        
        Returns:
            Lista de objetos Tile
        """
        tile_objects = []
        for (grid_x, grid_y), tile_index in self.tile_map.items():
            world_x = grid_x * self.tile_size
            world_y = grid_y * self.tile_size
            tile = Tile(world_x, world_y, self.tile_size, tile_index, 
                       self.tileset_path, self.tiles)
            tile_objects.append(tile)
        return tile_objects
    
    def draw(self, screen, camera=None):
        """Desenha todos os tiles do mapa"""
        for tile_obj in self.get_tile_objects():
            tile_obj.draw(screen, camera)

