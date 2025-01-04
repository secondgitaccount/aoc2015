from . import adiciona
from re import compile
from sys import argv


lex = compile(r'|'.join([
    r'(?P<HEX>\\x[0-9a-f]{2})',
    r'(?P<QUOTE>\\")',
    r'(?P<SLASH>\\\\)',
    r'(?P<CHAR>.)',
]))


if len(argv) > 1:

    with open(argv[1], 'r') as file:
        total = 0

        for line in file:
            total += len(line.strip())

            for m in lex.finditer(line.strip()[1:-1]):
                for k, v in m.groupdict().items():
                    if v:
                        total -= 1

    print('*', total)

    with open(argv[1], 'r') as file:
        lengths = []
        for line in file:
            total = 0
            for m in lex.finditer(line.strip()[1:-1]):
                for k, v in m.groupdict().items():
                    if v != None:
                        total = adiciona(total, k)

            lengths.append(6 + total - len(line.strip()))

        print('**', sum(lengths))

else:

    exemplo = [
        r'""',
        r'"abc"',
        r'"aaa\"aaa"',
        r'"\x27"',
    ]

    total = 0

    for e in exemplo:
        total += len(e)

        for m in lex.finditer(e[1:-1]):
            for k, v in m.groupdict().items():
                if v:
                    total -= 1

    print(total)
