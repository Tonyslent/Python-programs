print('aumento'.upper())
print('Contexto: sua empresa decidiu dar um aumento aos seus funcionários, sendo que,\nse você ganha mais que 1250 reais, seu aumento é de 10%, caso contrario,\nseu aumento é de 15%.')
sal = float(input('Qual o seu salário: '))
au = ''
if sal <= 1250:
    au = sal * 0.15 + sal
else:
    au = sal * 0.1 + sal
print('Seu salario que era {:.2f} após o aumento vai ser {:.2f}'.format(sal,au ))
