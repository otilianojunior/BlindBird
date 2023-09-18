import pygame
import random
from app.util.ImageUtil import ImageUtil
from app.util.PyGameUtil import PyGameUtil


TELA_LARGURA = 500
TELA_ALTURA = 800


IMAGEM_CANO = PyGameUtil().load_img_scale_2x('pipe.png')

#
# IMAGEM_CHAO = PyGameUtil().scale_2x(PyGameUtil().load_image(ImageUtil.load_image('base.png')))
# IMAGEM_BACKGROUND = PyGameUtil().scale_2x(PyGameUtil().load_image(ImageUtil.load_image('bg.png')))
# IMAGEM_PASSARO = PyGameUtil().scale_2x(PyGameUtil().load_image(ImageUtil.load_image('bird1.png')))
