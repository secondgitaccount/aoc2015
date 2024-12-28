import itertools as i
import functools as f


def cv(line):
    info = line.strip().replace('gain ', '').replace('lose ', '-').split(' ')
    return (info[0], info[-1][:-1]), int(info[2])


def indices_membros(it):
    indices = dict(cv(p) for p in it)
    membros = set()
    for p in indices.keys():
        membros.add(p[0])
        membros.add(p[1])

    return indices, membros


def pares(mesa):
    c = i.cycle(mesa)
    return [*i.pairwise([next(c) for _ in range(len(mesa) + 1)])]


def soma_felicidade(indices, mesa):
    return sum([indices[(a, b)] + indices[(b, a)]
                for a,b
                in mesa])

def maior_soma_felicidade(indices, membros):
    permutacoes = map(pares, i.permutations(membros))
    soma = f.partial(soma_felicidade, indices)

    return max(map(soma, permutacoes))

