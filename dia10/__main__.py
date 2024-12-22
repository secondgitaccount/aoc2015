from . import look_and_say


print('Testando look_and_say')

entrada = '1'
esperado = '11'
resultado = look_and_say(entrada)
assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

entrada = '11'
esperado = '21'
resultado = look_and_say(entrada)
assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

entrada = '21'
esperado = '1211'
resultado = look_and_say(entrada)
assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

entrada = '1211'
esperado = '111221'
resultado = look_and_say(entrada)
assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

entrada = '111221'
esperado = '312211'
resultado = look_and_say(entrada)
assert esperado == resultado, f'Esperado `{esperado}`, resultado `{resultado}`.'

entrada = '1'
esperado = '312211'
vezes = 5
resultado = look_and_say(entrada, vezes)
assert esperado == resultado, f'Esperado `{esperado}` repetindo `look_and_say` {vezes} vezes, resultado `{resultado}`.'

print('Ok!')

print('*', len(look_and_say('1113222113', 40)))
print('**', len(look_and_say('1113222113', 50)))
