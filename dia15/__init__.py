from functools import reduce


def deserializa(it):
    for l in it:
        t, q = l.split(': ')
        info = dict((c, int(v))
                    for c, v
                    in map(lambda s: s.split(' '),
                           q.split(', ')))

        info['type'] = t
        yield info


def combina(m, *ingredientes):
    if len(ingredientes) == 1:
        yield [(m, ingredientes[0])]
    else:
        ingrediente, *resto = ingredientes

        limite = 1 + m - len(ingredientes)

        for i in range(1, limite + 1):
            for r in combina(m - i, *resto):
                r.append((i, ingrediente))
                yield r


def total_ingrediente(t):
    n, i = t
    return dict((c, n * v if type(v) == int else v) 
                for c, v
                in i.items())


def soma_caracteristicas_ingredientes_diferentes(ingredientes):
    def acc(p, atual):
        return dict((c, (p[c] + v) if type(v) == int else 'acc')
                    for c, v
                    in atual.items())

    return reduce(acc, ingredientes)


def pontuacao_receita(receita, *chaves):
    p = 1
    for c in chaves: 
        if receita[c] <= 0:
            return 0

        p *= receita[c]

    return p


def calcula_pontuacao(r, p=lambda x: True):
    totais_ingredientes = map(total_ingrediente, r)
    soma_caracteristicas = soma_caracteristicas_ingredientes_diferentes(totais_ingredientes)
    if not p(soma_caracteristicas):
        return 0

    return pontuacao_receita(soma_caracteristicas,
                             'capacity',
                             'durability',
                             'flavor',
                             'texture')

