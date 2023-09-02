x = int(input('\033[1;35;40mEscreva a medida em metros que eu te mostrarei em centimetros e milimetros: '))

cent = x * 100
mili = x * 1000

print('Essa medida em centimetros é \033[7m{}\033[m\033[1;35;40m e em milimetros é \033[7m{}\033[m'.format(cent, mili))