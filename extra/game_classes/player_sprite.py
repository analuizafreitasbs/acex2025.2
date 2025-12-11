import pygame
from pygame.locals import *

class PlayerSprite(pygame.Rect):
    """
    Classe do jogador com suporte a sprite e animações
    """
    def __init__(self, x, y, size, world_width, idle_sprite_path=None, run_sprite_path=None):
        super().__init__(x, y, size, size)
        
        self.world_width = world_width  # Largura do mundo
        
        # ===== SPRITES =====
        # Sprite parado
        self.sprite_idle = None
        if idle_sprite_path:
            try:
                self.sprite_idle = pygame.image.load(idle_sprite_path).convert_alpha()
                self.sprite_idle = pygame.transform.scale(self.sprite_idle, (size, size))
            except:
                # Fallback para retângulo colorido
                self.sprite_idle = pygame.Surface((size, size))
                self.sprite_idle.fill((255, 0, 0))
        else:
            self.sprite_idle = pygame.Surface((size, size))
            self.sprite_idle.fill((255, 0, 0))
        
        # Sprites de corrida (frames de animação)
        self.run_frames = []
        if run_sprite_path:
            try:
                run_sheet = pygame.image.load(run_sprite_path).convert_alpha()
                frame_width = run_sheet.get_width() // 7  # Assumindo 7 frames
                frame_height = run_sheet.get_height()
                
                for i in range(7):
                    frame = run_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
                    frame = pygame.transform.scale(frame, (size, size))
                    self.run_frames.append(frame)
            except:
                # Fallback
                for i in range(7):
                    frame = pygame.Surface((size, size))
                    frame.fill((255, 0, 0))
                    self.run_frames.append(frame)
        
        # Controle de animação
        self.anim_index = 0
        self.anim_speed = 0.18
        self.current_sprite = self.sprite_idle
        
        # Cor de debug
        self.color = (255, 0, 0)
        
        # Posição inicial
        self.start_pos = (x, y)
        
        # Física
        self.vel_y = 0
        self.gravity = 0.5
        self.jump_force = -8
        self.speed_x = 4
        
        # Estados
        self.is_on_ground = False
        self.is_dashing = False
        self.can_dash = True
        self.direction = 1  # 1 direita, -1 esquerda
        
        # Pulo duplo
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        
        # Avanço
        self.dash_speed = 40
        
        # Escalada
        self.climb_speed = 4
        self.side_touch_buffer = 5
    
    # ========================
    #      ANIMAÇÃO
    # ========================
    def animate(self, dx):
        """Atualiza animação baseado no movimento"""
        # Escolhe sprite idle ou run
        if dx != 0:
            self.anim_index += self.anim_speed
            if self.anim_index >= len(self.run_frames):
                self.anim_index = 0
            if self.run_frames:
                self.current_sprite = self.run_frames[int(self.anim_index)]
        else:
            self.current_sprite = self.sprite_idle
            self.anim_index = 0
        
        # Flip automático ao andar para esquerda
        if self.direction == -1:
            self.current_sprite = pygame.transform.flip(self.current_sprite, True, False)
    
    # ========================
    #     CONTROLES
    # ========================
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
    
    # ========================
    #    COLISÃO HORIZONTAL
    # ========================
    def check_horizontal_collision(self, dx, platforms):
        """Verifica e resolve colisões horizontais"""
        self.x += dx
        
        # Limitar ao mundo
        self.left = max(0, self.left)
        self.right = min(self.world_width, self.right)
        
        for plat in platforms:
            if self.colliderect(plat):
                if self.bottom > plat.top + 5 and self.top < plat.bottom - 5:
                    if dx > 0:
                        self.right = plat.left
                    elif dx < 0:
                        self.left = plat.right
    
    # ========================
    #    COLISÃO VERTICAL
    # ========================
    def check_vertical_collision(self, platforms):
        """Verifica e resolve colisões verticais"""
        on_platform = False
        # Salva posição antes do movimento (já foi aplicado no update)
        prev_top = self.top - self.vel_y
        prev_bottom = self.bottom - self.vel_y
        
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
    
    # ========================
    #        ESCALADA
    # ========================
    def check_climb(self, platforms, keys):
        """Verifica e trata escalada de parede"""
        touching_side = False
        for plat in platforms:
            if self.colliderect(plat):
                vertical_overlap = (self.bottom > plat.top + self.side_touch_buffer) and \
                                   (self.top < plat.bottom - self.side_touch_buffer)
                if vertical_overlap:
                    touching_side = True
                    break
        
        if touching_side and keys[K_w]:
            self.y -= self.climb_speed
            self.vel_y = 0
    
    # ========================
    #        UPDATE
    # ========================
    def update(self, platforms):
        """Atualiza posição e física do jogador"""
        dx, keys = self.handle_input()
        
        # Avanço
        if self.is_dashing:
            dx = self.dash_speed * self.direction
            self.is_dashing = False
        
        # Movimento horizontal
        self.check_horizontal_collision(dx, platforms)
        
        # Gravidade
        self.vel_y += self.gravity
        self.y += self.vel_y
        
        # Colisões verticais
        self.check_vertical_collision(platforms)
        
        # Escalada
        self.check_climb(platforms, keys)
        
        # Animação
        self.animate(dx)
    
    # ========================
    #        DRAW
    # ========================
    def draw(self, screen, camera):
        """Desenha o jogador na tela"""
        rect_visible = camera.apply(self)
        screen.blit(self.current_sprite, rect_visible)
        # pygame.draw.rect(screen, (255, 0, 0), rect_visible, 1)  # Debug hitbox
