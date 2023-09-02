import math
num = int(input('Digite um número e eu direi a você se ele é impar ou par: '))
num1 = num % 2
if num1 == 0:
    print('Seu número é PAR!')
else:
    print('Seu número é ÍMPAR!')