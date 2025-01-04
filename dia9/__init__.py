def roteiros(distancias, locais):

    def __recur__(origem, destino, locais):
        if not locais:
            yield []

        else:
            proximos = [*filter(lambda t: t[0] == destino and t[1] in locais, distancias)]
            for o, d in proximos:
                for r in __recur__(o, d, locais.difference({o, d})):
                    r.append((o, d))
                    yield r


    for origem, destino in distancias:
        for r in __recur__(origem, destino, locais.difference({origem, destino})):
            if len(r) == (len(locais) - 2):
                r.append((origem, destino))
                yield r


def calcula_distancia(roteiros, distancias, fn):
    def distancia_total_roteiro(roteiro):

        def distancias_roteiro(roteiro):
            return map(lambda k: distancias[k], roteiro)

        return sum(distancias_roteiro(roteiro))


    return fn(map(distancia_total_roteiro, roteiros))


def menor_distancia(roteiros, distancias):
    return calcula_distancia(roteiros, distancias, min)


def maior_distancia(roteiros, distancias):
    return calcula_distancia(roteiros, distancias, max)
