acumulador = 0
contador = 0
for soma in range(1, 7):
    x = int(input('\033[1mDigite aqui um número: '))
    if x % 2 == 0:
        acumulador += x
        contador += 1
print('A soma dos \033[1;4;35m{}\033[m números \033[1;31mpares\033[m inseridos é: \033[1;4;35m{}\033[m'.format(contador, acumulador))