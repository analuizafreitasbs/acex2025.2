import pygame
from pygame.locals import *
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa as funções de cada fase
# Cada fase tem uma função run_phaseX() que executa a fase e retorna um resultado
from phases.phase4 import run_phase4
from phases.phase5 import run_phase5
from phases.phase6 import run_phase6

class GameManager:
    """
    Gerenciador de fases do jogo
    
    Esta classe controla o fluxo do jogo, gerenciando qual fase está ativa
    e transicionando entre elas quando o jogador completa uma fase.
    """
    def __init__(self):
        """
        Construtor da classe - inicializa o gerenciador
        
        __init__ é um método especial do Python chamado automaticamente quando
        criamos um objeto: manager = GameManager()
        
        Não há super() aqui porque GameManager não herda de nenhuma classe.
        Se herdasse, usaríamos super().__init__() para chamar o construtor da classe pai.
        """
        # self.current_phase - Armazena qual fase está atualmente ativa
        # Começa na fase 4 (primeira fase do jogo)
        self.current_phase = 4  # Fase inicial
        
        # self.phases - Dicionário que mapeia número da fase para sua função
        # Chave: número da fase (4, 5, 6)
        # Valor: função que executa aquela fase (run_phase4, run_phase5, run_phase6)
        # Isso permite chamar a fase correta dinamicamente: self.phases[4]()
        self.phases = {
            4: run_phase4,  # Função que executa a fase 4
            5: run_phase5,  # Função que executa a fase 5
            6: run_phase6   # Função que executa a fase 6
        }
    
    def run(self):
        """
        Executa o loop principal do gerenciador
        
        Este método fica em loop, executando fases sequencialmente.
        Quando uma fase termina, decide se avança para próxima, reinicia ou sai.
        """
        # Loop infinito que continua até o jogador sair ou completar todas as fases
        while True:
            # Verifica se a fase atual existe no dicionário de fases
            if self.current_phase in self.phases:
                # Chama a função da fase atual
                # self.phases[self.current_phase] pega a função (ex: run_phase4)
                # () executa a função
                # A função retorna uma string: "next", "restart" ou "quit"
                result = self.phases[self.current_phase]()
                
                # Analisa o resultado retornado pela fase
                if result == "next":
                    # "next" significa que o jogador completou a fase e quer avançar
                    # Avança para próxima fase
                    if self.current_phase < 6:
                        # Se não é a última fase, incrementa o número da fase
                        self.current_phase += 1
                        # O loop continua e executa a próxima fase
                    else:
                        # Se é a fase 6 (última), mostra tela de jogo completo
                        self.show_game_complete()
                        # break sai do loop while, terminando o jogo
                        break
                elif result == "restart":
                    # "restart" significa que o jogador quer reiniciar a fase atual
                    # O restart já foi feito dentro da fase (ela reseta tudo)
                    # continue volta ao início do loop, executando a mesma fase novamente
                    continue
                elif result == "quit":
                    # "quit" significa que o jogador quer sair do jogo
                    # break sai do loop while, terminando o programa
                    break
            else:
                # Se a fase atual não existe no dicionário, sai do loop
                # Isso não deveria acontecer, mas é uma proteção
                break
    
    def show_game_complete(self):
        """
        Mostra tela de jogo completo
        
        Esta função cria uma janela simples mostrando que o jogador completou
        todas as fases. É chamada quando o jogador completa a fase 6.
        """
        # pygame.init() - Inicializa todos os módulos do pygame
        # Necessário antes de usar qualquer funcionalidade do pygame
        # Se já foi inicializado antes, não faz nada (seguro chamar múltiplas vezes)
        pygame.init()
        
        # pygame.display.set_mode() - Cria a janela do jogo
        # Retorna uma Surface que representa a tela
        # (640, 360) define o tamanho da janela
        screen = pygame.display.set_mode((640, 360))
        
        # pygame.display.set_caption() - Define o título da janela
        # Aparece na barra de título
        pygame.display.set_caption('Game Complete!')
        
        # pygame.time.Clock() - Cria um objeto Clock para controlar FPS
        # Usado com clock.tick() para limitar frames por segundo
        clock = pygame.time.Clock()
        
        # pygame.font.SysFont() - Cria uma fonte usando fonte do sistema
        # Parâmetros: (nome_da_fonte, tamanho, negrito, itálico)
        # Retorna um objeto Font que pode renderizar texto
        font_large = pygame.font.SysFont('arial', 30, True, False)   # Grande, negrito
        font_small = pygame.font.SysFont('arial', 18, False, False) # Pequena, normal
        
        # Variável de controle do loop
        running = True
        
        # Loop da tela de vitória
        while running:
            # pygame.event.get() - Pega todos os eventos desde a última chamada
            # Retorna uma lista de objetos Event
            for event in pygame.event.get():
                # pygame.QUIT - Evento disparado quando o usuário fecha a janela (X)
                if event.type == pygame.QUIT:
                    running = False  # Sai do loop
                
                # pygame.KEYDOWN - Evento disparado quando uma tecla é pressionada
                if event.type == pygame.KEYDOWN:
                    # event.key contém qual tecla foi pressionada
                    # K_ESCAPE = tecla ESC, K_RETURN = tecla ENTER
                    if event.key == K_ESCAPE or event.key == K_RETURN:
                        running = False  # Sai do loop
            
            # screen.fill() - Preenche toda a tela com uma cor
            # (0, 0, 0) = preto em RGB
            # Limpa o frame anterior
            screen.fill((0, 0, 0))
            
            # font.render() - Cria uma imagem (Surface) com o texto renderizado
            # Parâmetros: (texto, antialiasing, cor_do_texto, cor_de_fundo_opcional)
            # antialiasing = True deixa o texto mais suave (menos pixelado)
            # Retorna uma Surface que pode ser desenhada com blit()
            title = font_large.render('PARABENS!', True, (255, 255, 0))  # Amarelo
            subtitle = font_large.render('VOCE ZEROU TODAS AS FASES!', True, (255, 255, 0))
            press_text = font_small.render('Pressione ESC ou ENTER para sair', True, (200, 200, 200))  # Cinza
            
            # screen.blit() - Desenha uma Surface (imagem/texto) na tela
            # Parâmetros: (surface_origem, posição_destino)
            # Centraliza horizontalmente: 640//2 - text.get_width()//2
            # 640//2 = centro da tela, text.get_width()//2 = metade da largura do texto
            # Subtraindo, posiciona o texto centralizado
            screen.blit(title, (640//2 - title.get_width()//2, 360 // 2 - 40))
            screen.blit(subtitle, (640//2 - subtitle.get_width()//2, 360 // 2))
            screen.blit(press_text, (640//2 - press_text.get_width()//2, 360 // 2 + 50))
            
            # pygame.display.flip() - Atualiza a tela, mostrando tudo que foi desenhado
            # Deve ser chamado uma vez por frame, após desenhar tudo
            # Alternativa: pygame.display.update() (mais lento, atualiza áreas específicas)
            pygame.display.flip()
            
            # clock.tick(FPS) - Limita a taxa de frames
            # FPS = Frames Per Second (quadros por segundo)
            # 60 FPS significa que o loop roda 60 vezes por segundo
            # Se o computador for muito rápido, espera para não rodar mais rápido
            # Se for muito lento, roda o mais rápido possível
            clock.tick(60)
        
        # pygame.quit() - Finaliza o pygame, libera recursos
        # Deve ser chamado antes de sair do programa
        # Libera memória, fecha dispositivos de áudio, etc.
        pygame.quit()

# __name__ == "__main__" - Verifica se o arquivo está sendo executado diretamente
# Se executarmos: python game_manager.py
# __name__ será "__main__" e o código abaixo roda
# Se importarmos: from phases import game_manager
# __name__ será "phases.game_manager" e o código abaixo NÃO roda
# Isso permite usar o arquivo como módulo ou como script principal
if __name__ == "__main__":
    # Cria uma instância do GameManager
    # Isso chama automaticamente __init__()
    manager = GameManager()
    
    # Chama o método run() que inicia o loop principal do jogo
    manager.run()