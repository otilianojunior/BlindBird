import pygame
from app.game.Chao import Chao
from app.game.Cano import Cano
from app.game.Tela import Tela
from app.game.Texto import Texto
from app.game.Passaro import Passaro


def verificar_colisao(passaros, canos, tela):
    if not tela.game_over:
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    tela.game_over = True
                    break


def blink_main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = Tela(500, 800)
    texto = Texto()
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    tela.game_over = False

    while rodando:
        relogio.tick(30)

        # interação com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if not tela.game_over:
                        for passaro in passaros:
                            passaro.pular()

        verificar_colisao(passaros, canos, tela)

        if not tela.game_over:
            for passaro in passaros:
                passaro.mover()
            chao.mover()

            adicionar_cano = False
            remover_canos = []
            for cano in canos:
                for i, passaro in enumerate(passaros):
                    if not cano.passou and passaro.x > cano.x:
                        cano.passou = True
                        adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)

            if adicionar_cano:
                pontos += 1
                canos.append(Cano(600))
            for cano in remover_canos:
                canos.remove(cano)

            for i, passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                    tela.game_over = True

        tela.tela_principal(passaros, canos, chao, pontos)
        if tela.game_over:
            tela.tela_game_over(pontos)
