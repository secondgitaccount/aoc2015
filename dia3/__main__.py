from . import solucao1, solucao2
from sys import argv


if len(argv) > 1:
    with open(argv[1]) as file:
        for line in file:
            print(solucao1(line.strip()))
            print(solucao2(line.strip()))

else:

    print('Testando solucao1')

    direcoes = ''
    resultado = solucao1(direcoes)
    esperado = 1
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '>'
    resultado = solucao1(direcoes)
    esperado = 2
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '^>v<'
    resultado = solucao1(direcoes)
    esperado = 4
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '^v^v^v^v^v'
    resultado = solucao1(direcoes)
    esperado = 2
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    print('OK!\n')


    print('Testando solucao2')

    direcoes = ''
    resultado = solucao2(direcoes)
    esperado = 1
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '^v'
    resultado = solucao2(direcoes)
    esperado = 3
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '^>v<'
    resultado = solucao2(direcoes)
    esperado = 3
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    direcoes = '^v^v^v^v^v'
    resultado = solucao2(direcoes)
    esperado = 11
    assert resultado == esperado, f'Esperado `{esperado}` para `{direcoes}`, resultado `{resultado}`.'

    print('OK!\n')
