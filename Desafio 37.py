#VARIAVEIS
x = int(input('Digite aqui um número \033[4;36minteiro\033[m: ' ))
print('TABELA DE CONVERSÃO\n1 = Binário\n2 = Octal\n3 = Hexadecimal')
c = int(input('Qual dos \033[4;36mmétodos de conversão\033[m \033[4;32macima\033[m você deseja: '))

#COMANDOS
if c == 1:
    print('O valor {} convertido para \033[4;36mbinário\033[m é \033[1;4;32m{}\033[m'.format(x, bin(x)[2:]))
elif c == 2:
    print('O valor {} convertido para \033[4;36moctal\033[m é \033[1;4;32m{}\033[m'.format(x, oct(x)[2:]))
elif c == 3:
    print('O valor {} convertido para \033[4;36mhexadecimal\033[m é \033[1;4;32m{}z\033[m'.format(x, hex(x)[2:]))