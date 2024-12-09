import hashlib


def encontrar_hash(ba, inicio):
    i = 1
    while True:
        n = bytearray(str(i), 'utf-8')
        h = hashlib.new('md5')
        h.update(ba + n)
        if h.hexdigest().startswith(inicio):
            return i

        i += 1


def solucao1(ba):
    return encontrar_hash(ba, '00000')


def solucao2(ba):
    return encontrar_hash(ba, '000000')
