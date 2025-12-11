import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fase 2')

AZUL = (0, 120, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

fonte = pygame.font.SysFont(None, 60)   # NOVO

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

running = True
clock = pygame.time.Clock()

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
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

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

    player_rect = pygame.Rect(player_x, int(player_y), 50, 50)     # NOVO
    portal_rect = pygame.Rect(portal_x, portal_y, portal_w, portal_h)  # NOVO

    if player_rect.colliderect(portal_rect):                       # NOVO
        texto = fonte.render("VOCÊ GANHOU!", True, (255,255,255))
        screen.blit(texto, (250,250))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
