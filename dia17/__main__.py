from sys import argv
from . import combinacoes_possiveis, combinacoes_possiveis_com_menor_numero_garrafas


if len(argv) > 1:
    volume = 150
    garrafas = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
    resultado = combinacoes_possiveis(volume, garrafas)
    print(' *', resultado)
    resultado = combinacoes_possiveis_com_menor_numero_garrafas(volume, garrafas)
    print('**', resultado)

else:
    print('Testando combinacoes_possiveis.')

    exemplo = [20, 15, 10, 5, 5]
    volume = 25

    esperado = 4
    resultado = combinacoes_possiveis(volume, exemplo)
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'
    print('Ok!')

    print('Testando combinacoes_possiveis_com_menor_numero_garrafas.')

    esperado = 3
    resultado = combinacoes_possiveis_com_menor_numero_garrafas(volume, exemplo)
    assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

    print('Ok!')

