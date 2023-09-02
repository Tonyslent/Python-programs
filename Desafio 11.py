y = float(input('Qual a \033[4;33maltura\033[m da sua parede em metros: '))
x = float(input('E a \033[4;35mlargura\033[m: '))
#1 Litro de tinta pinta 2m²
area = x * y
tinta = area / 2

print('Para \033[31mpintar\033[m essa parede você precisará de \033[4;32m{} litros\033[m de tinta'.format(tinta))