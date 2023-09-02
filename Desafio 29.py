import math
print('RADAR    80km/h')
vel = int(input('Qual a sua velocidade quando você passou no radar: '))

multa = 7
preco = ((vel - 80) * multa)

if vel <= 80:
    print('Continue assim!!!')
if vel > 80:
    print(f'Você ultrapassou o limite do radar, e por isso, vai ser multado em {preco} reais')