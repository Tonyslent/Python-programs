print('\033[1;31mALISTAMENTO MILITAR\033[m')
ano = int(input('Em qual \033[1;31mANO\033[m você nasceu: '))
anobase = 2023
data = anobase - ano
falta = 18 - data
expirado = data - 18
if data < 18:
    print('Faltam \033[4;31m{}\033[m ano(s) para seu alistamento militar!!!'.format(falta))
elif data == 18:
    print('Você precisa fazer o seu alistamento militar \033[4;31mESSE ANO!!!')
else:
    print('Seu alistamento militar ja passou faz \033[4;31m{}\033[m ano(s)!!!'.format(expirado))