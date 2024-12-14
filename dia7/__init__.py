from re import fullmatch as fm


def mod(v):
    return v % (2 ** 16)


def recur(v, d, p, fn):
    if p(v):
        return v
    else:
        return fn(v, d)


def resolve(k, d):

    if type(k) == int:
        return k

    e = d[k]

    if type(e) == int:
        return e

    elif len(e) == 1:
        v = recur(e[0],
                  d,
                  lambda v: type(v) == int,
                  resolve)

        d[k] = v
        return v

    elif len(e) == 2:
        v = mod(~recur(e[1],
                       d,
                       lambda v: type(v) == int,
                       resolve))

        d[k] = v
        return v

    else:
        a, f, b = e
        r1 = resolve(a, d)
        r2 = resolve(b, d)

        if f == 'AND':
            v = r1 & r2
            d[k] = v
            return v

        elif f == 'OR':
            v = r1 | r2
            d[k] = v
            return v

        elif f == 'LSHIFT':
            v = r1 << r2
            d[k] = v
            return v

        elif f == 'RSHIFT':
            v = r1 >> r2
            d[k] = v
            return v

        else:
            raise ValueError(f'??? {e}')


def solucao1(it):
    converte = lambda s: int(s) if fm(r'\d+', s) else s
    circuito = {}

    for linha in it:
        e, k = linha.strip().split(' -> ')
        circuito[k] = tuple(converte(t) for t in e.split(' '))

    return resolve('a', circuito)


def solucao2(it):
    converte = lambda s: int(s) if fm(r'\d+', s) else s
    circuito = {}

    for linha in it:
        e, k = linha.strip().split(' -> ')
        circuito[k] = tuple(converte(t) for t in e.split(' '))

    copia = circuito.copy()

    resolve('a', circuito)
    copia['b'] = circuito['a']

    return resolve('a', copia)
