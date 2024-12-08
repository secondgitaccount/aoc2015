def solucao1(instrucao):
    piso = 0

    for i in instrucao:
        if i == '(':
            piso += 1
        elif i == ')':
            piso -= 1

    return piso


def solucao2(instrucao):
    indice = -1
    piso = 0

    for p, i in enumerate(instrucao, 1):
        if i == '(':
            piso += 1
        elif i == ')':
            piso -= 1
            if piso < 0:
                return p

    return indice
