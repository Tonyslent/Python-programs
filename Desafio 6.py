x = int(input('\033[1;mDgite aqui um número e eu te direi qual o \033[1;31mdobro\033[m, \033[1;32mtriplo\033[m e sua \033[1;33mraiz quadrada\033[m: '))

dobro = x * 2
triplo = x * 3
raiz2 = x ** (1/2)

print('O dobro desse número é \033[1;31m{}\033[m, o triplo \033[1;32m{}\033[m, e a raiz quadrada é \033[1;33m{}'.format(dobro, triplo, raiz2))