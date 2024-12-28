from sys import argv
from . import indices_membros, maior_soma_felicidade, pares, soma_felicidade


if len(argv) - 1:
    with open(argv[1], 'r') as f:
        indices, membros = indices_membros(f)
        print(' *', maior_soma_felicidade(indices, membros))

        indices2 = indices.copy()
        membros2 = membros.copy()
        membros2.add('Me')

        for m in membros:
            indices2[('Me', m)] = 0
            indices2[(m, 'Me')] = 0

        print('**', maior_soma_felicidade(indices2, membros2))

else:
    exemplo = '''Alice would gain 54 happiness units by sitting next to Bob.
                 Alice would lose 79 happiness units by sitting next to Carol.
                 Alice would lose 2 happiness units by sitting next to David.
                 Bob would gain 83 happiness units by sitting next to Alice.
                 Bob would lose 7 happiness units by sitting next to Carol.
                 Bob would lose 63 happiness units by sitting next to David.
                 Carol would lose 62 happiness units by sitting next to Alice.
                 Carol would gain 60 happiness units by sitting next to Bob.
                 Carol would gain 55 happiness units by sitting next to David.
                 David would gain 46 happiness units by sitting next to Alice.
                 David would lose 7 happiness units by sitting next to Bob.
                 David would gain 41 happiness units by sitting next to Carol.'''

    print(maior_soma_felicidade(*indices_membros(exemplo.split('\n'))))

