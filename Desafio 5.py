x = int(input('\033[4;33;36mDigite um número e eu direi à você qual é o sucessor e o antecessor:\033[m '))
resultado1 = x - 1
resultado2 = x + 1
print('O número antecessor ao seu é \033[4;35m{}\033[m e o sucessor dele é \033[4;35m{}\033[m'.format(resultado1, resultado2))