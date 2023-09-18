import os
from dotenv import load_dotenv


class ImageUtil:
    def __init__(self):
        load_dotenv()
        self.base_dir = os.getenv("PATH_APP")

    def file_exists(self, image_name):
        try:
            image_path = os.path.join(self.base_dir, 'assets/imgs', image_name)
            return os.path.exists(image_path)
        except Exception as ex:
            raise Exception(f"Erro ao verificar a existência do arquivo: {ex}")

    def image_path(self, image_name):
        try:
            if self.file_exists(image_name):
                image_path = os.path.join(self.base_dir, 'assets/imgs/', image_name)
                return image_path
            else:
                raise FileNotFoundError(f"Arquivo de imagem não encontrado: {image_name}")
        except Exception as ex:
            raise Exception(f"Erro ao carregar o caminho da imagem: {ex}")


# if __name__ == "__main__":
#     util = ImageUtil()
#     image_name = "pipe.png"
#     try:
#         loaded_image = util.image_path(image_name)
#         print(loaded_image)
#     except Exception as ex:
#         print(f"Erro: {ex}")
