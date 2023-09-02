import random
numale = random.randint(0, 10)
texto = 'JOGO DO ADIVINHA'
acumulador = 0
print('\033[1;36m',texto.center(30, '='),'\033[m')
tru = False
while not tru:
    player = int(input('Adivinhe o número entre \033[1;36m0\033[m e \033[1;36m10\033[m: '))
    acumulador += 1
    if player == numale:
        tru = True
        print('\033[1;36mAcertou!!!\033[m')
    else:
        if player > numale:
            print('\033[1;36mUm pouco menos...\033[m Tente de novo: ')
        elif player < numale:
            print('\033[1;36mUm pouco mais...\033[m Tente de novo: ')
print('para adivinhar o número foram necessarios \033[1;36m{}\033[m tentativa(s)'.format(acumulador))
