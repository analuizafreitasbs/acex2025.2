import pygame
from pygame.locals import *
import sys
import os

# Adiciona o diretório pai ao path para importar game_classes
# sys.path.insert() adiciona um caminho ao Python path, permitindo importar módulos de outros diretórios
# os.path.dirname() pega o diretório de um arquivo
# os.path.abspath(__file__) pega o caminho absoluto do arquivo atual
# Fazemos isso duas vezes (dirname duas vezes) para subir dois níveis: phases -> extra -> raiz
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa classes do jogo (versões sem sprite)
from game_classes.player import PlayerNoSprite
from game_classes.enemy_no_sprite import EnemyNoSprite
from game_classes.platform_no_sprite import PlatformNoSprite
from game_classes.door import Door

def run_phase4():
    """
    Executa a fase 4 e retorna o resultado
    
    Returns:
        "next": Se o jogador completou e quer ir para próxima fase
        "restart": Se o jogador quer reiniciar (já tratado internamente)
        "quit": Se o jogador quer sair do jogo
    """
    # pygame.init() - Inicializa todos os módulos do pygame
    # Deve ser chamado antes de usar qualquer funcionalidade do pygame
    # Inicializa: display, font, mixer (som), etc.
    pygame.init()
    
    # --- Configuração da Fase 4 ---
    # Tela grande fixa
    SCREEN_WIDTH = 1000  # Largura da janela em pixels
    SCREEN_HEIGHT = 600  # Altura da janela em pixels
    
    # pygame.display.set_mode() - Cria a janela do jogo
    # Retorna uma Surface (superfície) que representa a tela
    # (largura, altura) define o tamanho da janela
    # Esta Surface é onde desenhamos tudo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # pygame.display.set_caption() - Define o título da janela
    # Aparece na barra de título da janela
    pygame.display.set_caption('Phase 4')
    
    # pygame.time.Clock() - Cria um objeto Clock para controlar a taxa de frames
    # Usado com clock.tick() para limitar o FPS (frames por segundo)
    # Importante para manter o jogo rodando na mesma velocidade em diferentes computadores
    clock = pygame.time.Clock()
    
    # Cores em formato RGB (Red, Green, Blue)
    # Cada valor vai de 0 a 255
    # (255, 255, 255) = Branco, (0, 0, 0) = Preto, etc.
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 100, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    
    # --- Criando o Mundo ---
    
    # 1. Chão e Plataformas
    ground_height = 50  # Altura do chão em pixels
    # Lista para passar ao jogador para checagem de colisão
    # O jogador precisa saber quais objetos ele pode colidir
    collision_objects = []
    
    # Chão
    # PlatformNoSprite(x, y, largura, altura, cor)
    # x, y: posição no canto superior esquerdo
    # SCREEN_HEIGHT - ground_height: posiciona o chão na parte inferior da tela
    ground = PlatformNoSprite(0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height, GREEN)
    collision_objects.append(ground)
    
    # Plataformas (Posições originais da Fase 4)
    # Lista de tuplas: (x, y, largura, altura)
    # y é calculado de baixo para cima: SCREEN_HEIGHT - ground_height - altura_desejada
    plat_coords = [
        (150, SCREEN_HEIGHT - ground_height - 100, 200, 20),
        (400, SCREEN_HEIGHT - ground_height - 200, 150, 20),
        (650, SCREEN_HEIGHT - ground_height - 300, 200, 20)
    ]
    # Loop cria uma plataforma para cada coordenada
    for (x, y, w, h) in plat_coords:
        p = PlatformNoSprite(x, y, w, h, YELLOW)
        collision_objects.append(p)
    
    # 2. Saída
    final_size = 100  # Tamanho da porta (quadrado)
    # Porta posicionada no canto superior direito, acima do chão
    final_door = Door(SCREEN_WIDTH - final_size, SCREEN_HEIGHT - ground_height - final_size, final_size)
    
    # 3. Inimigo
    enemy_size = 40
    # Limites da patrulha (Começo da tela até antes da porta)
    right_border = 600
    door_limit = SCREEN_WIDTH - final_size
    # EnemyNoSprite(x, y, tamanho, limite_esquerdo, limite_direito, velocidade)
    # speed=0 significa que o inimigo não se move (estático)
    enemy = EnemyNoSprite(right_border, 
                          SCREEN_HEIGHT - ground_height - enemy_size, 
                          enemy_size, 
                          0,
                          door_limit, 
                          speed=0)
    
    # 4. Jogador
    player_size = 50
    # PlayerNoSprite(x, y, tamanho, largura_tela)
    # Inicialmente criado em (0, 0), será reposicionado
    player = PlayerNoSprite(0, 0, player_size, SCREEN_WIDTH)
    # bottomleft = (x, y) - Define a posição usando o canto inferior esquerdo
    # ground.topleft = (x, y) - Pega o canto superior esquerdo do chão
    # Isso posiciona o jogador em cima do chão
    player.bottomleft = ground.topleft  # Posiciona no chão
    
    # --- Variáveis de Controle ---
    passed = False  # True quando o jogador completou a fase
    died = False    # True quando o jogador morreu
    
    def restart_game():
        """
        Reinicia o jogo
        Reseta todas as entidades para suas posições iniciais
        """
        nonlocal passed, died  # Permite modificar variáveis do escopo externo
        # Reset do jogador - volta para posição inicial e reseta estados
        player.reset()
        # Reset do inimigo - volta para posição inicial
        enemy.reset()
        
        passed = False
        died = False
    
    # --- Loop Principal ---
    # O loop principal do jogo roda continuamente até o jogador sair
    # Cada iteração do loop é um "frame" do jogo
    running = True
    while running:
        # 1. Eventos
        # pygame.event.get() - Pega todos os eventos que aconteceram desde a última chamada
        # Eventos são: teclas pressionadas, mouse clicado, janela fechada, etc.
        # Retorna uma lista de objetos Event
        for event in pygame.event.get():
            # pygame.QUIT - Evento disparado quando o usuário fecha a janela (X)
            if event.type == pygame.QUIT:
                pygame.quit()  # Finaliza o pygame
                return "quit"  # Retorna status de saída
            
            # pygame.KEYDOWN - Evento disparado quando uma tecla é pressionada
            # event.key contém qual tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                # K_ESCAPE - Tecla ESC
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return "quit"
            
            # Só processa controles do jogo se o jogador não morreu nem passou
            if not passed and not died:
                if event.type == pygame.KEYDOWN:
                    # K_SPACE ou K_w - Teclas de pulo
                    if (event.key == K_SPACE or event.key == K_w):
                        player.jump()
                    # K_e - Tecla de avanço (dash)
                    if event.key == K_e:
                        player.start_dash()
            else:
                # Menu de game over/vitória
                if event.type == pygame.KEYDOWN:
                    # K_r - Reiniciar
                    if event.key == K_r:
                        restart_game()
                    # K_n - Próxima fase (só funciona se passou)
                    elif event.key == K_n and passed:
                        # Próxima fase
                        pygame.quit()
                        return "next"
        
        # 2. Lógica de Jogo
        # Atualiza o estado do jogo apenas se o jogador está jogando
        if not passed and not died:
            # player.update() - Atualiza posição, física e colisões do jogador
            # Recebe a lista de objetos com os quais pode colidir
            player.update(collision_objects)
            # enemy.update() - Atualiza posição do inimigo (patrulha)
            enemy.update()
    
            # colliderect() - Método do pygame.Rect que verifica se dois retângulos se sobrepõem
            # Retorna True se há colisão, False caso contrário
            # player e enemy são ambos pygame.Rect (herdam de Rect)
            if player.colliderect(enemy):
                died = True
            
            # Verifica se o jogador chegou na porta (objetivo)
            if player.colliderect(final_door):
                passed = True
    
            # 3. Desenho (Render)
            # screen.fill() - Preenche toda a tela com uma cor
            # Limpa o frame anterior, preparando para desenhar o novo frame
            screen.fill(BLUE)  # Fundo azul simples
            
            # Desenha tudo diretamente (sem câmera)
            # Cada objeto tem um método draw() que desenha ele mesmo na tela
            for obj in collision_objects:
                obj.draw(screen)  # Desenha sem câmera (posição direta)
                
            final_door.draw(screen)  # Desenha a porta
            enemy.draw(screen)       # Desenha o inimigo
            player.draw(screen)      # Desenha o jogador
    
        # 4. Telas de Game Over / Vitória
        elif died:
            # pygame.font.SysFont() - Cria uma fonte usando uma fonte do sistema
            # Parâmetros: (nome_da_fonte, tamanho, negrito, itálico)
            # Retorna um objeto Font
            font = pygame.font.SysFont('arial', 20, True, True)
            # font.render() - Cria uma imagem (Surface) com o texto renderizado
            # Parâmetros: (texto, antialiasing, cor_do_texto, cor_de_fundo_opcional)
            # Retorna uma Surface que pode ser desenhada com blit()
            text = font.render('You died!! Press R to retry', True, WHITE)
            screen.fill(RED)
            # screen.blit() - Desenha uma Surface (imagem/texto) na tela
            # Parâmetros: (surface, posição)
            # Centraliza o texto: SCREEN_WIDTH//2 - text.get_width()//2
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT // 2))
    
        elif passed:
            # Cria duas fontes: uma grande para título, uma pequena para opções
            font_large = pygame.font.SysFont('arial', 24, True, False)
            font_small = pygame.font.SysFont('arial', 18, False, False)
            
            # Renderiza todos os textos do menu de vitória
            title = font_large.render('FASE 4 COMPLETA!', True, (255, 255, 0))
            restart_text = font_small.render('R - Reiniciar Fase', True, (200, 200, 200))
            next_text = font_small.render('N - Proxima Fase', True, (200, 200, 200))
            esc_text = font_small.render('ESC - Sair', True, (150, 150, 150))
            
            screen.fill(BLACK)
            # Calcula posição Y centralizada com espaçamento
            y_offset = SCREEN_HEIGHT // 2 - 60
            # Desenha cada texto centralizado horizontalmente
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, y_offset))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, y_offset + 40))
            screen.blit(next_text, (SCREEN_WIDTH//2 - next_text.get_width()//2, y_offset + 65))
            screen.blit(esc_text, (SCREEN_WIDTH//2 - esc_text.get_width()//2, y_offset + 90))
    
        # pygame.display.flip() - Atualiza a tela, mostrando tudo que foi desenhado
        # Deve ser chamado uma vez por frame, após desenhar tudo
        # Alternativa: pygame.display.update() (mais lento, atualiza áreas específicas)
        pygame.display.flip()
        
        # clock.tick(FPS) - Limita a taxa de frames
        # FPS = Frames Per Second (quadros por segundo)
        # 65 FPS significa que o loop roda 65 vezes por segundo
        # Se o computador for muito rápido, espera para não rodar mais rápido que isso
        # Se for muito lento, roda o mais rápido possível
        clock.tick(65)
    
    # pygame.quit() - Finaliza o pygame, libera recursos
    # Deve ser chamado antes de sair do programa
    pygame.quit()
    return "quit"