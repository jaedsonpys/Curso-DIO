import itertools
# usada para iterações e permutações/combinações

string = str(input('String a ser permutada: ')).strip()

result = itertools.permutations(string, len(string))
for r in result:
    print(''.join(r))