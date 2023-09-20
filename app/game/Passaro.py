from app.util.PyGameUtil import PyGameUtil


IMAGEM_PASSARO = [
    PyGameUtil().load_img_scale_2x('bird1.png'),
    PyGameUtil().load_img_scale_2x('bird2.png'),
    PyGameUtil().load_img_scale_2x('bird3.png'),
    PyGameUtil().load_img_scale_2x('bird4.png'),
]


class Passaro:
    IMGS = IMAGEM_PASSARO

    # animações da rotação
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
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = - 11 #altura do pulo do passaro
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > - 35:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela, game_over):
        # Definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        if game_over:
            # Usar a imagem do passaro bird4 quando o jogo estiver no estado de "game over"
            self.imagem = self.IMGS[3]
        else:
            if self.contagem_imagem < self.TEMPO_ANIMACAO:
                self.imagem = self.IMGS[0]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
                self.imagem = self.IMGS[1]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
                self.imagem = self.IMGS[2]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
                self.imagem = self.IMGS[1]
            elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
                self.imagem = self.IMGS[0]
                self.contagem_imagem = 0

        # se o passaro tiver caindo eu não vou bater asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        # desenhar a imagem
        imagem_rotacionada = PyGameUtil().rotate_image(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return PyGameUtil().mask_surface(self.imagem)
