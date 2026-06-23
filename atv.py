import pygame
import random
import sys

# Inicialização
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 400
TAMANHO = 20

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 35)


def desenhar_cobra(cobra):
    for bloco in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            (bloco[0], bloco[1], TAMANHO, TAMANHO)
        )


def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))


def gerar_comida():
    x = random.randrange(0, LARGURA, TAMANHO)
    y = random.randrange(0, ALTURA, TAMANHO)
    return [x, y]


def jogo():
    x = LARGURA // 2
    y = ALTURA // 2

    dx = TAMANHO
    dy = 0

    cobra = [[x, y]]
    tamanho = 1

    comida = gerar_comida()

    rodando = True

    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -TAMANHO

                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = TAMANHO

                elif evento.key == pygame.K_LEFT and dx == 0:
                    dx = -TAMANHO
                    dy = 0

                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx = TAMANHO
                    dy = 0

        x += dx
        y += dy

        # Perdeu encostando na parede
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            rodando = False

        cobra.append([x, y])

        if len(cobra) > tamanho:
            del cobra[0]

        # Encostou no próprio corpo
        if [x, y] in cobra[:-1]:
            rodando = False

        # Comeu comida
        if [x, y] == comida:
            tamanho += 1
            comida = gerar_comida()

        # Desenhar
        tela.fill(PRETO)

        pygame.draw.rect(
            tela,
            VERMELHO,
            (comida[0], comida[1], TAMANHO, TAMANHO)
        )

        desenhar_cobra(cobra)
        mostrar_pontos(tamanho - 1)

        pygame.display.update()

        clock.tick(10)

    print("Fim de jogo! Pontos:", tamanho - 1)


jogo()