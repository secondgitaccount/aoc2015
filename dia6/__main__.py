from . import instrucao, monta_grade, solucao
from sys import argv


if len(argv) > 1:

    with open(argv[1], 'r') as file:
        grade = monta_grade(1000)
        solucao1 = solucao(grade,
                           instrucao(file),
                           on=lambda _: 1,
                           off=lambda _: 0,
                           toggle=lambda n: 0 if n else 1)

        print('*', solucao1)


    with open(argv[1], 'r') as file:
        grade = monta_grade(1000)
        solucao2 = solucao(grade,
                           instrucao(file),
                           on=lambda n: 1 + n,
                           off=lambda n: n - 1 if n else n,
                           toggle=lambda n: 2 + n)

        print('**', solucao2)
