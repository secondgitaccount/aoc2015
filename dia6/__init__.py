def instrucao(it):
    for i in it:
        tipo, ns = i.strip().replace('turn ', '').replace(' through ', ',').split(' ')
        indices = map(int, ns.split(','))
        yield tipo, *indices


def indice(linha, coluna, colunas=1000):
    return coluna + (linha * colunas)


def monta_linha(n, v=0):
    return [v for _ in range(0, n)]


def monta_grade(n, v=0):
    return [monta_linha(n, v) for _ in range(0, n)]


def opera_interruptor(grade, fn, li, ci, lf, cf):
    for linha in range(li, lf + 1):
        for coluna in range(ci, cf + 1):
            grade[linha][coluna] = fn(grade[linha][coluna])


def solucao(grade, instrucoes, **kwargs):
    for tipo, *indices in instrucoes:
        if tipo == 'on':
            opera_interruptor(grade, kwargs['on'], *indices)
        elif tipo == 'off':
            opera_interruptor(grade, kwargs['off'], *indices)
        elif tipo == 'toggle':
            opera_interruptor(grade, kwargs['toggle'], *indices)
        else:
            raise ValueError(f'??? {tipo}.')

    return sum(sum(linha) for linha in grade)
