"""
Módulo de Classes do Jogo

Este módulo contém todas as classes do jogo usadas nas diferentes fases.
"""

# Player classes
from .player import PlayerNoSprite
from .player_sprite import PlayerSprite

# Enemy classes
from .enemy_no_sprite import EnemyNoSprite
from .enemy_sprite import EnemySprite

# Platform classes
from .platform_no_sprite import PlatformNoSprite
from .platform_sprite import PlatformSprite

# Spike classes
from .spike_no_sprite import SpikeNoSprite
from .spike_sprite import SpikeSprite

# Other classes
from .door import Door
from .camera import Camera
from .tile import Tile, TileMap
from .support import import_cut_graphics

# Backward compatibility - mantém Spike antigo se existir
try:
    from .spike import Spike
except ImportError:
    # Se não existir, usa SpikeSprite como fallback
    Spike = SpikeSprite

__all__ = [
    # Player
    'PlayerNoSprite',
    'PlayerSprite',
    # Enemy
    'EnemyNoSprite',
    'EnemySprite',
    # Platform
    'PlatformNoSprite',
    'PlatformSprite',
    # Spike
    'SpikeNoSprite',
    'SpikeSprite',
    'Spike',  # Backward compatibility (se existir)
    # Other
    'Door',
    'Camera',
    'Tile',
    'TileMap',
    'import_cut_graphics'
]
