from pprint import pprint
from sys import argv
from . import anima, anima_quebrado, deserializa


with open(argv[1], 'r') as f:
    grade = deserializa(f)
    print(' *', sum(map(sum, anima(grade, 100))))
    print('**', sum(map(sum, anima_quebrado(grade, 100))))

