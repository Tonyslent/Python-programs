print('\033[1;4;34mIMC\033[m')
#variaveis
peso = float(input('Qual é o seu \033[1;35mpeso\033[m: '))
altura = float(input('Qual a sua \033[1;35maltura\033[m: '))
#calculos
imc = peso / (altura ** 2)
#comandos

if 25 >= imc >= 18.5:
    print('Você está no \033[1;32mPESO IDEAL\033[m')
elif imc < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO')
    print('\033[1;31mPROCURE UM MÉDICO!!!\033[m')
elif 30 >= imc >= 25:
    print('Você está \033[1;35mSOBREPESO')
    print('\033[1;31mPROCURE UM MÉDICO!!!\033[m')
elif 40 >= imc >= 30:
    print('Você está com \033[1;33mOBESIDADE')
    print('\033[1;31mPROCURE UM MÉDICO!!!\033[m')
elif imc > 40:
    print('Você está em \033[1;31mOBESIDADE MÓRBIDA')
    print('\033[1;31;44mPROCURE UM MÉDICO!!!\033[m')
print('Seu \033[1;4;36mIMC\033[m é \033[1;4;36m{:.2f}\033[m'.format(imc))