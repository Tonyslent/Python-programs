from time import sleep
termo1 = int(input('Qual o \033[1;31mprimero\033[m termo da \033[1;33mPA\033[m: '))
razao = int(input('Qual a \033[1;34mrazão\033[m da \033[1;33mPA\033[m: '))
resultado = 0
print('A \033[1;35mprogrssão aritimética\033[m é: ')
for pa in range(1, 11):
    resultado = termo1 + (pa - 1) * razao
    print('\033[1;34m',resultado,'\033[m', end=' -> ')
    sleep(0.5)
print('\033[1;32mFIM\033[m')
