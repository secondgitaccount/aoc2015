UP = '^'
RIGHT = '>'
DOWN = 'v'
LEFT = '<'


def posicoes(direcoes):
    linha, coluna = (0, 0)
    posicoes = {(linha, coluna)}

    for direcao in direcoes:
        if direcao == UP:
            linha -= 1
        elif direcao == RIGHT:
            coluna += 1
        elif direcao == DOWN:
            linha += 1
        elif direcao == LEFT:
            coluna -= 1

        posicoes.add((linha, coluna))

    return posicoes


def solucao1(direcoes):
    return len(posicoes(direcoes))


def solucao2(direcoes):
    noel = posicoes(direcao for i, direcao in enumerate(direcoes) if not i % 2)
    robo = posicoes(direcao for i, direcao in enumerate(direcoes) if i % 2)

    return len(robo.union(noel))
