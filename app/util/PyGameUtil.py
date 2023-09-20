import pygame
from app.util.ImageUtil import ImageUtil


class PyGameUtil:
    def load_image(self, image_name):
        try:
            image = pygame.image.load(ImageUtil().image_path(image_name))
            return image
        except Exception as ex:
            raise Exception(f"Erro ao carregar a imagem: {ex}")

    def load_img_scale_2x(self, image_name):
        try:
            imagem_2x = pygame.transform.scale2x(self.load_image(image_name))
            return imagem_2x
        except Exception as ex:
            raise Exception(f"Erro ao carregar e trasformar escala da imagem: {ex}")

    def rotate_image(self, imagem, angulo):
        try:
            imagem_rotacionada = pygame.transform.rotate(imagem, angulo)
            return imagem_rotacionada
        except Exception as ex:
            raise Exception(f"Erro ao rotacionar imagem: {ex}")

    def mask_surface(self, imagem):
        try:
            mascara_colisao = pygame.mask.from_surface(imagem)
            return mascara_colisao
        except Exception as ex:
            raise Exception(f"Erro ao fazer mascara de colisao da imagem: {ex}")

    def new_superficie(self, imagem):
        try:
            superficie = pygame.transform.flip(imagem, False, True)
            return superficie
        except Exception as ex:
            raise Exception(f"Erro ao criar nova superficie: {ex}")

    def init_font(self):
        try:
            return pygame.font.init()
        except Exception as ex:
            raise Exception(f"Erro ao iniciar fontes no pygame: {ex}")
