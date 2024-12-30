from sys import argv
from . import calcula_pontuacao, combina, deserializa 


if len(argv) > 1:
    descricao = '''Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
                   PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
                   Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
                   Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8'''

    ingredientes = [*deserializa(l.strip() for l in descricao.split('\n'))]
    receitas = combina(100, *ingredientes)
    resultado = max(map(calcula_pontuacao, receitas))

    print(' *', resultado)
    receitas = combina(100, *ingredientes)
    resultado = max(map(lambda r: calcula_pontuacao(r, lambda r: r['calories'] == 500), receitas))
    print('**', resultado)

else:

    exemplo = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
                 Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

    ingredientes = [*deserializa(l.strip() for l in exemplo.split('\n'))]

    print('Testando pontuacao_receita.')
    esperado = 62842880
    receitas = combina(100, *ingredientes)
    resultado = max(map(calcula_pontuacao, receitas))

    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    esperado = 57600000
    receitas = combina(100, *ingredientes)
    resultado = max(map(lambda r: calcula_pontuacao(r, lambda r: r['calories'] == 500), receitas))
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('Ok!')

