import pygame
from pygame.locals import *

# Importa classes do jogo (versões sem sprite, mas com câmera)
from game_classes.camera import Camera
from game_classes.player import PlayerNoSprite
from game_classes.enemy_no_sprite import EnemyNoSprite
from game_classes.platform_no_sprite import PlatformNoSprite
from game_classes.door import Door

pygame.init()

# --- Configuração da Tela ---
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Phase 5 - Modularized')
clock = pygame.time.Clock()

# --- Cores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# --- Carregamento de Assets ---
# Mantém isso aqui para passar a imagem ao loop de desenho
try:
    background_img_original = pygame.image.load('extra/assets/background.jpg').convert()
    background_width = int(SCREEN_WIDTH * 1.4)
    background_extended = pygame.transform.scale(background_img_original, (background_width, SCREEN_HEIGHT))
except pygame.error as e:
    print(f"Erro ao carregar background: {e}")
    background_width = int(SCREEN_WIDTH * 1.4)
    background_extended = pygame.Surface((background_width, SCREEN_HEIGHT))
    background_extended.fill(BLACK)

# --- Setup do Nível ---
ground_height = 30
# Lista de objetos que colidem (Chão + Plataformas)
collision_objects = []

# 1. Chão
ground = PlatformNoSprite(0, SCREEN_HEIGHT - ground_height, background_width, ground_height, GREEN)
collision_objects.append(ground)

# 2. Plataformas Flutuantes
plats_coords = [
    (80, SCREEN_HEIGHT - ground_height - 60, 100, 15),
    (260, SCREEN_HEIGHT - ground_height - 120, 120, 15),
    (450, SCREEN_HEIGHT - ground_height - 80, 100, 15)
]
for (x, y, w, h) in plats_coords:
    p = PlatformNoSprite(x, y, w, h, YELLOW)
    collision_objects.append(p)

# 3. Saída (Porta)
final_size = 30
final_door = Door(560, ground.top - final_size, final_size)

# 4. Inimigo
enemy_size = 25
left_border = 100
right_border = final_door.left - 20
# Inicia no meio (300)
enemy = EnemyNoSprite(300, ground.top - enemy_size, enemy_size, left_border, right_border)

# 5. Jogador
player_size = 25
player = PlayerNoSprite(50, ground.top - player_size, player_size, background_width)

# 6. Câmera
camera = Camera(background_width, SCREEN_HEIGHT, SCREEN_WIDTH)

# --- Estados do Jogo ---
passed = False
died = False

def restart_game():
    """Reinicia o jogo"""
    global passed, died
    player.reset()
    enemy.reset()
    passed = False
    died = False

# --- Loop Principal ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not passed and not died:
            if event.type == pygame.KEYDOWN:
                # Pulo
                if (event.key == K_SPACE or event.key == K_w):
                    player.jump()
                # Avanço
                if event.key == K_e:
                    player.start_dash()
        else:
            # Reiniciar se morreu ou ganhou
            if event.type == pygame.KEYDOWN and event.key == K_r:
                restart_game()

    if not passed and not died:
        # --- Atualizações ---
        player.update(collision_objects)
        enemy.update()
        camera.update(player)

        # --- Colisões de Jogo ---
        if player.colliderect(enemy):
            died = True
        
        if player.colliderect(final_door):
            passed = True

        # --- Desenho ---
        # 1. Background (com parallax simples da câmera)
        screen.blit(background_extended, (0, 0), (camera.x, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        # 2. Objetos
        for obj in collision_objects:
            obj.draw(screen, camera)
        
        final_door.draw(screen, camera)
        enemy.draw(screen, camera)
        player.draw(screen, camera)

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
