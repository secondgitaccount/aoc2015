def solucao1(strings):
    pares_proibidos = [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]

    total = 0

    for string in strings:
        vogais = filter(lambda l: l in 'aeiou', string)
        if len([*vogais]) < 3:
            continue

        pares = [*zip(string[:-1], string[1:])]
        if not len([*filter(lambda t: t[0] == t[1], pares)]):
            continue

        if len([*filter(lambda t: t in pares_proibidos, pares)]):
            continue

        total += 1

    return total


def trios_letras(string):
    return [*zip(string[:-2],
                 string[1:-1],
                 string[2:])]


def pares_letras(string):
    pares = []
    for i, _ in enumerate(string[:-1]):
        pares.append((string[i:i+2], i, i+1))

    return pares


def contem_pares_repetidos(string):
    pares = pares_letras(string)
    for i, (p1, c1, f1) in enumerate(pares, 1):
        for (p2, c2, f2) in pares[i:]:
            if p1 == p2 and not c2 in [c1, f1]:
                return True

    return False


def solucao2(strings):
    total = 0
    for string in strings:
        contem_trio = any(filter(lambda t: t[0] == t[2], trios_letras(string)))
        pares_repetidos = contem_pares_repetidos(string)

        if pares_repetidos and contem_trio:
            total += 1

    return total
