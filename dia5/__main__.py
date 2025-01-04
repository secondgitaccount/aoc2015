from . import contem_pares_repetidos, pares_letras, solucao1, solucao2
from sys import argv


if len(argv) > 1:
    strings = []
    with open(argv[1], 'r') as file:
        for line in file:
            strings.append(line.strip())

        print('* ', solucao1(strings))
        print('** ', solucao2(strings))

else:

    print('Testando pares_letras')

    esperado = [('xy', 0, 1), ('yx', 1, 2), ('xy', 2, 3)]
    resultado = pares_letras('xyxy')
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    esperado = [('aa', 0, 1), ('aa', 1, 2)]
    resultado = pares_letras('aaa')
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('OK!\n')


    print('Testando contem_pares_repetidos')

    esperado = True
    resultado = contem_pares_repetidos('aabcdefgaa')
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    esperado = False
    resultado = contem_pares_repetidos('aaa')
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('OK!\n')


    print('Testando solucao1')

    strings = [
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb',
    ]

    esperado = 2
    resultado = solucao1(strings)
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('OK!\n')


    print('Testando solucao2')

    strings = [
        'qjhvhtzxzqqjkmpb',
        'xxyxx',
        'uurcxstgmygtbstg',
        'ieodomkazucvgmuy',
    ]

    esperado = 2
    resultado = solucao2(strings)
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('OK!\n')
