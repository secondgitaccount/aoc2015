def soma_recursiva(dados, *ignorar):
    if type(dados) == int:
        return dados

    elif type(dados) == list:
        return sum(map(lambda d: soma_recursiva(d, *ignorar), dados))

    elif type(dados) == dict:
        if not any(map(lambda v: v in ignorar, dados.values())):
            return sum(map(lambda d: soma_recursiva(d, *ignorar), dados.values()))
        else:
            return 0

    else:
        return 0
