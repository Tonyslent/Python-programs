import random

numero = random.randint(0,5)
print('Pensei em um número que está entre 0 e 5')
num = int(input('Tente adivinhar: '))

if num == numero:
    print('PARABÉNS, VOCÊ ACERTOU!!!')

else:
    print('QUE PENA, VOCÊ PERDEU!!!')