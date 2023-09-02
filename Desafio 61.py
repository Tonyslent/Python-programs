termo1 = int(input('Qual o \033[32mPRIMEIRO\033[m termo da PA: '))
razao = int(input('Qual é a \033[31mRAZÃO\033[m dela: '))
termo = termo1
contador = 1

while contador <= 10:
    print('\033[35m{}\033[m'.format(termo), end='-> ')
    termo += razao
    contador += 1
print('\033[33mFIM', end='')
