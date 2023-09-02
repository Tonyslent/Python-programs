base = int(input('Digite aqui um número: '))
tot = 0
for primo in range(1, base + 1):
    if base % primo == 0:
        print('\033[1;35m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(primo), end='')
print('\n\033[mO número \033[35m{}\033[m foi divisivel \033[35m{}\033[m vez(es)'.format(base, tot))
if tot == 2:
    print('Por isso, ele é um número \033[1;32mPRIMO\033[m')
else:
    print('Por isso, ele \033[1;31mNÃO\033[m é um número primo')
