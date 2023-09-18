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


# if __name__ == "__main__":
#     util = PyGameUtil()
#     image_name = "pipe.png"
#     try:
#         loaded_image = util.load_img_scale_2x(image_name)
#         print(loaded_image)
#     except Exception as ex:
#         print(f"Erro: {ex}")