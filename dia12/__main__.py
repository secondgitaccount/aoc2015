from . import soma_recursiva
from json import loads
from sys import argv


if len(argv) > 1:

    with open(argv[1], 'r') as f:
        dados = loads(f.read())
        print(' *', soma_recursiva(dados))
        print('**', soma_recursiva(dados, 'red'))
