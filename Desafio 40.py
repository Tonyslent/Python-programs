print('\033[1;4;35mMÉDIA ESCOLAR\033[m')
#variaveis
x = float(input('Qual foi a \033[1;4;32mnota\033[m da prova: '))
y = float(input('E qual foi a \033[1;4;32mnota\033[m do dever de casa: '))
#contas
media = (x + y) / 2
#comandos
if media < 5:
    print('\033[1;31mREPROVADO!!!')
elif media >= 5 and media < 7:
    print('\033[1;33mRECUPERAÇÃO!!!')
elif media >= 7:
    print('\033[1;32mAPROVADO!!!')