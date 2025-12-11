import pygame
from pygame.locals import *

# Importa classes do jogo (versões sem sprite)
from game_classes.player import PlayerNoSprite
from game_classes.enemy_no_sprite import EnemyNoSprite
from game_classes.platform_no_sprite import PlatformNoSprite
from game_classes.door import Door

pygame.init()

# --- Configuração da Fase 4 ---
# Tela grande fixa
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Phase 4')
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# --- Criando o Mundo ---

# 1. Chão e Plataformas
ground_height = 50
# Lista para passar ao jogador para checagem de colisão
collision_objects = []

# Chão
ground = PlatformNoSprite(0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height, GREEN)
collision_objects.append(ground)

# Plataformas (Posições originais da Fase 4)
plat_coords = [
    (150, SCREEN_HEIGHT - ground_height - 100, 200, 20),
    (400, SCREEN_HEIGHT - ground_height - 200, 150, 20),
    (650, SCREEN_HEIGHT - ground_height - 300, 200, 20)
]
for (x, y, w, h) in plat_coords:
    p = PlatformNoSprite(x, y, w, h, YELLOW)
    collision_objects.append(p)

# 2. Saída
final_size = 100
final_door = Door(SCREEN_WIDTH - final_size, SCREEN_HEIGHT - ground_height - final_size, final_size)

# 3. Inimigo
enemy_size = 40
# Limites da patrulha (Começo da tela até antes da porta)
right_border = 600
door_limit = SCREEN_WIDTH - final_size
enemy = EnemyNoSprite(right_border, 
                      SCREEN_HEIGHT - ground_height - enemy_size, 
                      enemy_size, 
                      0,
                      door_limit, 
                      speed=0)

# 4. Jogador
player_size = 50
player = PlayerNoSprite(0, 0, player_size, SCREEN_WIDTH)
player.bottomleft = ground.topleft  # Posiciona no chão

# --- Variáveis de Controle ---
passed = False
died = False

def restart_game():
    """Reinicia o jogo"""
    global passed, died
    # Reset do jogador
    player.reset()
    # Reset do inimigo
    enemy.reset()
    
    passed = False
    died = False

# --- Loop Principal ---
running = True
while running:
    # 1. Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not passed and not died:
            if event.type == pygame.KEYDOWN:
                if (event.key == K_SPACE or event.key == K_w):
                    player.jump()
                if event.key == K_e:
                    player.start_dash()
        else:
            if event.type == pygame.KEYDOWN and event.key == K_r:
                restart_game()

    # 2. Lógica de Jogo
    if not passed and not died:
        player.update(collision_objects)
        enemy.update()

        if player.colliderect(enemy):
            died = True
        
        if player.colliderect(final_door):
            passed = True

        # 3. Desenho (Render)
        screen.fill(BLUE)  # Fundo azul simples
        
        # Desenha tudo diretamente (sem câmera)
        for obj in collision_objects:
            obj.draw(screen)
            
        final_door.draw(screen)
        enemy.draw(screen)
        player.draw(screen)

    # 4. Telas de Game Over / Vitória
    elif died:
        font = pygame.font.SysFont('arial', 20, True, True)
        text = font.render('You died!! Press R to retry', True, WHITE)
        screen.fill(RED)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT // 2))

    elif passed:
        font = pygame.font.SysFont('arial', 20, True, False)
        text = font.render('Congratulations! Press R to Repeat.', True, WHITE)
        screen.fill(BLACK)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(65)

pygame.quit()
