import itertools as i


def combinacoes_possiveis(volume, garrafas):
    total = 0

    for n in range(1, len(garrafas) + 1):
        for combinacao in i.combinations(garrafas, n):
            if sum(combinacao) == volume:
                total += 1 

    return total


def combinacoes_possiveis_com_menor_numero_garrafas(volume, garrafas):
    for n in range(1, len(garrafas) + 1):
        total = 0
        for combinacao in i.combinations(garrafas, n):
            if sum(combinacao) == volume:
                total += 1

        if total:
            return total

    return total

