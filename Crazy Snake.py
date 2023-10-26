import pygame
from pygame.locals import *
from sys import exit
from random import randint
import random

pygame.init()

#Declaração de variáveis em geral: 

largura = 640
altura = 480

x_cobra = largura/2
y_cobra = altura/2

x_maca = randint(40, 600)
y_maca = randint(50, 430)

x_bloco_preto = randint(40, 600)
y_bloco_preto = randint(50, 430)
bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)  # Adicione essa linha

comprimentoini = 5
game_over = 0

xcontrole = 20
ycontrole = 0
pontos = 0

fonte = pygame.font.SysFont("Arial", 40, True, False)
fonte1 = pygame.font.SysFont("Arial", 40, False, False)


contador_frames = 0  # Contador de frames
intervalo_frames = 100  # Intervalo de frames para atualizar a posição do bloco preto
velocidade_objeto_preto = 10  # Velocidade inicial do objeto preto

pygame.mixer.music.set_volume(0.2)
musicafundo = pygame.mixer.music.load("smw_castle_clear.wav")
pygame.mixer.music.play(-1)
barulhocoli = pygame.mixer.Sound("smw_jump.wav")

fundo_jogo_imagem = pygame.image.load('imagens/fundo_jogo.jpg')
tela_inicial_imagem = pygame.image.load("imagens/tela_inicial_crazy_snake.png")
fundo_lost_imagem = pygame.image.load("imagens/tela_lost_crazy_snake.png")
imagem_cabeca = pygame.image.load("imagens/cabeca_cobra.png")
imagem_cabeca_cima = pygame.image.load("imagens/cabeça_cobra_cima.png")
imagem_cabeca_baixo = pygame.image.load("imagens/cabeça_cobra_baixo.png")
imagem_cabeca_esquerda = pygame.image.load("imagens/cabeça_cobra_esquerda.png")
imagem_cabeca_direita = pygame.image.load("imagens/cabeça_cobra_direita.png")
imagem_bloco_preto = pygame.image.load("imagens/imagem_bloco_preto.png")
imagem_maça = pygame.image.load("imagens/imagem_maça.png")

#Fim da declaração de variáveis.

tela = pygame.display.set_mode((largura, altura),)
pygame.display.set_caption("Crazy Snake")

def telainicial():

    global contador_frames, velocidade, x_bloco_preto, y_bloco_preto, largura, altura, velocidade_objeto_preto
    running = True
    while running:
        #verificar eventos de entrada
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False # Encerrar a tela de início se qualquer tecla for pressionada
        velocidade = 9 + pontos // 1
        # desenhar o fundo e a mensagem de inicio na tela
        tela.blit(tela_inicial_imagem, (0,0))
        # atualizar tela
        pygame.display.flip()
        
        contador_frames += 1
        if contador_frames >= intervalo_frames:
            contador_frames = 0

        x_bloco_preto += velocidade_objeto_preto
        y_bloco_preto += velocidade_objeto_preto

        # Verificar se o objeto preto atingiu as bordas da tela
        if x_bloco_preto < 0 or x_bloco_preto > largura - 20:
            velocidade_objeto_preto *= -1  # Inverter a direção do movimento
        if y_bloco_preto < 0 or y_bloco_preto > altura - 20:
            velocidade_objeto_preto *= -1  # Inverter a direção do movimento

def aumentacobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))

def exibir_pontuacao_final(pontos):
    mensagem_final = f"Sua pontuação final: {pontos}"
    texto_final = fonte1.render(mensagem_final, True, (255, 255, 255))
    posicao_x = largura - texto_final.get_width() - 20  
    posicao_y = 20  
    tela.blit(texto_final, (posicao_x, posicao_y))
    pygame.display.flip()

def reset_jogo():
    global x_cobra, y_cobra, y_maca, x_maca, x_bloco_preto, y_bloco_preto, bloco_preto, comprimentoini, xcontrole, ycontrole, pontos, relogio, lista_cobra
    x_cobra = largura/2
    y_cobra = altura/2

    x_maca = randint(40, 600)
    y_maca = randint(50, 430)

    x_bloco_preto = randint(40, 600)
    y_bloco_preto = randint(50, 430)
    bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)  

    comprimentoini = 5

    xcontrole = 20
    ycontrole = 0
    pontos = 0
    telainicial()
    relogio = pygame.time.Clock()
    lista_cobra = []
    executar()

def executar():
    global x_bloco_preto, y_bloco_preto, bloco_preto, x_maca, y_maca, pontos, x_cobra, y_cobra, xcontrole, ycontrole, comprimentoini

    while True:
        tela.blit(fundo_jogo_imagem, (0, 0))
        tela.blit(imagem_bloco_preto, (x_bloco_preto, y_bloco_preto))
        tela.blit(imagem_maça, (x_maca, y_maca))
        relogio.tick(100)
        tela.fill((255,255,255))
        tela.blit(fundo_jogo_imagem, (0, 0))
        mensagem = f"Pontos: {pontos}"
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if xcontrole == velocidade:
                        pass
                    else:
                        xcontrole = -velocidade
                        ycontrole = 0
                if event.key == K_RIGHT:
                    if xcontrole == -velocidade:
                        pass
                    else:
                        xcontrole = velocidade
                        ycontrole = 0
                if event.key == K_UP:
                    if ycontrole == velocidade:
                        pass
                    else:
                        ycontrole = -velocidade
                        xcontrole = 0
                if event.key == K_DOWN:
                    if ycontrole == -velocidade:
                        pass
                    else:
                        ycontrole = velocidade
                        xcontrole = 0
        x_cobra = x_cobra + (xcontrole/10)
        y_cobra = y_cobra + (ycontrole/10)
        x_cobra = x_cobra + (xcontrole/10)
        y_cobra = y_cobra + (ycontrole/10)

        if xcontrole == 0 and ycontrole < 0:
            imagem_cabeca = imagem_cabeca_cima
        elif xcontrole == 0 and ycontrole > 0:
            imagem_cabeca = imagem_cabeca_baixo
        elif xcontrole < 0 and ycontrole == 0:
            imagem_cabeca = imagem_cabeca_esquerda
        elif xcontrole > 0 and ycontrole == 0:
            imagem_cabeca = imagem_cabeca_direita


        if x_cobra < 0 or x_cobra > largura or y_cobra < 0 or y_cobra > altura:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            reset_jogo()
                        elif event.key == pygame.K_s:
                            pygame.quit()
                            exit()
                tela.blit(fundo_lost_imagem, (0, 0))
                exibir_pontuacao_final(pontos)
                pygame.display.flip()
                    

                        
        cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
        maca = tela.blit(imagem_maça, (x_maca, y_maca))
        bloco = tela.blit(imagem_bloco_preto, (x_bloco_preto, y_bloco_preto))

        if cobra.colliderect(maca):
            x_maca = randint(40, 600)
            y_maca = randint(50, 430)
            pontos = pontos + 1
            barulhocoli.play()
            comprimentoini = comprimentoini + 10

        if cobra.colliderect(bloco):
            x_bloco_preto = randint(40, 600)
            y_bloco_preto = randint(50, 430)
            bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)
            pygame.display.flip()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            reset_jogo()
                        elif event.key == pygame.K_s:
                            pygame.quit()
                            exit()
                tela.blit(fundo_lost_imagem, (0, 0))
                exibir_pontuacao_final(pontos)
                pygame.display.flip()   


        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)
        lista_cobra.append(lista_cabeca)

        if lista_cobra.count(lista_cabeca) > 1:
            while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                reset_jogo()
                            elif event.key == pygame.K_s:
                                pygame.quit()
                                exit()
                    tela.blit(fundo_lost_imagem, (0, 0))
                    exibir_pontuacao_final(pontos)
                    pygame.display.flip()
                        

        if len (lista_cobra) > comprimentoini:

            del lista_cobra[0]
            
        aumentacobra (lista_cobra)
        tela.blit(texto_formatado, (420, 40))
        tela.blit(imagem_cabeca, (x_cobra, y_cobra))

        if random.random() < 0.01:  
            x_bloco_preto = random.randint(40, 600)
            y_bloco_preto = random.randint(50, 430)
            bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)

        pygame.display.update()

telainicial()
relogio = pygame.time.Clock()
lista_cobra = []
executar()