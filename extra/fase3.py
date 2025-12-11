import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fase 3')

AZUL = (0, 120, 255)
ROSA = (255, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

fonte = pygame.font.SysFont(None, 60)   # NOVO: fonte usada para mensagem de vitória

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

parede = pygame.Rect(350, 450, 100, 100)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and no_chao:
            if event.key == pygame.K_SPACE:
                vel_y = forca_pulo
                no_chao = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        novo_x = player_x - player_speed
        if not pygame.Rect(novo_x, player_y, 50, 50).colliderect(parede):
            player_x = novo_x

    if keys[pygame.K_RIGHT]:
        novo_x = player_x + player_speed
        if not pygame.Rect(novo_x, player_y, 50, 50).colliderect(parede):
            player_x = novo_x

    vel_y += gravidade
    player_y += vel_y

    player_rect = pygame.Rect(player_x, int(player_y), 50, 50)   # NOVO: retângulo do player
    portal_rect = pygame.Rect(portal_x, portal_y, portal_w, portal_h)  # NOVO: retângulo do portal

    # NOVO: colisão vertical com a parede
    if player_rect.colliderect(parede):
        # bateu por cima da parede (caindo)
        if vel_y > 0 and player_y + 50 <= parede.top + vel_y:
            player_y = parede.top - 50
            vel_y = 0
            no_chao = True

        # bateu por baixo da parede (subindo)
        elif vel_y < 0 and player_y >= parede.bottom - vel_y:
            player_y = parede.bottom
            vel_y = 0

    # colisão com o chão
    if player_y + 50 >= 550:
        player_y = 550 - 50
        vel_y = 0
        no_chao = True

    screen.fill(AZUL)

    pygame.draw.rect(screen, VERDE, (0, 550, 800, 50))
    pygame.draw.rect(screen, VERMELHO, (player_x, int(player_y), 50, 50))
    pygame.draw.rect(screen, PRETO, (portal_x, portal_y, portal_w, portal_h))
    pygame.draw.rect(screen, ROSA, parede)

    # NOVO: detectar vitória ao encostar no portal
    if player_rect.colliderect(portal_rect):
        texto = fonte.render("VOCÊ GANHOU!", True, (255,255,255))
        screen.blit(texto, (250,250))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
