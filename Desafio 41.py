print('\033[1;36mCATEGORIZADOR\033[m')
#variaveis
y = int(input('Em que \033[1;4;32mANO\033[m você nasceu: '))
x = 2023 - y
#comandos
if x <= 9:
    print('Você é da categoria: \033[1;35mMIRIM')
elif x >= 10 and x < 14:
    print('Você é  da categoria: \033[1;35mINFANTIL')
elif x >= 15 and x < 19:
    print('VOcê é da categoria: \033[1;35mJUNIOR')
elif x == 20:
    print('Você é da categoria: \033[1;35mSÊNIOR')
elif x > 20:
    print('Você é da categoria \033[1;35mMASTER')