acumulador = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        acumulador += c
print('A soma dos \033[1;35m{}\033[m valores \033[4;36mmultiplos de 3\033[m que são \033[4;36mímpares\033[m é: \033[1;35m{}\033[m'.format(contador, acumulador))
