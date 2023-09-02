km = float(input('Quantos \033[32mquilometros\033[m foram percorridos: '))
dia = int(input('Quantos \033[32mdias\033[m você usou o carro: '))

resul1 = km * 0.15
resul2 = dia * 60
resulf = resul2 + resul1

print('O total a se pagar pelo uso do carro é de \033[1;34mR${:.2f}'.format(resulf))