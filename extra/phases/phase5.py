import pygame
from pygame.locals import *
import sys
import os

# Adiciona o diretório pai ao path para importar game_classes
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa classes do jogo (versões sem sprite, mas com câmera)
from game_classes.camera import Camera
from game_classes.player import PlayerNoSprite
from game_classes.enemy_no_sprite import EnemyNoSprite
from game_classes.platform_no_sprite import PlatformNoSprite
from game_classes.door import Door

def run_phase5():
    """
    Executa a fase 5 e retorna o resultado
    
    Esta fase introduz a câmera, que segue o jogador em um mundo maior que a tela
    """
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
    # try/except: Tenta carregar a imagem, se falhar usa fallback
    try:
        # pygame.image.load() - Carrega uma imagem de um arquivo
        # Retorna uma Surface com a imagem
        # .convert() - Converte para o formato de pixel da tela (mais rápido)
        background_img_original = pygame.image.load('extra/assets/background.jpg').convert()
        background_width = int(SCREEN_WIDTH * 1.4)  # Mundo 40% maior que a tela
        # pygame.transform.scale() - Redimensiona uma Surface
        # Parâmetros: (surface, (nova_largura, nova_altura))
        # Retorna uma nova Surface com o tamanho especificado
        background_extended = pygame.transform.scale(background_img_original, (background_width, SCREEN_HEIGHT))
    except pygame.error as e:
        # Se falhar ao carregar, cria uma superfície preta como fallback
        print(f"Erro ao carregar background: {e}")
        background_width = int(SCREEN_WIDTH * 1.4)
        # pygame.Surface() - Cria uma superfície vazia (imagem em branco)
        # Parâmetros: ((largura, altura), flags_opcionais)
        background_extended = pygame.Surface((background_width, SCREEN_HEIGHT))
        # .fill() - Preenche a superfície com uma cor
        background_extended.fill(BLACK)
    
    # --- Setup do Nível ---
    ground_height = 30
    collision_objects = []
    
    # 1. Chão
    # O chão usa background_width (maior que SCREEN_WIDTH) para permitir câmera
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
    # ground.top - Pega a coordenada Y do topo do chão
    final_door = Door(560, ground.top - final_size, final_size)
    
    # 4. Inimigo
    enemy_size = 25
    left_border = 100
    right_border = final_door.left - 20
    enemy = EnemyNoSprite(300, ground.top - enemy_size, enemy_size, left_border, right_border)
    
    # 5. Jogador
    player_size = 25
    # background_width: mundo maior que a tela
    player = PlayerNoSprite(50, ground.top - player_size, player_size, background_width)
    
    # 6. Câmera
    # Camera(largura_mundo, altura_mundo, largura_tela)
    # A câmera converte coordenadas do mundo para coordenadas da tela
    camera = Camera(background_width, SCREEN_HEIGHT, SCREEN_WIDTH)
    
    # --- Estados do Jogo ---
    passed = False
    died = False
    
    def restart_game():
        """Reinicia o jogo"""
        nonlocal passed, died
        player.reset()
        enemy.reset()
        passed = False
        died = False
    
    # --- Loop Principal ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return "quit"
            
            if not passed and not died:
                if event.type == pygame.KEYDOWN:
                    if (event.key == K_SPACE or event.key == K_w):
                        player.jump()
                    if event.key == K_e:
                        player.start_dash()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        restart_game()
                    elif event.key == K_n and passed:
                        pygame.quit()
                        return "next"
    
        if not passed and not died:
            # --- Atualizações ---
            player.update(collision_objects)
            enemy.update()
            # camera.update() - Atualiza a posição da câmera para seguir o jogador
            # A câmera calcula onde deve estar baseado na posição do jogador
            camera.update(player)
    
            # --- Colisões de Jogo ---
            if player.colliderect(enemy):
                died = True
            
            if player.colliderect(final_door):
                passed = True
    
            # --- Desenho ---
            # 1. Background (com parallax simples da câmera)
            # screen.blit() com área de recorte (terceiro parâmetro)
            # screen.blit(surface, posição_destino, área_origem)
            # (camera.x, 0, SCREEN_WIDTH, SCREEN_HEIGHT) define qual parte da imagem mostrar
            # Isso cria o efeito de "mover" o background conforme a câmera se move
            screen.blit(background_extended, (0, 0), (camera.x, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
            # 2. Objetos
            # Todos os objetos recebem a câmera para converter coordenadas mundo->tela
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
            font_large = pygame.font.SysFont('arial', 24, True, False)
            font_small = pygame.font.SysFont('arial', 18, False, False)
            
            title = font_large.render('FASE 5 COMPLETA!', True, (255, 255, 0))
            restart_text = font_small.render('R - Reiniciar Fase', True, (200, 200, 200))
            next_text = font_small.render('N - Proxima Fase', True, (200, 200, 200))
            esc_text = font_small.render('ESC - Sair', True, (150, 150, 150))
            
            screen.fill(BLACK)
            y_offset = SCREEN_HEIGHT // 2 - 60
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, y_offset))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, y_offset + 40))
            screen.blit(next_text, (SCREEN_WIDTH//2 - next_text.get_width()//2, y_offset + 65))
            screen.blit(esc_text, (SCREEN_WIDTH//2 - esc_text.get_width()//2, y_offset + 90))
    
        pygame.display.flip()
        clock.tick(65)
    
    pygame.quit()
    return "quit"