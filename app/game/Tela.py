import pygame
from app.util.PyGameUtil import PyGameUtil
from app.game.Texto import Texto

IMAGEM_BACKGROUND = PyGameUtil().load_img_scale_2x('bg.png')


class Tela:
    def __init__(self, LARGURA, ALTURA):
        self.largura = LARGURA
        self.altura = ALTURA
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.game_over = False  # Flag para indicar se a tela de game over deve ser exibida

    def tela_principal(self, passaros, canos, chao, pontos):
        self.tela.blit(IMAGEM_BACKGROUND, (0, 0))
        for passaro in passaros:
            passaro.desenhar(self.tela, self.game_over)  # Adicione o parâmetro game_over aqui
        for cano in canos:
            cano.desenhar(self.tela)

        Texto().pontos_tela_principal(self.tela, self.largura, pontos)
        chao.desenhar(self.tela)

        if self.game_over:
            tela_em_escala_de_cinza = self.aplicar_cinza(self.tela.copy())
            self.tela.blit(tela_em_escala_de_cinza, (0, 0))
            self.tela_game_over(pontos)

        pygame.display.update()

    def tela_game_over(self, pontos):
        # Configurar a tela de game over no centro e com 2/3 da largura e altura da tela principal
        tela_game_over = pygame.Surface((self.largura * 2 / 3, self.altura * 2 / 3))
        tela_game_over.fill((255, 255, 255))  # Preencha com a cor de fundo desejada
        tela_game_over_rect = tela_game_over.get_rect(center=self.tela.get_rect().center)
        self.tela.blit(tela_game_over, tela_game_over_rect)

        Texto().pontos_tela_game_over(self.tela, pontos)

    def aplicar_cinza(self, superficie):
        superficie_cinza = pygame.transform.grayscale(superficie)
        return superficie_cinza

    def ativar_tela_game_over(self):
        self.game_over = True

    def desativar_tela_game_over(self):
        self.game_over = False
