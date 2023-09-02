import math

x = float(input('Digite aqui um numero e eu irei arredondar ele para você: '))

print('O número \033[32m{}\033[m arredondado é \033[36m{}'.format(x,math.floor(x)))