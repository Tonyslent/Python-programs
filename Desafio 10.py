#Considere
#US$1.00 = R$3,27
x = float(input('Quantos \033[1;34mreais\033[m você tem na carteira: '))
d = 3.27
r = x / d

print('Você poderia \033[1;32mtransformar\033[m seus \033[1;34m{} reais\033[m em \033[1;34m{:.2f} dólares'.format(x,r))