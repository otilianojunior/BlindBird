import os
import pygame
from dotenv import load_dotenv
from app.util.PyGameUtil import PyGameUtil


class Texto:
    def __init__(self):
        load_dotenv()
        self.base_dir = os.getenv("PATH_APP")
        PyGameUtil().init_font()
        self.FONTE_PONTOS = self.load_font_pontos()

    def load_font_pontos(self):
        try:
            font_path = os.path.join(self.base_dir, 'assets/fonts/screenlogger-cool.ttf')
            font_size = 80
            fonte = PyGameUtil().load_font(font_path, font_size)
            return fonte
        except Exception as ex:
            raise Exception(f"Erro ao carregar fontes: {ex}")

    def pontos_tela_principal(self, tela, largura, pontos):
        texto = self.FONTE_PONTOS.render(f"{pontos}", 1, (255, 255, 255))
        x = (largura - texto.get_width()) // 2
        y = 10
        tela.blit(texto, (x, y))

    def pontos_tela_game_over(self, tela, pontos):
        texto = self.FONTE_PONTOS.render(f"Pontos: {pontos}", 1, (255, 0, 0))
        tela_rect = tela.get_rect()
        # Defina a posição vertical do texto (2/3 da altura da tela)
        texto_y = tela_rect.height * 1 / 3
        # Centralize horizontalmente o texto
        texto_rect = texto.get_rect(midtop=(tela_rect.centerx, texto_y))
        tela.blit(texto, texto_rect)
