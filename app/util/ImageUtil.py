import os


class ImageUtil:
    def file_exists(self, image_name):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(base_dir, 'app/assets/imgs', image_name)
            return os.path.exists(image_path)
        except Exception as ex:
            raise Exception(f"Erro ao verificar a existência do arquivo: {ex}")

    def load_image(self, image_name):
        try:
            if self.file_exists(image_name):
                base_dir = os.path.dirname(os.path.abspath(__file__))
                image_path = os.path.join(base_dir, 'app/assets/imgs/', image_name)
                return image_path
            else:
                raise FileNotFoundError(f"Arquivo de imagem não encontrado: {image_name}")
        except Exception as ex:
            raise Exception(f"Erro ao carregar o caminho da imagem: {ex}")


if __name__ == "__main__":
    util = ImageUtil()
    image_name = "pipe.png"
    try:
        loaded_image = util.file_exists(image_name)
        print(loaded_image)
    except Exception as ex:
        print(f"Erro: {ex}")
