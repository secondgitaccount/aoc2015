from sys import argv
from pprint import pprint
from . import compara_exatamente, compara_iguais_maiores_menores, deserializa


if len(argv) > 1:
    with open(argv[1], 'r') as f:
        tias = [*enumerate(map(deserializa, f), 1)]

        print(' *', [*filter(compara_exatamente, tias)])
        print('**', [*filter(compara_iguais_maiores_menores, tias)])

