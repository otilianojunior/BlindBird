import os
import pygame
from dotenv import load_dotenv
from app.util.PyGameUtil import PyGameUtil


class Texto:
    def __init__(self):
        load_dotenv()
        self.base_dir = os.getenv("PATH_APP")
        PyGameUtil().init_font()
        self.FONTE_PONTOS = self.load_font()

    def load_font(self):
        try:
            font_path = os.path.join(self.base_dir, 'assets/fonts/screenlogger-cool.ttf')
            font_size = 80
            return pygame.font.Font(font_path, font_size)
        except Exception as ex:
            raise Exception(f"Erro ao carregar fontes: {ex}")

    def desenhar_pontos(self, tela, largura, pontos):
        texto = self.FONTE_PONTOS.render(f"{pontos}", 1, (255, 255, 255))
        x = (largura - texto.get_width()) // 2
        y = 10
        tela.blit(texto, (x, y))
