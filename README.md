# Guardiões da Mata - Projeto ACEX1

## 📋 Sobre o Projeto

**Guardiões da Mata** é um jogo de plataforma 2D desenvolvido em Python utilizando a biblioteca Pygame, criado como projeto prático para a disciplina **ACEX1 (Atividades Curriculares de Extensão 1)** do curso de **Sistemas de Informações do IFBA**.

O jogo apresenta o **Curupira**, figura lendária do folclore brasileiro conhecida como protetor das florestas, em uma aventura que combina mecânicas clássicas de jogos de plataforma com uma narrativa que valoriza a cultura brasileira e a conscientização ambiental.

## 🎯 Objetivos e Justificativa

### Objetivos

- **Servir como projeto prático** para o ensino de desenvolvimento de jogos, abordando conceitos de programação, design de jogos, pixel art e game design
- **Valorizar e divulgar o folclore brasileiro**, especialmente a figura do Curupira e a importância da preservação ambiental
- **Criar uma experiência de plataforma 2D** desafiadora, divertida e acessível para diferentes públicos

### Justificativa

O projeto surge da necessidade de criar material didático prático e culturalmente relevante para o ensino de desenvolvimento de jogos. A escolha do Curupira como protagonista não é apenas uma homenagem ao folclore brasileiro, mas também uma oportunidade de conscientização ambiental através da narrativa. O formato de plataforma 2D foi escolhido por sua acessibilidade técnica para fins didáticos e pela familiaridade do público geral com o gênero.

## 🎮 Análise do Jogo

**"Guardiões da Mata"** é um jogo de plataforma 2D de ação onde o jogador controla o Curupira, protetor mítico das florestas brasileiras. No jogo o protagonista possui a movimentação clássica de jogos de plataforma, podendo navegar pelo cenário se movendo em ambas as direções, esquerda e direita e saltando por obstáculos.

### Diferenciais

- **Protagonista e narrativa baseados no folclore brasileiro**
- **Estética pixel art** com paleta de cores vibrantes inspirada na fauna e flora brasileira
- **Projeto open-source** com finalidade educacional

## 🎨 Atmosfera do Jogo

O jogo tem um tom geral **aventuresco, místico e levemente melancólico**. 

O estilo visual é **pixel art**, com nível de detalhes mediano, sendo o sprite do personagem principal cerca de **32x21 pixels** e os tilesets **32x32 pixels**. Isso permite um nível moderado de detalhes, dessa forma o jogo é capaz de projetar ao jogador o que se deseja ser transmitido sem muitas abstrações, ao mesmo tempo que não põe em risco o desenvolvimento do jogo com sprites de alta resolução e alto tempo de desenvolvimento.

A paleta de cores é rica em **tons de verde e terrosos**.

### Inspirações

- Florestas dos filmes de **Hayao Miyazaki** (Princesa Mononoke)
- Estética visual de jogos como **Owlboy**, **Ori and the Blind Forest** e **Wild at Hearts**

## 🛠️ Tecnologias Utilizadas

### Python
Linguagem de programação principal utilizada no desenvolvimento do projeto. Python foi escolhido por sua simplicidade, legibilidade e vasta comunidade, facilitando o aprendizado e o desenvolvimento.

### Pygame

**Pygame** é uma biblioteca multiplataforma de código aberto escrita em Python, projetada para criar jogos e aplicações multimídia interativas.

#### O que é Pygame?

Pygame fornece funcionalidades para:
- **Gerenciamento de janelas e displays**: Criação e controle de janelas de jogo
- **Renderização gráfica**: Desenho de sprites, formas geométricas e textos
- **Input handling**: Processamento de eventos de teclado, mouse e joystick
- **Sistema de sprites**: Gerenciamento eficiente de objetos gráficos
- **Colisão**: Detecção de colisões entre objetos
- **Áudio**: Reprodução de sons e músicas
- **Timing**: Controle de FPS e animações

#### Por que Pygame?

- **Simplicidade**: API intuitiva e fácil de aprender
- **Educacional**: Ideal para ensino de programação e desenvolvimento de jogos
- **Leve**: Requisitos de sistema baixos
- **Documentação**: Excelente documentação e tutoriais disponíveis
- **Comunidade**: Grande comunidade ativa e suporte

## 📚 Documentação dos Métodos do Pygame Utilizados

Esta seção documenta todos os métodos e funcionalidades do Pygame utilizados neste projeto, explicando como funcionam e para que servem.

### Módulo: `pygame`

#### `pygame.init()`

**O que faz**: Inicializa todos os módulos do Pygame que foram importados.

**Como funciona**: 
- Deve ser chamado antes de usar qualquer funcionalidade do Pygame
- Inicializa os módulos: display (janela), font (fontes), mixer (áudio), etc.
- É seguro chamar múltiplas vezes (se já foi inicializado, não faz nada)
- Retorna uma tupla indicando quais módulos foram inicializados com sucesso

**Exemplo de uso**:
```python
pygame.init()  # Inicializa todos os módulos
```

**Quando usar**: Sempre no início do programa, antes de criar janelas ou usar qualquer funcionalidade do Pygame.

---

#### `pygame.quit()`

**O que faz**: Finaliza o Pygame e libera todos os recursos alocados.

**Como funciona**:
- Desinicializa todos os módulos do Pygame que foram inicializados
- Libera memória, fecha dispositivos de áudio, etc.
- Deve ser chamado antes de sair do programa

**Exemplo de uso**:
```python
pygame.quit()  # Finaliza o Pygame
```

**Quando usar**: No final do programa ou quando o jogador quer sair do jogo.

---

### Módulo: `pygame.display`

#### `pygame.display.set_mode(tamanho)`

**O que faz**: Cria uma janela ou tela para exibição.

**Parâmetros**:
- `tamanho`: Tupla `(largura, altura)` em pixels que define o tamanho da janela

**Retorna**: Uma `Surface` que representa a tela. Esta Surface é onde desenhamos tudo.

**Como funciona**:
- Cria uma janela do jogo com o tamanho especificado
- Retorna uma Surface especial que representa a tela
- Tudo que desenhamos nesta Surface aparece na janela

**Exemplo de uso**:
```python
screen = pygame.display.set_mode((640, 360))  # Cria janela 640x360
```

**Quando usar**: No início do jogo, antes de desenhar qualquer coisa.

---

#### `pygame.display.set_caption(título)`

**O que faz**: Define o título da janela do jogo.

**Parâmetros**:
- `título`: String com o texto que aparecerá na barra de título da janela

**Como funciona**:
- Altera o texto que aparece na barra de título da janela
- Útil para identificar o jogo ou mostrar informações

**Exemplo de uso**:
```python
pygame.display.set_caption('Phase 4')  # Define título da janela
```

**Quando usar**: Após criar a janela, para personalizar o título.

---

#### `pygame.display.flip()`

**O que faz**: Atualiza a tela, mostrando tudo que foi desenhado desde a última atualização.

**Como funciona**:
- Pega tudo que foi desenhado na Surface da tela e exibe na janela
- Deve ser chamado uma vez por frame, após desenhar tudo
- Alternativa: `pygame.display.update()` (mais lento, atualiza áreas específicas)

**Exemplo de uso**:
```python
# Desenha tudo...
screen.fill(BLUE)
player.draw(screen)
# ...

pygame.display.flip()  # Atualiza a tela, mostrando tudo
```

**Quando usar**: No final de cada frame do loop principal, após desenhar todos os elementos.

---

### Módulo: `pygame.time`

#### `pygame.time.Clock()`

**O que faz**: Cria um objeto Clock para controlar a taxa de frames (FPS).

**Retorna**: Um objeto `Clock` que pode ser usado para limitar o FPS.

**Como funciona**:
- Cria um objeto que mede o tempo entre frames
- Usado com `clock.tick(FPS)` para limitar quantos frames por segundo o jogo roda
- Importante para manter o jogo rodando na mesma velocidade em diferentes computadores

**Exemplo de uso**:
```python
clock = pygame.time.Clock()  # Cria o objeto Clock

# No loop do jogo:
clock.tick(60)  # Limita a 60 FPS
```

**Quando usar**: No início do jogo, antes do loop principal.

---

#### `clock.tick(FPS)`

**O que faz**: Limita a taxa de frames do jogo.

**Parâmetros**:
- `FPS`: Número de frames por segundo desejado (ex: 60 para 60 FPS)

**Como funciona**:
- Se o computador for muito rápido, espera para não rodar mais rápido que o FPS especificado
- Se for muito lento, roda o mais rápido possível (não força espera)
- Retorna o tempo em milissegundos desde a última chamada

**Exemplo de uso**:
```python
clock.tick(60)  # Limita a 60 frames por segundo
```

**Quando usar**: No final de cada iteração do loop principal do jogo.

---

### Módulo: `pygame.event`

#### `pygame.event.get()`

**O que faz**: Pega todos os eventos que aconteceram desde a última chamada.

**Retorna**: Uma lista de objetos `Event` representando eventos (teclas pressionadas, mouse clicado, janela fechada, etc.)

**Como funciona**:
- Coleta todos os eventos do sistema operacional relacionados ao jogo
- Eventos incluem: teclas pressionadas, mouse movido/clicado, janela fechada, etc.
- Cada evento é um objeto com propriedades como `type` e `key`

**Exemplo de uso**:
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

**Quando usar**: No início de cada frame do loop principal, para processar entrada do usuário.

---

#### Tipos de Eventos

##### `pygame.QUIT`

**O que é**: Evento disparado quando o usuário fecha a janela (clica no X).

**Como usar**:
```python
if event.type == pygame.QUIT:
    running = False  # Sai do loop do jogo
```

**Propriedades**: Não tem propriedades adicionais, apenas indica que a janela foi fechada.

---

##### `pygame.KEYDOWN`

**O que é**: Evento disparado quando uma tecla é pressionada.

**Como usar**:
```python
if event.type == pygame.KEYDOWN:
    if event.key == K_SPACE:  # Verifica qual tecla foi pressionada
        player.jump()
```

**Propriedades**:
- `event.key`: Qual tecla foi pressionada (ex: `K_SPACE`, `K_a`, `K_ESCAPE`)

**Teclas comuns**:
- `K_SPACE`: Barra de espaço
- `K_w`, `K_a`, `K_s`, `K_d`: Teclas WASD
- `K_ESCAPE`: Tecla ESC
- `K_RETURN`: Tecla ENTER
- `K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`: Setas direcionais

---

### Módulo: `pygame.key`

#### `pygame.key.get_pressed()`

**O que faz**: Retorna o estado de todas as teclas do teclado.

**Retorna**: Uma lista/array onde cada índice representa uma tecla. `True` se está pressionada, `False` se não está.

**Como funciona**:
- Diferente de `KEYDOWN`, que detecta quando uma tecla é pressionada uma vez
- `get_pressed()` verifica se a tecla está pressionada AGORA (mantida pressionada)
- Útil para movimento contínuo (andar enquanto segura a tecla)

**Exemplo de uso**:
```python
keys = pygame.key.get_pressed()
if keys[K_a]:  # Se a tecla A está pressionada
    player.move_left()
if keys[K_d]:  # Se a tecla D está pressionada
    player.move_right()
```

**Quando usar**: Para movimento contínuo ou ações que acontecem enquanto a tecla está pressionada.

**Diferença entre `KEYDOWN` e `get_pressed()`**:
- `KEYDOWN`: Detecta quando a tecla é PRESSIONADA (uma vez)
- `get_pressed()`: Verifica se a tecla está PRESSIONADA AGORA (contínuo)

---

### Módulo: `pygame.image`

#### `pygame.image.load(caminho)`

**O que faz**: Carrega uma imagem de um arquivo.

**Parâmetros**:
- `caminho`: String com o caminho para o arquivo de imagem (ex: `'assets/player.png'`)

**Retorna**: Uma `Surface` contendo a imagem carregada.

**Como funciona**:
- Lê o arquivo de imagem do disco
- Converte para um formato que o Pygame pode usar
- Retorna uma Surface que pode ser desenhada na tela

**Exemplo de uso**:
```python
player_image = pygame.image.load('assets/player.png')
```

**Formatos suportados**: PNG, JPG, BMP, GIF, etc.

**Quando usar**: Para carregar sprites, backgrounds e outras imagens do jogo.

---

#### `surface.convert()`

**O que faz**: Converte a Surface para o formato de pixel da tela.

**Retorna**: Uma nova Surface convertida (ou a mesma se já estiver no formato correto).

**Como funciona**:
- Otimiza a Surface para o formato usado pela tela
- Torna o desenho mais rápido
- Remove transparência (usa fundo preto)

**Exemplo de uso**:
```python
image = pygame.image.load('background.jpg').convert()
```

**Quando usar**: Para imagens que não precisam de transparência (backgrounds, por exemplo).

---

#### `surface.convert_alpha()`

**O que faz**: Converte a Surface mantendo o canal alpha (transparência).

**Retorna**: Uma nova Surface convertida com transparência preservada.

**Como funciona**:
- Similar a `convert()`, mas preserva a transparência
- Necessário para sprites com fundo transparente (PNG com alpha)

**Exemplo de uso**:
```python
sprite = pygame.image.load('player.png').convert_alpha()
```

**Quando usar**: Para sprites e imagens que precisam de transparência.

---

### Módulo: `pygame.transform`

#### `pygame.transform.scale(surface, tamanho)`

**O que faz**: Redimensiona uma Surface para um novo tamanho.

**Parâmetros**:
- `surface`: A Surface original que será redimensionada
- `tamanho`: Tupla `(nova_largura, nova_altura)` em pixels

**Retorna**: Uma nova Surface com o tamanho especificado.

**Como funciona**:
- Redimensiona a imagem usando interpolação
- Pode esticar ou encolher a imagem
- A qualidade pode diminuir se redimensionar muito

**Exemplo de uso**:
```python
# Redimensiona para 100x100 pixels
small_image = pygame.transform.scale(original_image, (100, 100))
```

**Quando usar**: Para ajustar o tamanho de sprites ou imagens para o tamanho desejado no jogo.

---

#### `pygame.transform.flip(surface, flip_x, flip_y)`

**O que faz**: Espelha uma Surface horizontalmente, verticalmente ou ambos.

**Parâmetros**:
- `surface`: A Surface original
- `flip_x`: `True` para espelhar horizontalmente (esquerda/direita)
- `flip_y`: `True` para espelhar verticalmente (cima/baixo)

**Retorna**: Uma nova Surface espelhada.

**Como funciona**:
- Cria uma cópia da imagem espelhada
- Útil para criar sprites virados (ex: personagem andando para esquerda)

**Exemplo de uso**:
```python
# Espelha horizontalmente (vira para esquerda)
flipped = pygame.transform.flip(sprite, True, False)
```

**Quando usar**: Para criar sprites virados sem precisar de sprites separados para cada direção.

---

### Módulo: `pygame.Surface`

#### `pygame.Surface(tamanho, flags)`

**O que faz**: Cria uma Surface vazia (imagem em branco).

**Parâmetros**:
- `tamanho`: Tupla `(largura, altura)` em pixels
- `flags`: Flags opcionais (ex: `pygame.SRCALPHA` para transparência)

**Retorna**: Uma nova Surface vazia.

**Como funciona**:
- Cria uma imagem vazia do tamanho especificado
- Pode ser preenchida com cores ou usada para compor outras imagens
- `pygame.SRCALPHA` permite transparência

**Exemplo de uso**:
```python
# Surface normal (sem transparência)
surface = pygame.Surface((100, 100))

# Surface com transparência
transparent = pygame.Surface((100, 100), pygame.SRCALPHA)
```

**Quando usar**: Para criar imagens programaticamente, composição de sprites, ou fallbacks quando imagens não carregam.

---

#### `surface.fill(cor)`

**O que faz**: Preenche toda a Surface com uma cor sólida.

**Parâmetros**:
- `cor`: Tupla RGB `(R, G, B)` ou RGBA `(R, G, B, A)`

**Como funciona**:
- Pinta toda a Surface com a cor especificada
- Útil para limpar a tela ou criar fundos sólidos

**Exemplo de uso**:
```python
screen.fill((0, 0, 0))  # Preenche de preto
surface.fill((255, 0, 0))  # Preenche de vermelho
```

**Quando usar**: Para limpar a tela no início de cada frame ou criar fundos coloridos.

---

#### `surface.blit(origem, destino, área_origem)`

**O que faz**: Desenha uma Surface em outra Surface.

**Parâmetros**:
- `origem`: A Surface que será desenhada
- `destino`: Tupla `(x, y)` indicando onde desenhar na Surface destino
- `área_origem` (opcional): Tupla `(x, y, largura, altura)` para desenhar apenas uma parte da origem

**Como funciona**:
- Copia pixels de uma Surface para outra
- É assim que desenhamos sprites, textos e imagens na tela
- O parâmetro `área_origem` permite desenhar apenas uma parte da imagem (útil para spritesheets)

**Exemplo de uso**:
```python
# Desenha sprite na posição (100, 50)
screen.blit(player_sprite, (100, 50))

# Desenha apenas uma parte do background (útil para câmera)
screen.blit(background, (0, 0), (camera_x, 0, screen_width, screen_height))
```

**Quando usar**: Para desenhar qualquer imagem, sprite ou texto na tela. É o método principal de renderização.

---

### Módulo: `pygame.font`

#### `pygame.font.SysFont(nome, tamanho, negrito, itálico)`

**O que faz**: Cria uma fonte usando uma fonte do sistema operacional.

**Parâmetros**:
- `nome`: Nome da fonte (ex: `'arial'`, `'times'`) ou `None` para fonte padrão
- `tamanho`: Tamanho da fonte em pixels
- `negrito`: `True` para negrito, `False` para normal
- `itálico`: `True` para itálico, `False` para normal

**Retorna**: Um objeto `Font` que pode renderizar texto.

**Como funciona**:
- Usa uma fonte instalada no sistema operacional
- Mais rápido que carregar fontes de arquivo
- Pode variar entre sistemas (diferentes sistemas têm fontes diferentes)

**Exemplo de uso**:
```python
font = pygame.font.SysFont('arial', 20, True, False)  # Arial, 20px, negrito
```

**Quando usar**: Para criar textos simples usando fontes do sistema.

---

#### `font.render(texto, antialiasing, cor_texto, cor_fundo)`

**O que faz**: Cria uma imagem (Surface) com o texto renderizado.

**Parâmetros**:
- `texto`: String com o texto a ser renderizado
- `antialiasing`: `True` para texto suave (menos pixelado), `False` para texto pixelado
- `cor_texto`: Tupla RGB `(R, G, B)` com a cor do texto
- `cor_fundo` (opcional): Tupla RGB com a cor de fundo (se não especificar, fundo transparente)

**Retorna**: Uma `Surface` contendo o texto renderizado.

**Como funciona**:
- Converte texto em uma imagem
- A Surface retornada pode ser desenhada com `blit()`
- `antialiasing=True` deixa o texto mais suave mas mais lento

**Exemplo de uso**:
```python
text_surface = font.render('Hello World', True, (255, 255, 255))  # Texto branco
screen.blit(text_surface, (100, 100))  # Desenha na tela
```

**Quando usar**: Para exibir qualquer texto no jogo (pontuação, menus, mensagens).

---

### Módulo: `pygame.draw`

#### `pygame.draw.rect(surface, cor, rect, largura)`

**O que faz**: Desenha um retângulo em uma Surface.

**Parâmetros**:
- `surface`: Surface onde desenhar
- `cor`: Tupla RGB `(R, G, B)` com a cor do retângulo
- `rect`: Objeto `Rect` ou tupla `(x, y, largura, altura)`
- `largura` (opcional): Largura da borda. `0` (padrão) = preenchido, `>0` = apenas borda

**Como funciona**:
- Desenha um retângulo na posição e tamanho especificados
- Se `largura=0`, preenche o retângulo
- Se `largura>0`, desenha apenas a borda

**Exemplo de uso**:
```python
# Retângulo preenchido
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

# Retângulo apenas com borda
pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)
```

**Quando usar**: Para desenhar formas simples, debug (mostrar hitboxes), ou versões sem sprite dos objetos.

---

### Classe: `pygame.Rect`

#### O que é `pygame.Rect`?

`pygame.Rect` é uma classe que representa um retângulo. É muito usada para posicionamento e detecção de colisões.

**Propriedades principais**:
- `x`, `y`: Posição do canto superior esquerdo
- `width`, `height`: Largura e altura
- `left`, `right`: Coordenada X da borda esquerda/direita
- `top`, `bottom`: Coordenada Y da borda superior/inferior
- `centerx`, `centery`: Coordenada X/Y do centro
- `center`: Tupla `(centerx, centery)`
- `topleft`, `topright`, `bottomleft`, `bottomright`: Tuplas com coordenadas dos cantos

**Como criar**:
```python
rect = pygame.Rect(x, y, width, height)
```

---

#### `rect.colliderect(outro_rect)`

**O que faz**: Verifica se dois retângulos se sobrepõem (colidem).

**Parâmetros**:
- `outro_rect`: Outro objeto `Rect` para verificar colisão

**Retorna**: `True` se há colisão, `False` caso contrário.

**Como funciona**:
- Verifica se há sobreposição entre os dois retângulos
- Muito eficiente e rápido
- Usado para detectar colisões entre objetos do jogo

**Exemplo de uso**:
```python
if player.colliderect(enemy):
    player.die()  # Se colidir com inimigo, morre

if player.colliderect(door):
    level_complete()  # Se colidir com porta, completa nível
```

**Quando usar**: Para detectar colisões entre qualquer objeto retangular do jogo (jogador, inimigos, plataformas, coletáveis).

---

#### `rect.move(x, y)`

**O que faz**: Retorna um novo Rect deslocado por uma quantidade.

**Parâmetros**:
- `x`: Quantidade de pixels para mover horizontalmente
- `y`: Quantidade de pixels para mover verticalmente

**Retorna**: Um novo `Rect` na nova posição (não modifica o original).

**Como funciona**:
- Cria uma cópia do Rect em uma nova posição
- Útil para cálculos sem modificar o original
- Usado no sistema de câmera para converter coordenadas

**Exemplo de uso**:
```python
# Move 10 pixels para direita, 5 para baixo
new_rect = old_rect.move(10, 5)
```

**Quando usar**: Para cálculos de posição, sistema de câmera, ou quando precisa de uma cópia deslocada.

---

### Módulo: `pygame.locals`

Este módulo contém constantes para eventos e teclas, facilitando o uso sem precisar escrever `pygame.KEYDOWN`, `pygame.K_SPACE`, etc.

**Importação comum**:
```python
from pygame.locals import *
```

**Constantes de eventos**:
- `QUIT`: Evento de fechar janela
- `KEYDOWN`: Tecla pressionada
- `KEYUP`: Tecla solta
- `MOUSEBUTTONDOWN`: Botão do mouse pressionado

**Constantes de teclas**:
- `K_SPACE`: Barra de espaço
- `K_a`, `K_b`, `K_c`, etc.: Letras
- `K_ESCAPE`: ESC
- `K_RETURN`: ENTER
- `K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`: Setas direcionais
- `K_w`, `K_a`, `K_s`, `K_d`: Teclas WASD

**Exemplo de uso**:
```python
from pygame.locals import *

if event.key == K_SPACE:  # Mais simples que pygame.K_SPACE
    player.jump()
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Pygame 2.6.1 ou superior

### Instalação

1. Clone ou baixe o repositório
2. Instale o Pygame (se ainda não tiver):
```bash
pip install pygame
```

### Executar o Jogo

Para executar o jogo completo com gerenciador de fases:
```bash
python extra/phases/game_manager.py
```

Para executar uma fase específica:
```bash
# Fase 4
python extra/phases/phase4.py

# Fase 5
python extra/phases/phase5.py

# Fase 6
python extra/phases/phase6.py
```

## 🎮 Controles

- **A / ←**: Mover para esquerda
- **D / →**: Mover para direita
- **W / Espaço**: Pular (pulo duplo disponível)
- **E**: Dash/Avanço (movimento rápido)
- **W (enquanto encostado na parede)**: Escalar parede
- **R**: Reiniciar fase (quando morrer ou completar)
- **N**: Próxima fase (quando completar)
- **ESC**: Sair do jogo

## 📚 Conceitos de Programação Ensinados

Este projeto aborda diversos conceitos importantes de programação:

### Programação Orientada a Objetos (POO)
- **Classes e Objetos**: Cada entidade do jogo é uma classe
- **Herança**: Classes herdam de `pygame.Rect` para obter funcionalidades de retângulo
- **Encapsulamento**: Cada classe gerencia seu próprio estado
- **Polimorfismo**: Diferentes classes com métodos `draw()` e `update()`

### Conceitos Específicos do Python
- **`__init__`**: Construtor de classes - método especial chamado automaticamente quando criamos um objeto
- **`super()`**: Chamada ao construtor da classe pai - permite herdar funcionalidades da classe base
- **`nonlocal`**: Modificação de variáveis do escopo externo em funções aninhadas
- **Módulos e Pacotes**: Organização do código em módulos reutilizáveis

### Conceitos de Desenvolvimento de Jogos
- **Game Loop**: Loop principal do jogo que atualiza e desenha continuamente
- **Event Handling**: Processamento de eventos (teclado, mouse)
- **Collision Detection**: Detecção de colisões usando `colliderect()`
- **Sprite Animation**: Animações de sprites usando múltiplos frames
- **Camera System**: Sistema de câmera para mundos maiores que a tela
- **State Management**: Gerenciamento de estados do jogo (jogando, pausado, game over)

## 🎓 Aspectos Educacionais

Este projeto serve como material didático para:

1. **Aprendizado de Python**: Sintaxe, estruturas de dados, funções, classes
2. **Programação Orientada a Objetos**: Classes, herança, encapsulamento, polimorfismo
3. **Desenvolvimento de Jogos**: Game loop, física, colisões, animações, câmera
4. **Arquitetura de Software**: Modularidade, organização de código, reutilização
5. **Cultura Brasileira**: Folclore, preservação ambiental, valorização da cultura nacional

## 📝 Fases do Jogo

### Fase 4
- **Características**: Tela fixa, sem câmera, sem sprites
- **Objetivo**: Introduzir mecânicas básicas de movimento e colisão
- **Foco Educacional**: Conceitos básicos de Pygame, eventos, colisão simples

### Fase 5
- **Características**: Câmera, mundo maior que a tela, sem sprites
- **Objetivo**: Introduzir sistema de câmera e mundos maiores
- **Foco Educacional**: Sistema de câmera, conversão de coordenadas mundo-tela, parallax

### Fase 6
- **Características**: Sprites, animações, mundo gigante, múltiplos inimigos e obstáculos
- **Objetivo**: Experiência completa com todos os recursos
- **Foco Educacional**: Animações, sprites, gerenciamento de assets, mundos grandes

## 🤝 Contribuindo

Este é um projeto educacional open-source. Contribuições são bem-vindas! 

Áreas onde você pode contribuir:
- Melhorias no código
- Adição de novas fases
- Criação de novos sprites
- Documentação
- Correção de bugs

## 📄 Licença

Este projeto é desenvolvido com fins educacionais para a disciplina ACEX1 do IFBA.

## 👥 Autores

Projeto desenvolvido para a disciplina **ACEX1 - Atividades Curriculares de Extensão 1** do curso de **Sistemas de Informações do IFBA**.

## 📖 Referências

- [Documentação Oficial do Pygame](https://www.pygame.org/docs/)
- [Tutorial de Pygame](https://www.pygame.org/wiki/tutorials)
- Folclore Brasileiro - Curupira
- Filmes de Hayao Miyazaki
- Jogos: Owlboy, Ori and the Blind Forest, Wild at Hearts

## 🎯 Próximos Passos

Possíveis melhorias e expansões:
- Adição de sistema de som e música
- Mais fases e níveis
- Sistema de pontuação
- Menu principal
- Sistema de save/load
- Mais tipos de inimigos e obstáculos
- Power-ups e coletáveis

---

**Desenvolvido com ❤️ para o ensino de programação e valorização da cultura brasileira**

