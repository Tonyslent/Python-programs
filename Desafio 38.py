print('\033[1;31mCOMPARADOR\033[m')
#variaveis
x = int(input('Digite Aqui um número: '))
y = int(input('Digite aqui outro número: '))
#comandos
if x > y:
    print('O primeiro valor é maior:\033[1;36m',x)
elif x < y:
    print('O segundo valor é maior:\033[1;36m',y)
else:
    print('\033[1;31mNÃO EXISTE\033[m um valor maior pois os dois são iguais')