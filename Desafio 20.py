import random
import math

aluno1 = (input('Qual o \033[31mprimeiro aluno\033[m: '))
aluno2 = (input('Qual o \033[32msegundo\033[m: '))
aluno3 = (input('QUal o \033[33mterceiro\033[m: '))
aluno4 = (input('E o \033[34multimo\033[m: '))
grupo = (aluno4, aluno3, aluno2, aluno1)

resulf = random.sample(grupo, k=4)

print('A ordem escolhida foi: \033[1;4;34m', resulf,'\033[m')
