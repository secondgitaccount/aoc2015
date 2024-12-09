def area_total(l, w, h):
    partes = [
        l * w,
        w * h,
        h * l,
    ]

    return sum(map(lambda n: 2 * n, partes)) + sorted(partes)[0]


def totalizador(it, calculador):
    total = 0
    for dimensoes in it:
        total += calculador(*dimensoes)

    return total


def solucao1(it):
    return totalizador(it, area_total)


def comprimento_total(l, w, h):
    volume = l * w * h
    menor, *_ = sorted([
        2 * l + 2 * w,
        2 * w + 2 * h,
        2 * h + 2 * l,
    ])

    return volume + menor


def solucao2(it):
    return totalizador(it, comprimento_total)
