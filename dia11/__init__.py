letras_invalidas = set('iol')

def contem_letra_invalida(senha):
    return bool(set(senha).intersection(letras_invalidas))


def pares_distintos_sem_sobreposicao(sequencia):

    pares = []
    for i in range(len(sequencia) - 1):
        par = sequencia[i:i+2]
        if not pares or pares[-1] != par:
            pares.append(par)

    return {p for p in pares if p[0] == p[1]}


def trios_ascendentes(sequencia):
    for i in range(len(sequencia) - 2):
        trio = [*map(ord, sequencia[i:i+3])]
        if trio[1] - trio[0] == 1 and trio[2] - trio[1] == 1:
            return True

    return False


def proxima(letra):
    primeira = ord('a')
    ultima = ord('z')
    n = ord(letra)

    if n + 1 > ultima:
        return 'a', True

    return chr(n + 1), False


def incrementa(senha):
    entrada = [*reversed(senha)]

    for i, letra in enumerate(entrada):
        nova_letra, carrega = proxima(letra)
        entrada[i] = nova_letra
        if not carrega:
            break
    else:
        if carrega:
            entrada.append('a')

    return ''.join(reversed(entrada))


def senha_valida(senha):

    if contem_letra_invalida(senha):
        return False

    nao_tem_pares_distintos_sem_sobreposicao = len(pares_distintos_sem_sobreposicao(senha)) < 2

    if nao_tem_pares_distintos_sem_sobreposicao:
        return False

    if not trios_ascendentes(senha):
        return False

    return True


def proxima_senha(senha, n=1):
    proxima = incrementa(senha)
    while not senha_valida(proxima):
        proxima = incrementa(proxima)

    return proxima_senha(proxima, n-1) if n - 1 else proxima
