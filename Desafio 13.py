print('\033[1;35mVocê vai receber um aumento salarial de 15%.')
x = float(input('\033[32mQual o seu salário:\033[m '))

percent = 0.15
aumento = x * percent
salarion = x + aumento

print('\033[1mSeu salário antigo era R$ \033[4;36m{:.2f}\033[m \033[1m e agora ele é R$ \033[4;36m{:.2f}\033[m \033[1mapós o aumento.'.format(x, salarion))
