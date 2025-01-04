def deserializa(it):
    return [[(1 if c == '#' else 0) for c in l.strip()] for l in it]


def anima(grade, vezes):
    lins = range(len(grade))
    cols = range(len(grade))

    def in_range(t):
        l, c = t
        return l in lins and c in cols


    def vizinhos(l, c):
        acima = filter(in_range, [(l-1, c-1), (l-1, c), (l-1, c+1)])
        lado = filter(in_range, [(l, c-1), (l, c+1)])
        abaixo = filter(in_range, [(l+1, c-1), (l+1, c), (l+1, c+1)])
        return [grade[l][c] for l, c in [*acima, *lado, *abaixo]]


    def acende(a, l, c):
        total_vizinhos = sum(vizinhos(l, c))
        if a:
            return 1 if total_vizinhos in [2, 3] else 0
        else:
            return 1 if total_vizinhos == 3 else 0


    while vezes:
        nova_grade = []
        for l, linha in enumerate(grade):
            nova_grade.append([acende(aceso, l, c) for c, aceso in enumerate(linha)])
        vezes -= 1

        grade = nova_grade

    return grade


def anima_quebrado(grade, vezes):
    lins = range(len(grade))
    cols = range(len(grade))

    def in_range(t):
        l, c = t
        return l in lins and c in cols


    def vizinhos(l, c):
        acima = filter(in_range, [(l-1, c-1), (l-1, c), (l-1, c+1)])
        lado = filter(in_range, [(l, c-1), (l, c+1)])
        abaixo = filter(in_range, [(l+1, c-1), (l+1, c), (l+1, c+1)])
        return [grade[l][c] for l, c in [*acima, *lado, *abaixo]]

    pl = 0
    pc = 0
    ul = len(grade) - 1
    uc = len(grade[0]) - 1

    cantos = [(pl, pc), (pl, uc), (ul, pc), (ul, uc)]
    for l, c in cantos:
        grade[l][c] = 1

    def acende(a, l, c):
        if (l, c) in cantos:
            return 1
        else:
            total_vizinhos = sum(vizinhos(l, c))
            if a:
                return 1 if total_vizinhos in [2, 3] else 0
            else:
                return 1 if total_vizinhos == 3 else 0


    while vezes:
        nova_grade = []
        for l, linha in enumerate(grade):
            nova_grade.append([acende(aceso, l, c) for c, aceso in enumerate(linha)])
        vezes -= 1

        grade = nova_grade

    return grade

