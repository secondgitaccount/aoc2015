identificador = dict(children=3,
                     cats=7,
                     samoyeds=2,
                     pomeranians=3,
                     akitas=0,
                     vizslas=0,
                     goldfish=5,
                     trees=3,
                     cars=2,
                     perfumes=1)


def deserializa(l):
    l = l.strip()
    index = l.index(': ')
    info = l[index + 2:].split(', ')
    return dict((c, int(v))
                 for c, v
                 in map(lambda s: s.split(': '),
                        info))


def compara(fn, *chaves):
    def _(d):
        for chave in chaves:
            if chave in d and not fn(d[chave], identificador[chave]):
                return False

        return True

    return _


def valida(*comparadores):
    def _(t):
        _, d = t
        for comp in comparadores:
            if not comp(d):
                return False

        return True

    return _


compara_exatamente = valida(compara(lambda a, b: a == b,
                                    *identificador.keys()))

GT = 'cats', 'trees'
LT = 'pomeranians', 'goldfish'
EQ = (k 
      for k
      in identificador.keys()
      if not k in (*GT, *LT)) 

compara_iguais = compara(lambda a, b: a == b, *EQ)
compara_maiores = compara(lambda a, b: a > b, *GT)
compara_menores = compara(lambda a, b: a < b, *LT)

compara_iguais_maiores_menores = valida(compara_iguais,
                                        compara_maiores,
                                        compara_menores)

