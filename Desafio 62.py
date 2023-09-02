termo1 = int(input('Qual o \033[32mPRIMEIRO\033[m termo da PA: '))
razao = int(input('Qual é a \033[31mRAZÃO\033[m dela: '))
termo = termo1
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('\033[35m{}\033[m'.format(termo), end='-> ')
        termo += razao
        contador += 1
    print('\033[33mPAUSA\033[m')
    mais = int(input('Você deseja continuar?\nCaso queira, digite a quantidade que desejar\nCaso não queira continuar, digite 0: '))
    if mais == 0:
        print('\033[32mFIM\033[m')
contador -= 1
print('O número \033[34mTOTAL\033[m de termos foi de \033[36m{}\033[m apresentados'.format(contador))

