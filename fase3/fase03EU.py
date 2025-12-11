import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fase 3 - Colisão Simples')

AZUL = (0, 120, 255)
ROSA = (255, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

player_x = 50
player_y = 500
player_speed = 5

vel_y = 0
gravidade = 0.5
forca_pulo = -12
no_chao = True

portal_x = 650
portal_y = 430
portal_w = 120
portal_h = 120

# --- NOVO: parede para colisão ---
parede = pygame.Rect(350, 450, 100, 100)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and no_chao:
                vel_y = forca_pulo
                no_chao = False

    keys = pygame.key.get_pressed()

# MOVIMENTO ESQUERMA + COLISÃO SIMPLES
    if keys[pygame.K_LEFT]:
        novo_x = player_x - player_speed
        player_teste = pygame.Rect(novo_x, player_y, 50, 50)
        if not player_teste.colliderect(parede):
            player_x = novo_x

# MOVIMENTO DIREITA + COLISÃO SIMPLES
    if keys[pygame.K_RIGHT]:
        novo_x = player_x + player_speed
        player_teste = pygame.Rect(novo_x, player_y, 50, 50)
        if not player_teste.colliderect(parede):
            player_x = novo_x

    vel_y += gravidade
    player_y += vel_y

    if player_y + 50 >= 550:
        player_y = 550 - 50
        vel_y = 0
        no_chao = True

    screen.fill(AZUL)

    pygame.draw.rect(screen, VERDE, (0, 550, 800, 50))
    pygame.draw.rect(screen, VERMELHO, (player_x, int(player_y), 50, 50))
    pygame.draw.rect(screen, PRETO, (portal_x, portal_y, portal_w, portal_h))
    pygame.draw.rect(screen, ROSA, parede)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
