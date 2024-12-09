from . import solucao1, solucao2


print('Testando solucao1')

resultado = solucao1(b'abcdef')
esperado = 609043
assert resultado == esperado, f'Esperado `{esperado}`, resultado `{resultado}`.'

resultado = solucao1(b'pqrstuv')
esperado = 1048970
assert resultado == esperado, f'Esperado `{esperado}`, resultado `{resultado}`.'
print('OK!\n')


print('* ', solucao1(b'iwrupvqb'))
print('** ', solucao2(b'iwrupvqb'))
