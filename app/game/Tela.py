import pygame
from app.util.PyGameUtil import PyGameUtil
from app.game.Texto import Texto

IMAGEM_BACKGROUND = PyGameUtil().load_img_scale_2x('bg.png')


class Tela:
    def __init__(self, LARGURA, ALTURA):
        self.largura = LARGURA
        self.altura = ALTURA
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))

    def desenhar_tela(self, passaros, canos, chao, pontos):
        self.tela.blit(IMAGEM_BACKGROUND, (0, 0))
        for passaro in passaros:
            passaro.desenhar(self.tela)
        for cano in canos:
            cano.desenhar(self.tela)

        Texto().desenhar_pontos(self.tela, self.largura, pontos)
        chao.desenhar(self.tela)
        pygame.display.update()
