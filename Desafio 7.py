resp1 = int(input('\033[1mQual foi a sua nota na prova de matemática: '))
resp2 = int(input('E no trabalho bimestral: '))

media = resp1 + resp2
mediaf = media / 2

print('Sua nota média nesse bimestre foi \033[4;32m{}\033[m de 10'.format(mediaf))
