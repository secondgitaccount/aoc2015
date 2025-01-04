from . import area_total, comprimento_total, solucao1, solucao2
from sys import argv


if len(argv) > 1:
    with open(argv[1], 'r') as file:
        it = (map(int, line.strip().split('x')) for line in file)
        print(solucao1(it))

    with open(argv[1], 'r') as file:
        it = (map(int, line.strip().split('x')) for line in file)
        print(solucao2(it))

else:

    print('Testando area_total')

    resultado = area_total(2, 3, 4)
    esperado = 58
    assert resultado == esperado, f'''Esperado `{esperado}` para `{(2, 3, 4)}`, resultado `{resultado}`.'''

    resultado = area_total(1, 1, 10)
    esperado = 43
    assert resultado == esperado, f'''Esperado `{esperado}` para `{(1, 1, 10)}`, resultado `{resultado}`.'''

    print('OK!\n')


    print('Testando solucao1')

    dimensoes = iter([(2, 3, 4), (1, 1, 10)])
    resultado = solucao1(dimensoes)
    esperado = 58 + 43
    assert resultado == esperado, f'''Esperado `{esperado}` para `{[(2, 3, 4), (1, 1, 10)]}`, resultado `{resultado}`.'''

    print('OK!\n')


    print('Testando comprimento_total')

    resultado = comprimento_total(2, 3, 4)
    esperado = 34
    assert resultado == esperado, f'''Esperado `{esperado}` para `{(2, 3, 4)}`, resultado `{resultado}`.'''

    resultado = comprimento_total(1, 1, 10)
    esperado = 14
    assert resultado == esperado, f'''Esperado `{esperado}` para `{(1, 1, 10)}`, resultado `{resultado}`.'''

    print('OK!\n')


    print('Testando solucao2')

    dimensoes = iter([(2, 3, 4), (1, 1, 10)])
    resultado = solucao2(dimensoes)
    esperado = 34 + 14
    assert resultado == esperado, f'''Esperado `{esperado}` para `{[(2, 3, 4), (1, 1, 10)]}`, resultado `{resultado}`.'''

    print('OK!\n')
