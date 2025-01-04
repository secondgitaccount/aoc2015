def agrupa(xs):
    grupos = []
    cabeca = [xs[0]]

    for x in xs[1:]:
        if x == cabeca[-1]:
            cabeca.append(x)
        else:
            grupos.append(cabeca)
            cabeca = [x]
    else:
        grupos.append(cabeca)

    return grupos


def look_and_say(xs, r=1):

    def __recur__(xs, r):
        if not r:
            return xs

        resultado = []

        for quantidade, n in map(lambda xs: (str(len(xs)), xs[0]), agrupa(xs)):
            resultado.append(quantidade)
            resultado.append(n)

        return __recur__(resultado, r-1)


    return ''.join(__recur__([*xs], r))
