import pygame
from pygame.locals import *

class PlayerNoSprite(pygame.Rect):
    """
    Classe do jogador sem sprite - usa retângulo colorido simples
    
    Herda de pygame.Rect, que é uma classe do pygame que representa um retângulo.
    Isso nos dá automaticamente: x, y, width, height, left, right, top, bottom, center, etc.
    E métodos como: colliderect() para verificar colisões.
    """
    def __init__(self, x, y, size, screen_width):
        """
        Construtor da classe - inicializa o objeto quando ele é criado
        
        Args:
            x: Posição X inicial
            y: Posição Y inicial  
            size: Tamanho do jogador (largura e altura, pois é quadrado)
            screen_width: Largura da tela (para limitar movimento)
        
        __init__ é um método especial do Python chamado automaticamente quando
        criamos um objeto: player = PlayerNoSprite(0, 0, 50, 1000)
        """
        # super() - Chama o método da classe pai (pygame.Rect)
        # super().__init__() chama o construtor de pygame.Rect
        # pygame.Rect(x, y, width, height) cria um retângulo
        # Isso inicializa todas as propriedades do Rect (x, y, width, height, etc.)
        # Sem isso, não teríamos acesso a métodos como colliderect(), left, right, etc
        super().__init__(x, y, size, size)
        self.color = (255, 0, 0)  # Vermelho
        
        self.start_pos = (x, y)  # Posição inicial
        self.screen_width = screen_width  # Largura da tela
        
        # Física
        self.vel_y = 0  # Velocidade vertical
        self.gravity = 0.5  # Força da gravidade
        self.jump_force = -10  # Força do pulo
        self.speed_x = 5  # Velocidade horizontal
        self.dash_speed = 100  # Velocidade do avanço
        
        # Estados
        self.is_on_ground = False  # Está no chão
        self.is_dashing = False  # Está avançando
        self.can_dash = True  # Pode avançar
        self.direction = 1  # Direção: 1 direita, -1 esquerda
        
        # Pulo duplo
        self.max_jumps = 2  # Máximo de pulos
        self.jumps_left = self.max_jumps  # Pulos restantes
        
        # Escalada
        self.climb_speed = 4  # Velocidade de escalada
        self.side_touch_buffer = 5  # Buffer de toque lateral
    
    def reset(self):
        """Reseta o jogador para posição inicial"""
        self.bottomleft = self.start_pos
        self.vel_y = 0
        self.is_on_ground = False
        self.jumps_left = self.max_jumps
        self.can_dash = True
        self.is_dashing = False
        self.direction = 1
    
    def handle_input(self):
        """Processa entrada do teclado"""
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[K_a]:
            dx = -self.speed_x
            self.direction = -1
        if keys[K_d]:
            dx = self.speed_x
            self.direction = 1
        return dx, keys
    
    def jump(self):
        """Faz o jogador pular"""
        if self.jumps_left > 0:
            self.vel_y = self.jump_force
            self.jumps_left -= 1
            self.is_on_ground = False
    
    def start_dash(self):
        """Inicia movimento de avanço"""
        if self.can_dash and not self.is_dashing:
            self.is_dashing = True
            self.can_dash = False
    
    def update(self, platforms):
        """Atualiza posição e física do jogador"""
        dx, keys = self.handle_input()
        
        # Lógica do avanço
        if self.is_dashing:
            dx = self.dash_speed * self.direction
            self.is_dashing = False
        
        # Movimento horizontal
        self.x += dx
        # Manter na tela
        self.left = max(0, self.left)
        self.right = min(self.screen_width, self.right)
        
        # Colisão horizontal
        for plat in platforms:
            if self.colliderect(plat):
                if self.bottom > plat.top + 5 and self.top < plat.bottom - 5:
                    if dx > 0:
                        self.right = plat.left
                    elif dx < 0:
                        self.left = plat.right
        
        # Movimento vertical
        self.vel_y += self.gravity
        
        # Lógica de escalada
        touching_side = False
        for plat in platforms:
            if self.colliderect(plat):
                # Verifica sobreposição vertical
                if (self.bottom > plat.top + self.side_touch_buffer) and \
                   (self.top < plat.bottom - self.side_touch_buffer):
                    touching_side = True
                    break
        
        if touching_side and keys[K_w]:
            self.y -= self.climb_speed
            self.vel_y = 0
        else:
            # Salva posição anterior antes de mover
            prev_top = self.top
            prev_bottom = self.bottom
            
            # Aplica movimento vertical
            self.y += self.vel_y
            
            # Colisão vertical - verifica após movimento
            on_platform = False
            
            for plat in platforms:
                if self.colliderect(plat):
                    # Calcula sobreposição para determinar direção da colisão
                    overlap_top = max(0, min(self.bottom, plat.bottom) - max(self.top, plat.top))
                    overlap_left = max(0, min(self.right, plat.right) - max(self.left, plat.left))
                    
                    # Se há sobreposição significativa
                    if overlap_top > 0 and overlap_left > 0:
                        # Verifica se estava acima da plataforma antes do movimento
                        was_above = prev_bottom <= plat.top
                        # Verifica se estava abaixo da plataforma antes do movimento
                        was_below = prev_top >= plat.bottom
                        
                        # Pouso: estava acima e agora está colidindo, caindo
                        if was_above and self.vel_y >= 0 and not was_below:
                            self.bottom = plat.top
                            self.vel_y = 0
                            self.is_on_ground = True
                            on_platform = True
                            self.jumps_left = self.max_jumps
                            self.can_dash = True
                            break  # Resolve apenas uma colisão por frame
                        
                        # Batendo no teto: estava abaixo e agora está colidindo, subindo
                        elif was_below and self.vel_y < 0 and not was_above:
                            self.top = plat.bottom
                            self.vel_y = 0
                            break  # Resolve apenas uma colisão por frame
                        
                        # Fallback: se não conseguiu determinar direção, usa posição relativa
                        # Apenas se ainda não resolveu a colisão
                        elif not on_platform:
                            # Se o centro Y do player está acima do centro da plataforma
                            # assume que está em cima
                            if self.centery < plat.centery:
                                self.bottom = plat.top
                                self.vel_y = 0
                                self.is_on_ground = True
                                on_platform = True
                                self.jumps_left = self.max_jumps
                                self.can_dash = True
                                break
            
            if not on_platform:
                self.is_on_ground = False
    
    def draw(self, screen, camera=None):
        """Desenha o jogador na tela"""
        if camera:
            rect_visible = camera.apply(self)
            pygame.draw.rect(screen, self.color, rect_visible)
        else:
            pygame.draw.rect(screen, self.color, self)

