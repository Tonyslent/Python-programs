import random
#variaveis
print('''\033[1;4;35mJOKENPÔ\033[m
\033[1;35m[ 1 ]\033[m - \033[1;32mPEDRA\033[m
\033[1;35m[ 2 ]\033[m - \033[1;32mPAPEL\033[m
\033[1;35m[ 3 ]\033[m - \033[1;32mTESOURA\033[m''')
mao = int(input('\nQual você escolhe: '))
pedra = 1
papel = 2
tesoura = 3
bot = random.randint(1,3)
#comandos
print('\033[1;35m==\033[m' * 15)
if bot == 1:
    print('O adversario escolheu \033[1;35mPEDRA!\033[m')
elif bot == 2:
    print('O adversario escolheu \033[1;35mPAPEL!\033[m')
elif bot == 3:
    print('O adversario escolheu \033[1;35mTESOURA!\033[m')
if mao  == 1:
    print('O jogador escolheu \033[1;35mPEDRA!\033[m')
elif mao == 2:
    print('O jogador escolheu \033[1;35mPAPEL!\033[m')
elif mao == 3:
    print('Ojogador escolheu \033[1;35mTESOURA!\033[m')
print('\033[1;35m==\033[m' * 15)
if mao == pedra and bot == tesoura:
    print('Você venceu!')
elif mao == pedra and bot == papel:
    print('Você perdeu, que pena!')
elif mao == pedra and bot == pedra:
    print('Empate')
if mao == papel and bot == tesoura:
    print('Você perdeu, que pena!')
elif mao == papel and bot == papel:
    print('Empate')
elif mao == papel and bot == pedra:
    print('Você venceu!')
if mao == tesoura and bot == tesoura:
    print('Empate')
elif mao == tesoura and bot == papel:
    print('Você venceu!')
elif mao == tesoura and bot == pedra:
    print('Você perdeu, que pena!')
print('FIM DE JOGO')