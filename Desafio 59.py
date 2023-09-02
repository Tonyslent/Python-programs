from time import sleep
x = float(input('Qual é o \033[1;32mprimeiro\033[m valor: '))
y = float(input('Qual é o \033[1;33msegundo\033[m valor: '))
maior = 0
resultado = 0
opcao = 0
while opcao != 5:
    sleep(1)
    print('=-=' * 10)
    opcao = int(input('''\033[1;35m[ 1 ]\033[m\033[1m SOMAR\n\033[1;35m[ 2 ]\033[m\033[1m MULTIPLICAR
\033[1;35m[ 3 ]\033[m\033[1m MAIOR\n\033[1;35m[ 4 ]\033[m\033[1m NOVOS NÚMEROS\n\033[1;35m[ 5 ]\033[m\033[1m SAIR
\033[4mQual a sua opção\033[m: '''))
    sleep(1)
    if opcao == 1:
        resultado = x + y
        print('A \033[1;31mSOMA\033[m entre \033[1;32m{}\033[m e \033[1;33m{}\033[m é \033[1;35m{}\033[m'.format(x, y, resultado))
    if opcao == 2:
        resultado = x * y
        print('A \033[1;31mMULTIPLICAÇÃO\033[m entre \033[1;32m{}\033[m e \033[1;33m{}\033[m  é \033[1;35m{}\033[m'.format(x, y, resultado))
    if opcao == 3:
        if x > y:
            maior = x
            print('\033[1mO maior valor é \033[35m{}\033[m'.format(maior))
        elif y > x:
            maior = y
            print('\033[1mO maior valor é \033[35m{}\033[m'.format(maior))
        elif x == y:
            print('\033[1mOs dois valores são \033[35miguais\033[m')
    if opcao == 4:
        print('NOVOS NÚMEROS')
        x = float(input('Qual é o \033[1;32mprimeiro\033[m número: '))
        y = float(input('Qual é o \033[1;33msegundo\033[m número: '))
    if opcao == 5:
        print('\033[1;32mFINALIZANDO, AGUARDE', end='')
        print('.', end=''), sleep(1)
        print('.', end=''), sleep(1)
        print('.')
        sleep(2)
        break
