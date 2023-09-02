import random
par = 'P'
impar = 'I'
contador = 0
while True:
    botbase = random.randint(1, 11)
    print('\033[31m---' * 15)
    print('PAR ou ÍMPAR'.center(45))
    print('---' * 15)
    playernum = int(input('\033[mDiga um \033[35mvalor\033[m: '))
    print('\033[31m---\033[m' * 15)
    pergteste = str(input('Par ou Ímpar [P/I]: '))
    resul = ''
    print('\033[31m---\033[m' * 15)
    teste = botbase + playernum
    print(f'Você escolheu \033[35m{playernum}\033[m e o BOT escolheu \033[33m{botbase}\033[m')
    if teste % 2 == 0:
        resul = 'PAR'
        print(f'A soma dos dois é \033[34m{botbase+playernum}\033[m e o resultado deu \033[4;32m{resul}\033[m')
    if teste % 1.5 == 0:
        resul = 'ÍMPAR'
        print(f'A soma dos dois é \033[34m{botbase+playernum}\033[m e o resultado deu \033[4;32m{resul}\033[m')
    print('\033[31m---\033[m' * 15)
    if resul == 'PAR' and pergteste == par:
        print('Você VENCEU!!!\nvamos Jogar de novo...')
        contador += 1
    elif resul == 'ÍMPAR' and pergteste == impar:
        print('Você VENCEU!!!\nvamos Jogar de novo...')
        contador += 1
    else:
        print('\033[41;30mVocê PERDEU!!!\033[m')
        break
print('\033[31m---' * 15)
print(' GAME OVER '.center(45, '='))
print(f'\033[mVocê venceu \033[32m{contador}\033[m vez(es)'.center(55))
print('\033[31m---' * 15, '\033[m')
