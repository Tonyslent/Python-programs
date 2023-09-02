print('\033[1;31mTABUADA\033[m')
multiplicador = int(input('\033[1mDigite aqui um número e eu derei para você a tabuada dele: \033[m'))
tabu = 0
for tabuada in range(1, 11):
        tabu = tabuada * multiplicador
        print('\033[1;35m{}\033[m \033[1mx\033[m \033[1;35m{}\033[m = \033[32m{}\033[m'.format(multiplicador, tabuada, tabu))