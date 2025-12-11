import pygame
from pygame.locals import *
import sys
import os

# Adiciona o diretório pai ao path para importar game_classes
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa classes do jogo (versões com sprite)
from game_classes.camera import Camera
from game_classes.player_sprite import PlayerSprite
from game_classes.enemy_sprite import EnemySprite
from game_classes.platform_sprite import PlatformSprite
from game_classes.door import Door
from game_classes.spike_sprite import SpikeSprite

def run_phase6():
    """Executa a fase 6 e retorna o resultado"""
    pygame.init()
    
    # --- Configuração Tela ---
    SCREEN_WIDTH = 640  # Mantém resolução "Retro" da Fase 5
    SCREEN_HEIGHT = 360
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Phase 6')
    clock = pygame.time.Clock()
    
    # --- Assets ---
    try:
        bg_original = pygame.image.load('extra/assets/background.jpg').convert()
        # 1. Redimensiona imagem para tamanho exato da TELA (fica com proporção bonita)
        bg_screen_sized = pygame.transform.scale(bg_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
        # Se der erro, cria quadrado preto
        bg_screen_sized = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        bg_screen_sized.fill((20, 20, 40))
    
    # 2. MUNDO GIGANTE (5000 pixels de largura)
    WORLD_WIDTH = 5000
    
    # 3. Criamos superfície vazia gigante
    bg_extended = pygame.Surface((WORLD_WIDTH, SCREEN_HEIGHT))
    
    # 4. Desenhamos imagem repetida (lado a lado) até preencher tudo
    # Calculamos quantas vezes imagem cabe no mundo
    tiles = (WORLD_WIDTH // SCREEN_WIDTH) + 1 
    
    # Loop repete a imagem lado a lado
    for i in range(tiles):
        # bg_extended.blit() - Desenha uma Surface em outra Surface
        # Parâmetros: (surface_origem, posição_destino)
        # i * SCREEN_WIDTH: posiciona cada cópia ao lado da anterior
        bg_extended.blit(bg_screen_sized, (i * SCREEN_WIDTH, 0))
    
    # --- Cores ---
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    
    # --- CONSTRUINDO O NÍVEL ---
    ground_h = 30
    collision_objects = []  # Chão e Plataformas
    death_objects = []      # Espinhos
    enemies = []            # Lista de inimigos
    
    # ==========================================
    # SETOR 1: O AQUECIMENTO (0 a 1000px)
    # ==========================================
    # Chão inicial
    collision_objects.append(PlatformSprite(0, SCREEN_HEIGHT - ground_h, 800, ground_h, GREEN, 
                                            tileset_path="extra/assets/tileset.png"))
    
    # Escadinha simples
    collision_objects.append(PlatformSprite(300, 250, 100, 15, YELLOW, 
                                            tileset_path="extra/assets/tileset.png"))
    collision_objects.append(PlatformSprite(500, 200, 100, 15, YELLOW, 
                                            tileset_path="extra/assets/tileset.png"))
    
    # Primeiro Inimigo (Tutorial de combate)
    enemies.append(EnemySprite(600, SCREEN_HEIGHT - ground_h - 35, 35, 500, 750, speed=2,
                               sprite_path="extra/assets/capivara-corrompida.png"))
    
    # ==========================================
    # SETOR 2: O LAGO DE ESPINHOS (1000px a 2000px)
    # ==========================================
    # Aqui não tem chão, só plataformas voadoras e espinhos embaixo
    # Espinho gigante no chão (se cair, morre)
    death_objects.append(SpikeSprite(800, SCREEN_HEIGHT - 10, 1200, 
                                      tileset_path="extra/assets/tileset.png"))  # Do pixel 800 ao 2000
    
    # Parkour
    coords_sector2 = [
        (900, 250, 80, 15),
        (1100, 220, 80, 15),
        (1250, 280, 80, 15),  # Pulo baixo
        (1400, 200, 100, 15),  # Plataforma pequena (difícil)
        (1600, 180, 50, 15),
        (1800, 250, 100, 15)  # Descanso
    ]
    for (x, y, w, h) in coords_sector2:
        collision_objects.append(PlatformSprite(x, y, w, h, YELLOW, 
                                                tileset_path="extra/assets/tileset.png"))
    
    # Inimigo voando/patrulhando em uma plataforma
    enemies.append(EnemySprite(1800, 250 - 25, 25, 1800, 1900, speed=1,
                               sprite_path="extra/assets/capivara-corrompida.png"))
    
    # ==========================================
    # SETOR 3: A TORRE (2000px a 3500px)
    # ==========================================
    # O chão volta, mas com inimigos rápidos
    collision_objects.append(PlatformSprite(2000, SCREEN_HEIGHT - ground_h, 1500, ground_h, GREEN, 
                                             tileset_path="extra/assets/tileset.png"))
    
    # Dois inimigos rápidos no chão
    enemies.append(EnemySprite(2200, SCREEN_HEIGHT - ground_h - 25, 25, 2100, 2500, speed=5,
                               sprite_path="extra/assets/capivara-corrompida.png"))
    enemies.append(EnemySprite(2800, SCREEN_HEIGHT - ground_h - 25, 25, 2600, 3000, speed=3,
                               sprite_path="extra/assets/capivara-corrompida.png"))
    
    # Obstáculos aéreos (precisa usar pulo duplo)
    collision_objects.append(PlatformSprite(2400, 200, 600, 15, YELLOW, 
                                            tileset_path="extra/assets/tileset.png"))
    death_objects.append(SpikeSprite(2400, 210, 600, 
                                     tileset_path="extra/assets/tileset.png"))  # Espinho EM CIMA da plataforma! Cuidado!
    
    # ==========================================
    # SETOR 4: RETA FINAL (3500px a 5000px)
    # ==========================================
    # Plataformas móveis simuladas (distantes) exigindo DASH
    collision_objects.append(PlatformSprite(3600, 250, 80, 15, YELLOW, 
                                             tileset_path="extra/assets/tileset.png"))
    collision_objects.append(PlatformSprite(3850, 250, 80, 15, YELLOW, 
                                             tileset_path="extra/assets/tileset.png"))  # Pulo longo (Dash necessário)
    collision_objects.append(PlatformSprite(4100, 250, 80, 15, YELLOW, 
                                             tileset_path="extra/assets/tileset.png"))
    
    # Chão final seguro
    collision_objects.append(PlatformSprite(4300, SCREEN_HEIGHT - ground_h, 700, ground_h, GREEN, 
                                             tileset_path="extra/assets/tileset.png"))
    
    # O Guardião Final (Inimigo muito rápido na porta)
    enemies.append(EnemySprite(4500, SCREEN_HEIGHT - ground_h - 50, 50, 4300, 4800, speed=9,
                               sprite_path="extra/assets/capivara-corrompida.png"))
    
    # A Porta
    final_door = Door(4900, SCREEN_HEIGHT - ground_h - 40, 40)
    
    # ==========================================
    # SETUP DO JOGADOR E CÂMERA
    # ==========================================
    player = PlayerSprite(50, SCREEN_HEIGHT - 100, 35, WORLD_WIDTH,
                          idle_sprite_path="extra/assets/player_idle.png",
                          run_sprite_path="extra/assets/player_run.png")
    camera = Camera(WORLD_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH)
    
    # --- Estados ---
    passed = False
    died = False
    
    def restart_game():
        """Reinicia o jogo"""
        nonlocal passed, died
        player.reset()
        # Reinicia todos os inimigos
        for enemy in enemies:
            enemy.reset()
        passed = False
        died = False
    
    # --- LOOP PRINCIPAL ---
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
                        # Próxima fase (última fase, então mostra tela de vitória final)
                        pygame.quit()
                        return "next"
    
        if not passed and not died:
            # --- ATUALIZAÇÕES ---
            player.update(collision_objects)
            
            for enemy in enemies:
                enemy.update()
                
            camera.update(player)
    
            # --- CHECAGEM DE MORTES ---
            # 1. Caiu no buraco (Y muito alto)
            if player.y > SCREEN_HEIGHT + 100:
                died = True
                
            # 2. Tocou em inimigo
            for enemy in enemies:
                if player.colliderect(enemy):
                    died = True
    
            # 3. Tocou em espinhos
            for spike in death_objects:
                if player.colliderect(spike):
                    died = True
    
            # --- VITÓRIA ---
            if player.colliderect(final_door):
                passed = True
    
            # --- DESENHO ---
            # Background com paralaxe simples (câmera movendo o fundo)
            screen.blit(bg_extended, (0, 0), (camera.x, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
            for obj in collision_objects:
                obj.draw(screen, camera)
                
            for spike in death_objects:
                spike.draw(screen, camera)
                
            for enemy in enemies:
                enemy.draw(screen, camera)
                
            final_door.draw(screen, camera)
            player.draw(screen, camera)
    
        elif died:
            font = pygame.font.SysFont('arial', 20, True, True)
            # Fundo vermelho translúcido
            screen.fill((100, 0, 0)) 
            text = font.render('YOU DIED! R to try again', True, WHITE)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT // 2))
    
        elif passed:
            font_large = pygame.font.SysFont('arial', 24, True, False)
            font_small = pygame.font.SysFont('arial', 18, False, False)
            
            title = font_large.render('FASE 6 COMPLETA!', True, (255, 255, 0))
            subtitle = font_large.render('JOGO FINALIZADO!', True, (255, 255, 0))
            restart_text = font_small.render('R - Reiniciar Fase', True, (200, 200, 200))
            next_text = font_small.render('N - Ver Tela Final', True, (200, 200, 200))
            esc_text = font_small.render('ESC - Sair', True, (150, 150, 150))
            
            screen.fill(BLACK)
            y_offset = SCREEN_HEIGHT // 2 - 80
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, y_offset))
            screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, y_offset + 35))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, y_offset + 75))
            screen.blit(next_text, (SCREEN_WIDTH//2 - next_text.get_width()//2, y_offset + 100))
            screen.blit(esc_text, (SCREEN_WIDTH//2 - esc_text.get_width()//2, y_offset + 125))
    
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    return "quit"