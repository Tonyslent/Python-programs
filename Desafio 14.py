temp = float(input('\033[1mQual é a tempuratura em graus Celcius no momento: '))
conv = (temp * 1.8) + 32

print('A temperatura agora é de \033[4;34m{} Fahrenheit'.format(conv))
