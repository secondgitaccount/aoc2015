from . import incrementa, proxima_senha, senha_valida
from sys import argv


if len(argv) > 1:

    print('*', proxima_senha(argv[1]))
    print('**', proxima_senha(argv[1], 2))

else:

    print('Testando incrementa')

    entrada = 'z'
    esperado = 'aa'
    resultado = incrementa(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    entrada = 'zzz'
    esperado = 'aaaa'
    resultado = incrementa(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    entrada = 'xz'
    esperado = 'ya'
    resultado = incrementa(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    print('Ok!')


    print('Testando senha_valida')

    entrada = 'hijklmmn'
    esperado = False
    resultado = senha_valida(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    entrada = 'abbceffg'
    esperado = False
    resultado = senha_valida(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    entrada = 'abbcegjk'
    esperado = False
    resultado = senha_valida(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    print('Ok!')


    print('Testando proxima_senha')

    entrada = 'abcdefgh'
    esperado = 'abcdffaa'
    resultado = proxima_senha(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    entrada = 'ghijklmn'
    esperado = 'ghjaabcc'
    resultado = proxima_senha(entrada)
    assert esperado == resultado, f'Esperado `{esperado}` para `{entrada}`, resultado `{resultado}`.'

    print('Ok!')
