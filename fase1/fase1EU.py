import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fase 1 - Simples')

AZUL = (0, 120, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fundo
    screen.fill(AZUL)

    # Chão verde (800 largura x 50 altura)
    pygame.draw.rect(screen, VERDE, (0, 550, 800, 50))

    # Player vermelho (quadrado 50x50)
    pygame.draw.rect(screen, VERMELHO, (50, 500, 50, 50))

    # Portal preto (quadrado 120x120)
    pygame.draw.rect(screen, PRETO, (650, 430, 120, 120))

    pygame.display.flip()

pygame.quit()
