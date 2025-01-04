from . import maior_distancia, menor_distancia, roteiros
from sys import argv
from pprint import pprint


if len(argv) > 1:
    with open(argv[1], 'r') as file:
        distancias = {}
        locais = set()

        for line in file:
            origem, destino, distancia = line.strip().replace(' to ', '*').replace(' = ', '*').split('*')
            distancias[(origem, destino)] = int(distancia)
            distancias[(destino, origem)] = int(distancia)
            locais.add(origem)
            locais.add(destino)


        print('*', menor_distancia(roteiros(distancias, locais), distancias))
        print('**', maior_distancia(roteiros(distancias, locais), distancias))

else:

    exemplo = '''London to Dublin = 464
                 London to Belfast = 518
                 Dublin to Belfast = 141'''

    distancias = {}
    locais = set()

    for line in (l.strip() for l in exemplo.split('\n')):

        origem, destino, distancia = line.strip().replace(' to ', '*').replace(' = ', '*').split('*')
        distancias[(origem, destino)] = int(distancia)
        distancias[(destino, origem)] = int(distancia)
        locais.add(origem)
        locais.add(destino)


    for roteiro in roteiros(distancias, locais):

        print(len(roteiro), roteiro)
        print(sum(map(lambda k: distancias[k], roteiro)))


    print('*', menor_distancia(roteiros(distancias, locais), distancias))
    print('**', maior_distancia(roteiros(distancias, locais), distancias))
