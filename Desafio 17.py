import math

x = float(input('Qual o \033[36mvalor\033[m do \033[31mcateto Oposto:\033[m '))
y = float(input('E o \033[35madjacente\033[m: '))

x2 = x ** 2
y2 = y ** 2
resulf = x2 + y2
raiz = math.sqrt(resulf)
print('O \033[36mvalor\033[m da \033[34mhipotenusa\033[m é de \033[1;33m{:.0f}\033[m ou \033[1;33m{:.3f}\033[m'.format(resulf, raiz))