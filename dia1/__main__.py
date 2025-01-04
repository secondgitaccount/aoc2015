from . import solucao1, solucao2
from sys import argv


if len(argv) > 1:
    with open(argv[1], 'r') as file:
        for line in file:
            print(solucao1(line.strip()))
            print(solucao2(line.strip()))

else:

    print('Testando solucao1')

    instrucoes = [
        (')())())', ')))', -3),
        ('())', '))(', -1),
        (')', '))(', -1),
        ('', '()()', 0),
        ('(())', '()()', 0),
        ('(((', '(()(()(', 3),
        ('(()(()(', '(((', 3),

    ]

    for i in instrucoes:
        i1, i2, piso = i
        resultado = all(map(lambda i: solucao1(i) == piso, [i1, i2]))
        esperado = True
        assert resultado == esperado, f'''Esperado `{esperado}` para `{i1}` e `{i2}` == `{piso}`, resultado `{resultado}`.'''

    print('OK!\n')


    print('Testando solucao2')

    instrucoes = [
        ('(', -1),
        (')', 1),
        ('()())', 5),
    ]

    for instrucao, esperado in instrucoes:
        resultado = solucao2(instrucao)
        assert resultado == esperado, f'''Esperado `{esperado}` para `{instrucao}`, resultado `{resultado}`.'''

    print('OK!\n')
