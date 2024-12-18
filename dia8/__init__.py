def adiciona(n, t):
    if t == 'HEX':
        v = 5
    elif t in ['SLASH', 'QUOTE']:
        v = 4
    else:
        v = 1

    return n + v

