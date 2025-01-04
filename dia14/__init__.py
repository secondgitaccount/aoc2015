class Rena:
    def __init__(self, velocidade, duracao_voo, duracao_descanso):
        self.velocidade = velocidade
        self.duracao_voo = duracao_voo
        self.duracao_descanso = duracao_descanso
        self.voando = duracao_voo
        self.descansando = 0


    def move(self):
        if self.descansando:
            self.descansando -= 1
            self.voando = not self.descansando and self.duracao_voo 
            return False

        else:
            self.voando -= 1
            self.descansando = not self.voando and self.duracao_descanso 
            return True


def renas(relatorio):
    rs = {}
    for l in relatorio.split('\n'):
        info = l.strip().split(' ')
        rs[info[0]] = Rena(*map(int, (info[i] for i in (3, 6, 13))))

    return rs


def maior_distancia_percorrida(renas, duracao):
    distancias = dict((r, 0) for r in renas.keys())

    while duracao:
        for c, r in renas.items():
            if r.move():
                distancias[c] += r.velocidade

        duracao -= 1

    return max(distancias.items(), key=lambda t: t[1])


def maior_pontuacao(renas, duracao):
    distancias = dict((r, 0) for r in renas.keys())
    pontuacao = dict((r, 0) for r in renas.keys())

    while duracao:
        for c, r in renas.items():
            if r.move():
                distancias[c] += r.velocidade

        ganhador, distancia = max(distancias.items(), key=lambda t: t[1])

        for g, _ in filter(lambda t: t[1] == distancia, distancias.items()):
            pontuacao[g] += 1

        duracao -= 1

    return max(pontuacao.items(), key=lambda t: t[1])

