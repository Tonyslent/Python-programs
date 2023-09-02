import random
import math
print('\033[1;35;40mRoleta da Sorte\033[m')
print('Aqui vão ser \033[32msorteados\033[m os alunos para que um apague o quadro')
aluno1 = str(input('Qual o nome do \033[31mprimeiro aluno\033[m: '))
aluno2 = str(input('E o \033[33msegundo\033[m: '))
aluno3 = str(input('E o \033[35mterceiro\033[m: '))
aluno4 = str(input('Por fim, qual o nome do \033[36multimo aluno\033[m: '))
nomes = aluno4, aluno3, aluno2, aluno1



print('O aluno selecionado para apagar o quadro foi \033[32m{}'.format(random.choice(nomes)))

