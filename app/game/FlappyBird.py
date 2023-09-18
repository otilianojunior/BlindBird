import pygame
import random
from app.util.PyGameUtil import PyGameUtil


TELA_LARGURA = 500
TELA_ALTURA = 800


IMAGEM_CANO = PyGameUtil().load_img_scale_2x('pipe.png')
IMAGEM_CHAO = PyGameUtil().load_img_scale_2x('base.png')
IMAGEM_BACKGROUND = PyGameUtil().load_img_scale_2x('bg.png')
IMAGEM_PASSARO = [
    PyGameUtil().load_img_scale_2x('bird1.png'),
    PyGameUtil().load_img_scale_2x('bird2.png'),
    PyGameUtil().load_img_scale_2x('bird3.png'),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGEM_PASSARO

    #animação da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.image = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento, formula do deslocamento S = (so + vot + at²)/2
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade + self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16

        #auxilio para o pulo
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # define qual a imagem do passaro a ser usada
        self.contagem_imagem += 1

        # batidas de asa
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o passaro tiver caindo não bate asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imaggem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=posicao_centro_imaggem)
        tela.blit(imagem_rotacionada, retangulo.topleft)





class Cano:
    pass


class Chao:
    pass
