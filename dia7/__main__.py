from . import solucao1, solucao2
from sys import argv


if len(argv) > 1:

    with open(argv[1], 'r') as f:
        print('*', solucao1(f))

    with open(argv[1], 'r') as f:
        print('**', solucao2(f))


else:

    print('Testando medir')

    instrucoes = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'g -> l',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]

    esperado = {('x',123),
                ('y',456),
                ('d',72),
                ('e',507),
                ('f',492),
                ('g',114),
                ('h',65412),
                ('i',65079),
                ('l',114),}

    assert False

    print('OK!\n')
