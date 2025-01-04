from sys import argv
from pprint import pprint
from . import maior_distancia_percorrida, maior_pontuacao, renas


if len(argv) > 1:
    relatorio = '''Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
                   Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
                   Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
                   Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
                   Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
                   Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
                   Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
                   Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
                   Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.'''

    print(' *', maior_distancia_percorrida(renas(relatorio), 2503))
    print('**', maior_pontuacao(renas(relatorio), 2503))

else:
    exemplo = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
                 Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

    pprint(maior_distancia_percorrida(renas(exemplo), 1000))
    pprint(maior_pontuacao(renas(exemplo), 1000))

