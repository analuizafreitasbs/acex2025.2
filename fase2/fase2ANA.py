import pygame
pygame.init()

# AQUI É IGUAL À FASE 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fase 2 - Interativa com Pulo')

AZUL = (0, 120, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# AQUI COMEÇA A MUDAR DA FASE 1 PARA A FASE 2
player_x = 50
player_y = 500
player_speed = 5

portal_x = 650
portal_y = 430
portal_w = 120
portal_h = 120

# Adicionamos: gravidade, pulo e controle vertical.
vel_y = 0                # Velocidade vertical do personagem
gravidade = 0.5          # Puxa o player para baixo
forca_pulo = -12         # Impulso do pulo (valor negativo sobe)
no_chao = True           # Garante que só pula se estiver no chão

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Evento de pulo 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and no_chao:
                vel_y = forca_pulo      # sobe
                no_chao = False         # não pode pular de novo até tocar o chão

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # GRAVIDADE — TOTALMENTE NOVO NESSA FASE
    vel_y += gravidade
    player_y += vel_y

    # Verifica se tocou o chão
    if player_y + 50 >= 550:               
        player_y = 550 - 50               # volta para cima do chão
        vel_y = 0                         # zera queda
        no_chao = True                    # pode pular de novo

    # Fase 2 mantém o mesmo cenário da Fase 1.
    screen.fill(AZUL)

    # Chão
    pygame.draw.rect(screen, VERDE, (0, 550, 800, 50))

    # Player
    pygame.draw.rect(screen, VERMELHO, (player_x, int(player_y), 50, 50))

    # Portal
    pygame.draw.rect(screen, PRETO, (portal_x, portal_y, portal_w, portal_h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
